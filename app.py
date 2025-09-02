

from flask import Flask, request, jsonify
import hashlib
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

app = Flask(__name__)

# Load sensitive values from .env
VERIFICATION_TOKEN = os.getenv("VERIFICATION_TOKEN")
ENDPOINT_URL = os.getenv("ENDPOINT_URL")

@app.route("/", methods=["GET"])
def verify():
    challenge_code = request.args.get("challenge_code", "")
    if not challenge_code:
        return "Missing challenge code", 400

    to_hash = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
    hashed = hashlib.sha256(to_hash.encode("utf-8")).hexdigest()

    return jsonify({"challengeResponse": hashed})

@app.route("/", methods=["POST"])
def handle_notification():
    data = request.json
    print("Received notification:", data)
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


