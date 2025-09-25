from flask import Flask, request, jsonify
import pyotp

app = Flask(__name__)

@app.route('/api/generate-2fa', methods=['GET'])
def generate_2fa():
    secret_key = request.args.get('secret')

    if not secret_key:
        return jsonify({"error": "TOTP secret is required."}), 400

    try:
        totp = pyotp.TOTP(secret_key)
        code = totp.now()

        return jsonify({
            "c": code
        })
    except Exception as e:
        return jsonify({"error": f"Failed to generate code."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
