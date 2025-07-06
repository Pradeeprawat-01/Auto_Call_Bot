from flask import Flask, request, jsonify, send_from_directory
from twilio.rest import Client
import os

app = Flask(__name__, static_folder='static')

# Allow loading static HTML directly
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# Replace with your credentials
account_sid = 'your twilio sid account no.'
auth_token = 'your twilio sid account token'
from_number = 'your twilio  no'

client = Client(account_sid, auth_token)

@app.route('/make-call', methods=['POST'])
def make_call():
    data = request.get_json()
    to_number = data.get('number')

    try:
        call = client.calls.create(
            twiml='<Response><Say>Hey! This is a test call from Python. Have a great day!</Say></Response>',
            to=to_number,
            from_=from_number
        )
        return jsonify({'success': True, 'sid': call.sid})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
