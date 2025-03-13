
from flask import Blueprint, jsonify
from app.db import get_db_connection

message_routes = Blueprint('message_routes', __name__)

@message_routes.route('/message/<int:message_id>', methods=['GET'])
def get_message(message_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, content FROM messages WHERE id = %s;', (message_id,))
    message = cur.fetchone()
    cur.close()
    conn.close()
    
    if message:
        return jsonify({"id": message[0], "content": message[1]})
    else:
        return jsonify({"error": "Message not found"}), 404

@message_routes.route('/message/random', methods=['GET'])
def get_random_message():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, content FROM messages ORDER BY RANDOM() LIMIT 1;')
    message = cur.fetchone()
    cur.close()
    conn.close()
    
    if message:
        return jsonify({"id": message[0], "content": message[1]})
    else:
        return jsonify({"error": "No messages found"}), 404
