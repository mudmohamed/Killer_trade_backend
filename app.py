from flask import Flask, jsonify, request
app = Flask(__name__)

status = "Offline"
balance = 0.0
trades = []

@app.route("/")
def home():
    return "Killer Trade Robot API"

@app.route("/api/start", methods=["POST"])
def start_trading():
    global status
    status = "Online"
    return jsonify({"message": "Trading started"}), 200

@app.route("/api/stop", methods=["POST"])
def stop_trading():
    global status
    status = "Offline"
    return jsonify({"message": "Trading stopped"}), 200

@app.route("/api/status")
def get_status():
    return jsonify({"status": status})

@app.route("/api/balance")
def get_balance():
    return jsonify({"balance": balance})

@app.route("/api/trades")
def get_trades():
    return jsonify(trades)
