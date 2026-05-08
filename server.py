from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='.')

data_live = [
    {"user": "acc1", "current": 77, "total": 50, "status": "xong"},
    {"user": "acc2", "current": 538, "total": 600, "status": "dang_chay"},
    {"user": "acc3", "current": 0, "total": 800, "status": "cho"}
]

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

@app.route("/data")
def data():
    return jsonify(data_live)

app.run(host="0.0.0.0", port=10000)