from flask import Flask
from services import rest_api
from services.endpoints.dummy import ns as dummy_ns

app = Flask(__name__)


@app.route('/')
def index():
    return 'Analyze That BFF'


# Flask-Restplus
# Flask-Restplus settings
app.config['RESTPLUS_SWAGGER_UI_DOC_EXPANSION'] = 'list'
app.config['RESTPLUS_VALIDATE'] = True
app.config['RESTPLUS_MASK_SWAGGER'] = False
app.config['RESTPLUS_ERROR_404_HELP'] = False

# Register API BluePrints
apiBlueprint = rest_api.get_blueprint()
rest_api.api.init_app(apiBlueprint)
rest_api.api.add_namespace(dummy_ns)
app.register_blueprint(apiBlueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
