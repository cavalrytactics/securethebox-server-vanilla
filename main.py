from flask import Flask, request
from flask_restplus import reqparse, abort, Api, Resource
from flask_cors import CORS, cross_origin
import os
from apiv1 import blueprint as apiv1
from apiv2 import blueprint as apiv2
from flask_talisman import Talisman
from flask_seasurf import SeaSurf

"""

Service listens on port 5000 (Flask Default Port)

"""

app = Flask(__name__)
api = Api(app=app)
# Api v1 - current features
api_v1 = app.register_blueprint(apiv1, url_prefix='/api/v1')
# Api v2 - future features
api_v2 = app.register_blueprint(apiv2, url_prefix='/api/v2')
CORS(app, resources={r"/*": {"origins": "*", "methods":["GET","POST"]}})
# CORS(api_v1, resources={r"/*": {"origins": "*", "methods":["GET","POST"]}}, send_wildcard=True)
# CORS(api_v2, resources={r"/*": {"origins": "*", "methods":["GET","POST"]}}, send_wildcard=True)

# SELF = "'self'"
# talisman = Talisman(
#     app,
#     content_security_policy={
#         'default-src': [
#                 '\'self\'',
#                 '*.securethebox.',
#                 'securethebox.',
#             ],
#     },
#     referrer_policy='no-referrer-when-downgrade'
#     content_security_policy_nonce_in=['script-src'],
#     feature_policy={
#         'geolocation': '\'none\'',
#     }
# )
# app.secret_key = '123abcakdjfa3abcakdjfakdjfaabcakdjfakdjfa'
# SeaSurf(app)

if __name__ == '__main__':
    # Look for environment variable APPENV
        app.run(host='0.0.0.0', debug=True)