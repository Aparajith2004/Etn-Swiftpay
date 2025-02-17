from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

@app.route('/api/pay', methods=['POST'])
def process_payment():
    data = request.json
    amount = data.get('amount')
    wallet_address = data.get('walletAddress')

    if not amount or not wallet_address:
        return jsonify({'message': 'Invalid payment details'}), 400

    # Simulate transaction success (Replace with actual ETN API call)
    tx_hash = "dummy-tx-hash-123456"
    
    return jsonify({'txHash': tx_hash})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
