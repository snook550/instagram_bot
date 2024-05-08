from flask import Flask, request, jsonify
from flask_cors import CORS
from config import VERIFY_TOKEN  # Import the verify token from config.py

app = Flask(__name__)
CORS(app)


@app.route("/bot-receiver", methods=["GET", "POST"])
def handle_webhook():
    if request.method == "GET":
        # Verification request from Instagram
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if verify_token == VERIFY_TOKEN:
            return challenge
        return "Verification token mismatch", 403
    elif request.method == "POST":
        # Handle the incoming webhook data
        data = request.json
        print("Received data:", data)
        return jsonify(success=True), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
