from fastapi import Security, Request
from fastapi_auth0 import Auth0User, Auth0
from . import config


def get_auth0():
    return Auth0(domain=config.AUTH0_DOMAIN,
                 api_audience=config.AUTH0_API_AUDIENCE,
                 scopes={'user:admin': ''})


def get_req(request: Request,
            user: Auth0User = Security(get_auth0().get_user)):
    return {"user": user, "request": request}
