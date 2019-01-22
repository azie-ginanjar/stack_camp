from flask_jwt_extended import jwt_required
from flask_restplus import Resource


class TestResource(Resource):
    method_decorators = [jwt_required]

    def get(self):
        return {"test": "hanya test belaka"}
