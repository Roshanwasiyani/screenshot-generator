from flask import Flask
from flask_restx import Api

# Imports apis from api package
from src.api.health_check_api import ns_health_check
from src.api.base_api import ns_base_template

app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app, version='1.0', title='Website Screenshot Generator', prefix='/api/v1')


# Register api
api.add_namespace(ns_health_check)
api.add_namespace(ns_base_template)



if __name__ == '__main__':
    app.run(debug=True)