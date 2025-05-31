import sqlite3

def connect_db():
    conn = sqlite3.connect("hotel.db")
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chambre (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT NOT NULL,
            type TEXT NOT NULL,
            prix REAL NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_client TEXT NOT NULL,
            date_reservation DATE NOT NULL,
            duree INTEGER NOT NULL,
            chambre_id INTEGER,
            FOREIGN KEY(chambre_id) REFERENCES chambre(id)
        )
    """)
    
    conn.commit()
    conn.close()

def ajouter_reservation(nom_client, date_reservation, duree, chambre_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservation (nom_client, date_reservation, duree, chambre_id)
        VALUES (?, ?, ?, ?)
    """, (nom_client, date_reservation, duree, chambre_id))
    conn.commit()
    conn.close()

def get_reservations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.id, r.nom_client, r.date_reservation, r.duree, c.numero
        FROM reservation r
        JOIN chambre c ON r.chambre_id = c.id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_chambres():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, numero FROM chambre")
    chambres = cursor.fetchall()
    conn.close()
    return chambres
