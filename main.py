from flask import Flask, request
from flask_restplus import reqparse, abort, Api, Resource
from flask_cors import CORS
import os
from apiv1 import blueprint as apiv1
from apiv2 import blueprint as apiv2

"""

Service listens on port 5000 (Flask Default Port)

"""

app = Flask(__name__)
api = Api(app=app)
# Api v1 - current features
app.register_blueprint(apiv1, url_prefix='/api/v1')
# Api v2 - future features
app.register_blueprint(apiv2, url_prefix='/api/v2')
CORS(app, resources={r"/*": {"origins": "*", "methods":["GET","POST"]}})


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)