from flask import Flask
from flask_restx import Api

# Imports apis from api package
from src.api.health_check_api import ns_health_check
from src.api.screenshot_api import ns_screenshot



def create_app():
    app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
    app.url_map.strict_slashes = False
    api = Api(app, version='1.0', title='Website Screenshot Generator', prefix=f'/api/v1')


    # Register api
    api.add_namespace(ns_health_check)
    api.add_namespace(ns_screenshot)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)