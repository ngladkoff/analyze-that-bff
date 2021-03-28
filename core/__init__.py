
from fastapi import Security, Request
from fastapi_auth0 import Auth0User, Auth0
from configuration import config


def get_auth0(settings: config.Settings = config.get_settings()):
    return Auth0(domain=settings.auth0_domain,
                 api_audience=settings.auth0_api_audience,
                 scopes={'read:dummys': ''})


def get_req(request: Request,
            user: Auth0User = Security(get_auth0().get_user)):
    return {"user": user, "request": request}
