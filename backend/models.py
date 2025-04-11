from .db import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS specimens (
            id SERIAL PRIMARY KEY,
            username TEXT,
            microscope_size REAL,
            magnification REAL,
            actual_size REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_specimen(username, microscope_size, magnification, actual_size):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO specimens (username, microscope_size, magnification, actual_size)
        VALUES (%s, %s, %s, %s)
    ''', (username, microscope_size, magnification, actual_size))
    conn.commit()
    conn.close()
