from flask import Blueprint
from flask_restplus import Api

REST_API = Blueprint('rest_api', __name__, url_prefix='/api/')


def get_blueprint():
    return REST_API


api = Api(version='1.0', title="Analyze That BFF",
          description="Analyze That API Backend For Frontend")
