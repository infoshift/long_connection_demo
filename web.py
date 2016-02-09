from gevent import monkey
monkey.patch_all()

from flask import Flask, jsonify
import gevent
import requests
import os


app = Flask(__name__)
API_URL = os.environ.get('API_URL', 'http://localhost:8000')


def heartbeater(s):
    while True:
        time.sleep(1)
        r = s.get(API_URL + '/heartbeat')
        print 'heartbeating... %s - %s' % (r.status_code, r.text)


@app.route('/')
def page_index():
    s = requests.Session()

    # Start the heartbeat thread.
    t = gevent.spawn(heartbeater, s)
    t.join()  # Start the fucking thread.

    # Simulates the long API request.
    r = s.get(API_URL + '/long_request')

    # Kill the heartbeat thread.
    t.kill()

    return jsonify({
        'status_code': r.status_code,
        'text_response': r.text,
    })
