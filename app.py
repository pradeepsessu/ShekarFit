from flask import Flask, request, jsonify, render_template
import razorpay
import hmac
import hashlib

app = Flask(__name__)

# Razorpay Keys (use test keys from dashboard first)
RAZORPAY_KEY_ID = "rzp_live_RFxFX92QUtd5vl"
RAZORPAY_SECRET = "WF30is0BdLQpz1iAwjH8xTN4"

# Razorpay client
razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET))


# ------------------------
# Home Page (Serve HTML)
# ------------------------
@app.route("/")
def home():
    return render_template("index.html", key_id=RAZORPAY_KEY_ID)


# ------------------------
# Create Order API
# ------------------------
@app.route("/create_order", methods=["POST"])
def create_order():
    data = request.json
    try:
        # Ensure amount is integer
        amount = int(data.get("amount")) * 100  # INR → paise
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid amount"}), 400

    order = razorpay_client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1
    })
    return jsonify(order)



# ------------------------
# Verify Payment API
# ------------------------
@app.route("/verify_payment", methods=["POST"])
def verify_payment():
    data = request.json
    razorpay_order_id = data.get("razorpay_order_id")
    razorpay_payment_id = data.get("razorpay_payment_id")
    razorpay_signature = data.get("razorpay_signature")

    generated_signature = hmac.new(
        RAZORPAY_SECRET.encode(),
        f"{razorpay_order_id}|{razorpay_payment_id}".encode(),
        hashlib.sha256
    ).hexdigest()

    if generated_signature == razorpay_signature:
        return jsonify({"status": "success", "payment_id": razorpay_payment_id})
    else:
        return jsonify({"status": "failed", "reason": "Signature mismatch"}), 400


if __name__ == "__main__":
    app.run(debug=True)
