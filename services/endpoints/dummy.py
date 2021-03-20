from flask_restplus import Resource
from services.serializers import dummy
from services.rest_api import api

ns = api.namespace('dummy', description='Dummy API')

DUMMYS = [
    {
        'id': 1,
        'name': 'dummy1'
    },
    {
        'id': 2,
        'name': 'dummy2'
    }
]


@ns.route('/')
class DummyCollection(Resource):
    @api.marshal_with(dummy, as_list=True)
    def get(self):
        return DUMMYS
