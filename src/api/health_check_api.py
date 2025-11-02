from flask_restx import Namespace, Resource

ns_health_check = Namespace('health-check',description='Health Check')


@ns_health_check.route('/')
class HealthCheck(Resource):
    def get(self):
        return {'message': 'Healthy Server'}, 200