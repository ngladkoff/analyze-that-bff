from flask_restplus import fields
from services.rest_api import api

dummy = api.model('Dummy', {
    'id': fields.Integer(readOnly=True, description='Unique Identifier'),
    'name': fields.String(required=True, description='Name')
})
