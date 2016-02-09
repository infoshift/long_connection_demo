from flask import Flask, jsonify
import time


app = Flask(__name__)


@app.route('/heartbeat')
def api_hello():
    # responds quickly.
    return 'ok'


@app.route('/long_request')
def api_long_request():
    time.sleep(120)  # 2 minutes
    return jsonify({'message': 'hello world'})
