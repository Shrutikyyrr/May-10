from flask import Blueprint, jsonify
from database import get_connection

log_bp = Blueprint("log_bp", __name__)

@log_bp.route("/logs", methods=["GET"])
def get_logs():

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        SELECT *
        FROM logs
        ORDER BY id DESC
    """)

    logs = [dict(row) for row in c.fetchall()]

    conn.close()

    return jsonify(logs)