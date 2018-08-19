from flask import Flask, jsonify


app = Flask(__name__)


parkir = {
    "jumlah_total": 6,
    "jumlah_sekarang": 0
}


def get_sisa():
    return parkir['jumlah_total'] - parkir['jumlah_sekarang']


@app.route("/total")
def total():
    return jsonify({"total": parkir['jumlah_total']})


@app.route("/sisa")
def sisa():
    return jsonify({"sisa": get_sisa()})


@app.route("/masuk")
def masuk():
    if parkir['jumlah_sekarang'] < parkir['jumlah_total']:
        parkir['jumlah_sekarang'] += 1
    return jsonify({"sisa": get_sisa()})


@app.route("/keluar")
def keluar():
    if parkir['jumlah_sekarang'] > 0:
        parkir['jumlah_sekarang'] -= 1
    return jsonify({"sisa": get_sisa()})


app.run()
