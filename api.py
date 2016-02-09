from flask import Flask, jsonify
import time


app = Flask(__name__)


@app.route('/heartbeat')
def api_hello():
    # responds quickly.
    return 'ok'


@app.route('/long_request')
def api_long_request():
    for _ in xrange(120):
        time.sleep(1)
        print 'sleeping... %s' % _
    return jsonify({'message': 'hello world'})
