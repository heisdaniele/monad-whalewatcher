import eventlet
eventlet.monkey_patch()

from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# In-memory storage for received transactions.
transactions = []

@app.route('/')
def index():
    # Render the main page (index.html) from the templates folder.
    return render_template('index.html')

@app.route('/api/transactions', methods=['POST'])
def api_transactions():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Append a timestamp to the transaction.
    data['received_at'] = datetime.utcnow().isoformat()
    transactions.append(data)
    # Emit a Socket.IO event to all connected clients.
    socketio.emit('new_transaction', data)
    return jsonify({"status": "success"}), 200

@app.route('/api/get_transactions', methods=['GET'])
def get_transactions():
    return jsonify(transactions)

if __name__ == '__main__':
    # Run the Flask server on port 5000.
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
