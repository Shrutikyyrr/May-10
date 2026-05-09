from flask import Blueprint, jsonify
from database import get_connection

analytics_bp = Blueprint("analytics_bp", __name__)

@analytics_bp.route("/analytics", methods=["GET"])
def analytics():

    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT COUNT(*) as total FROM books")
    total_books = c.fetchone()["total"]

    c.execute("SELECT COUNT(*) as total FROM members")
    total_members = c.fetchone()["total"]

    c.execute("""
        SELECT COUNT(*) as total
        FROM borrow_records
        WHERE status='borrowed'
    """)
    borrowed = c.fetchone()["total"]

    c.execute("""
        SELECT COUNT(*) as total
        FROM borrow_records
        WHERE status='returned'
    """)
    returned = c.fetchone()["total"]

    conn.close()

    return jsonify({
        "total_books": total_books,
        "total_members": total_members,
        "borrowed_books": borrowed,
        "returned_books": returned
    })