from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from services.routes import router as api_router
from core import config
from core import tasks


def get_application():

    cfg = config.get_settings()
    app = FastAPI(title=cfg.app_title, version=cfg.app_version)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

    app.include_router(api_router, prefix=cfg.api_prefix)

    # Default page
    @app.get("/")
    def read_root(request: Request):
        url = request.url
        return {
            "Description": "Analyze-That-BFF",
            "Docs": f"{url}docs"
            }

    return app


app = get_application()
