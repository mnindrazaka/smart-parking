from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


parking = {
    "max": 6,
    "current": 0
}


def getRemains():
    return parking['max'] - parking['current']


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/max")
def max():
    return jsonify({"remains": parking['max']})


@app.route("/remains")
def remains():
    return jsonify({"remains": getRemains()})


@app.route("/enter")
def enter():
    if parking['current'] < parking['max']:
        parking['current'] += 1

    socketio.emit("update remains", {"count": getRemains()})
    return jsonify({"remains": getRemains()})


@app.route("/exit")
def exit():
    if parking['current'] > 0:
        parking['current'] -= 1

    socketio.emit("update remains", {"count": getRemains()})
    return jsonify({"remains": getRemains()})


@socketio.on('connect', namespace='/')
def sendData():
    emit("update remains", {"count": getRemains()})


app.run(host='0.0.0.0')
