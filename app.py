from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# Your secret token from eBay Developer Portal (set one there and copy here)
VERIFICATION_TOKEN = "your-verification-token"
ENDPOINT_URL = "https://your-render-url.onrender.com"

@app.route("/", methods=["GET"])
def verify():
    # Handle the initial verification GET from eBay
    challenge_code = request.args.get("challenge_code", "")
    if not challenge_code:
        return "Missing challenge code", 400

    # Hash: challengeCode + verificationToken + endpoint
    to_hash = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
    hashed = hashlib.sha256(to_hash.encode("utf-8")).hexdigest()

    return jsonify({"challengeResponse": hashed})

@app.route("/", methods=["POST"])
def handle_notification():
    data = request.json
    print("Received notification:", data)
    # Here you could add logic to delete user data from your DB
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
