from flask import Blueprint
from flask_restplus import Api, Resource

from app_routes.namespace_academy import api as ns1

blueprint = Blueprint('apiv3', __name__)

api = Api(blueprint)
api.add_namespace(ns1)

# GRPC