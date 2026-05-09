from database import get_connection

def add_member(data):
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO members(name,email)
        VALUES (?,?)
    """, (
        data["name"],
        data["email"]
    ))

    conn.commit()
    conn.close()


def get_members():
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM members")

    members = [dict(row) for row in c.fetchall()]

    conn.close()

    return members