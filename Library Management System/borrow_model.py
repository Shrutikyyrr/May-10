from database import get_connection
from datetime import datetime

def borrow_book(member_id, book_id):

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        SELECT available
        FROM books
        WHERE id=?
    """, (book_id,))

    book = c.fetchone()

    if not book:
        return {"error": "Book not found"}

    if book["available"] <= 0:
        return {"error": "Book unavailable"}

    c.execute("""
        INSERT INTO borrow_records(
            member_id,
            book_id,
            borrow_date,
            status
        )
        VALUES (?, ?, ?, ?)
    """, (
        member_id,
        book_id,
        datetime.now().strftime("%Y-%m-%d"),
        "borrowed"
    ))

    c.execute("""
        UPDATE books
        SET available = available - 1
        WHERE id=?
    """, (book_id,))

    conn.commit()
    conn.close()

    return {"message": "Book borrowed"}


def return_book(record_id):

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        SELECT book_id
        FROM borrow_records
        WHERE id=? AND status='borrowed'
    """, (record_id,))

    record = c.fetchone()

    if not record:
        return {"error": "Record not found"}

    book_id = record["book_id"]

    c.execute("""
        UPDATE borrow_records
        SET status='returned',
            return_date=?
        WHERE id=?
    """, (
        datetime.now().strftime("%Y-%m-%d"),
        record_id
    ))

    c.execute("""
        UPDATE books
        SET available = available + 1
        WHERE id=?
    """, (book_id,))

    conn.commit()
    conn.close()

    return {"message": "Book returned"}