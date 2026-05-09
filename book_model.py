from database import get_connection

def add_book(data):
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO books(title, author, isbn, quantity, available)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["title"],
        data["author"],
        data["isbn"],
        data["quantity"],
        data["quantity"]
    ))

    conn.commit()
    conn.close()


def get_books():
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM books")
    books = [dict(row) for row in c.fetchall()]

    conn.close()

    return books


def delete_book(book_id):
    conn = get_connection()
    c = conn.cursor()

    c.execute("DELETE FROM books WHERE id=?", (book_id,))

    conn.commit()
    conn.close()