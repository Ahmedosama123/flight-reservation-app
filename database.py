

import sqlite3

def connect():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert(name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservations VALUES (NULL,?,?,?,?,?,?)",
                   (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def view_all():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update(id, name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE reservations SET 
        name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
        WHERE id=?
    """, (name, flight_number, departure, destination, date, seat_number, id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id=?", (id,))
    conn.commit()
    conn.close()
