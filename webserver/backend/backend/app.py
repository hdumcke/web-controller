import os
import sys
import threading
import time
from UDPComms import Publisher
from flask import Flask, send_from_directory
from backend.controller.controller import Controller


controller_pub = Publisher(8830,65530)
current = 'dance'
## Configurable ##
MESSAGE_RATE = 20
PORT = 8080

app = Flask(__name__)
controller = Controller(MESSAGE_RATE)


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory('./static/', path)


@app.route('/')
@app.route('/dance')
@app.route('/walk')
@app.route('/pupper')
def root():
    return send_from_directory("%s%s" % (os.path.dirname(__file__), '/static/'), 'index.html')


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory("%s%s" % (os.path.dirname(__file__), '/img/'), path)


@app.route("/pupper/<string:command>/<string:param>", methods=['GET'])
def pupper(command, param):
    gait = 'pupper'
    controller.setParams(gait, command, param)
    return controller.getParams(gait, command, param)


@app.route("/dance/<string:command>/<string:param>", methods=['GET'])
def dance(command, param):
    gait = 'dance'
    controller.setParams(gait, command, param)
    return controller.getParams(gait, command, param)


@app.route("/walk/<string:command>/<string:param>", methods=['GET'])
def walk(command, param):
    gait = 'walk'
    controller.setParams(gait, command, param)
    return controller.getParams(gait, command, param)


def runLoop():
    while True:

        #print(controller.getMsg(), file=sys.stdout)
        controller_pub.send(controller.getMsg())

        time.sleep(1 / MESSAGE_RATE)


def main():
    threading.Thread(target=runLoop, daemon=True).start()
    app.run(host='0.0.0.0', port=PORT)


if __name__ == "__main__":
    main()
