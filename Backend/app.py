import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Create SQLite Database
def init_db():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, message TEXT)''')
    conn.commit()
    conn.close()

init_db()  # Initialize database on startup

@app.route('/post', methods=['POST'])
def post_message():
    data = request.json
    message = data.get("message")

    if not message:
        return jsonify({"status": "error", "message": "Message cannot be empty"}), 400

    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (message) VALUES (?)", (message,))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": f"Posted: {message}"})

@app.route('/messages', methods=['GET'])
def get_messages():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    messages = cursor.fetchall()
    conn.close()

    return jsonify({"messages": [{"id": row[0], "message": row[1]} for row in messages]})

if __name__ == "__main__":
    app.run(debug=True)
