# -*- coding:utf8 -*-
import logging
import os
from flask import Flask, jsonify, make_response
from flask import request
import settings
import django
from flask_cors import CORS

os.environ['DJANGO_SETTINGS_MODULE'] = 'app_data.settings'
django.setup()

app = Flask(__name__)
CORS(app)
logging.basicConfig(filename="./logs/%s.log" % settings.psm, level=logging.INFO)


@app.route('/bitrun/api/v1/get_images', methods=['POST'])
def get_images():
    from api_process import api_process
    data = request.json
    images = data.get("images")
    result = api_process.get_images(images)
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@app.route('/bitrun/api/v1/get_image/<image_type>', methods=['GET'])
def get_image_by_type(image_type):
    from api_process import api_process
    result = api_process.get_image_by_type(image_type)
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@app.route('/bitrun/api/v1/get_goods', methods=['GET'])
def get_goods():
    from api_process import api_process
    result = api_process.get_goods()
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@app.route('/bitrun/api/v1/story_happen', methods=['POST'])
def story_happen():
    from api_process import api_process
    data = request.json
    result = api_process.story_happen(**data)
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@app.route('/bitrun/api/v1/get_monkey_status/<address>', methods=['GET'])
def get_monkey_status(address):
    from api_process import api_process
    result = api_process.get_monkey_status(address)
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@app.route('/bitrun/api/v1/go_home/<address>', methods=['GET'])
def go_home(address):
    """
    go home
    :param address:
    :return:
    """
    from api_process import api_process
    result = api_process.go_home(address)
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


def run_server():
    app.run(debug=True, port=8888, host='0.0.0.0')
