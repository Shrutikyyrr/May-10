from database import get_connection
from datetime import datetime

def log_action(action):
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO logs(action, timestamp)
        VALUES (?, ?)
    """, (
        action,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()