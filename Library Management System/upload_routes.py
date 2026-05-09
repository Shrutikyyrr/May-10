from flask import Blueprint, request, jsonify
import pandas as pd
from database import get_connection
from models.log_model import log_action

upload_bp = Blueprint("upload_bp", __name__)

@upload_bp.route("/upload-books", methods=["POST"])
def upload_books():

    file = request.files["file"]

    df = pd.read_csv(file)

    conn = get_connection()
    c = conn.cursor()

    inserted = 0

    for _, row in df.iterrows():

        try:
            c.execute("""
                INSERT INTO books(
                    title,
                    author,
                    isbn,
                    quantity,
                    available
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                row["title"],
                row["author"],
                row["isbn"],
                row["quantity"],
                row["quantity"]
            ))

            inserted += 1

        except:
            continue

    conn.commit()
    conn.close()

    log_action(f"CSV Upload Added {inserted} books")

    return jsonify({
        "message": "CSV uploaded",
        "books_added": inserted
    })