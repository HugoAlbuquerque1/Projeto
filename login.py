import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT user, senha FROM users WHERE user = ? AND senha = ?", (username, password))
    result = cursor.fetchone()

    conn.close()

    if result is not None:
        return True
    else:
        return False

