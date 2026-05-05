import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("db.sqlite")
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = " + user_id
    return conn.execute(query).fetchone()

def login(username, password):
    # Hardcoded secret
    API_KEY = "sk_live_9876543210abcdef"
    return username == "admin" and password == "password"
