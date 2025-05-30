import sqlite3
import pandas as pd
from datetime import datetime

class HotelDatabase:
    def __init__(self, db_path='hotel.db'):
        self.db_path = db_path
        self.create_tables()
        self.populate_initial_data()
    
    def get_connection(self):
        """Créer une connexion à la base de données"""
        return sqlite3.connect(self.db_path)
    
    def create_tables(self):
        """Créer toutes les tables de la base de données"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Table Hotel
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Hotel (
                id_hotel INTEGER PRIMARY KEY,
                ville TEXT NOT NULL,
                pays TEXT NOT NULL,
                code_postal TEXT
            )
        ''')
        
        # Table Client
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Client (
                id_client INTEGER PRIMARY KEY,
                adresse TEXT,
                ville TEXT,
                code_postal TEXT,
                email TEXT UNIQUE,
                telephone TEXT,
                nom TEXT NOT NULL
            )
        ''')
        
        # Table Prestation
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Prestation (
                id_prestation INTEGER PRIMARY KEY,
                prix REAL,
                nom TEXT NOT NULL
            )
        ''')
        
        # Table TypeChambre
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TypeChambre (
                id_type INTEGER PRIMARY KEY,
                nom TEXT NOT NULL,
                prix REAL NOT NULL
            )
        ''')
        
        # Table Chambre
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Chambre (
                id_chambre INTEGER PRIMARY KEY,
                numero INTEGER NOT NULL,
                nb_personnes INTEGER,
                balcon BOOLEAN,
                id_hotel INTEGER,
                id_type INTEGER,
                FOREIGN KEY (id_hotel) REFERENCES Hotel(id_hotel),
                FOREIGN KEY (id_type) REFERENCES TypeChambre(id_type)
            )
        ''')
        
        # Table Reservation
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Reservation (
                id_reservation INTEGER PRIMARY KEY,
                date_debut DATE NOT NULL,
                date_fin DATE NOT NULL,
                id_client INTEGER,
                FOREIGN KEY (id_client) REFERENCES Client(id_client)
            )
        ''')
        
        # Table Evaluation
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Evaluation (
                id_evaluation INTEGER PRIMARY KEY,
                date_evaluation DATE,
                note INTEGER CHECK(note >= 1 AND note <= 5),
                commentaire TEXT,
                id_client INTEGER,
                FOREIGN KEY (id_client) REFERENCES Client(id_client)
            )
        ''')
        
        # Table de liaison Reservation_Chambre
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Reservation_Chambre (
                id_reservation INTEGER,
                id_chambre INTEGER,
                PRIMARY KEY (id_reservation, id_chambre),
                FOREIGN KEY (id_reservation) REFERENCES Reservation(id_reservation),
                FOREIGN KEY (id_chambre) REFERENCES Chambre(id_chambre)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def populate_initial_data(self):
        """Peupler la base avec les données initiales"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Vérifier si les données existent déjà
        cursor.execute("SELECT COUNT(*) FROM Hotel")
        if cursor.fetchone()[0] > 0:
            conn.close()
            return
        
        # Données Hotel
        hotels = [
            (1, 'Paris', 'France', '75001'),
            (2, 'Lyon', 'France', '69002')
        ]
        cursor.executemany("INSERT INTO Hotel VALUES (?, ?, ?, ?)", hotels)
        
        # Données Client
        clients = [
            (1, '12 Rue de Paris', 'Paris', '75001', 'jean.dupont@email.fr', '0612345678', 'Jean Dupont'),
            (2, '5 Avenue Victor Hugo', 'Lyon', '69002', 'marie.leroy@email.fr', '0623456789', 'Marie Leroy'),
            (3, '8 Boulevard Saint-Michel', 'Marseille', '13005', 'paul.moreau@email.fr', '0634567890', 'Paul Moreau'),
            (4, '27 Rue Nationale', 'Lille', '59800', 'lucie.martin@email.fr', '0645678901', 'Lucie Martin'),
            (5, '3 Rue des Fleurs', 'Nice', '06000', 'emma.giraud@email.fr', '0656789012', 'Emma Giraud')
        ]
        cursor.executemany("INSERT INTO Client VALUES (?, ?, ?, ?, ?, ?, ?)", clients)
        
        # Données Prestation
        prestations = [
            (1, 15, 'Petit-déjeuner'),
            (2, 30, 'Navette aéroport'),
            (3, 0, 'Wi-Fi gratuit'),
            (4, 50, 'Spa et bien-être'),
            (5, 20, 'Parking sécurisé')
        ]
        cursor.executemany("INSERT INTO Prestation VALUES (?, ?, ?)", prestations)
        
        # Données TypeChambre
        types_chambre = [
            (1, 'Simple', 80),
            (2, 'Double', 120)
        ]
        cursor.executemany("INSERT INTO TypeChambre VALUES (?, ?, ?)", types_chambre)
        
        # Données Chambre
        chambres = [
            (1, 201, 2, 0, 1, 1),
            (2, 502, 5, 1, 1, 2),
            (3, 305, 3, 0, 2, 1),
            (4, 410, 4, 0, 2, 2),
            (5, 104, 1, 1, 2, 2),
            (6, 202, 2, 0, 1, 1),
            (7, 307, 3, 1, 1, 2),
            (8, 101, 1, 0, 1, 1)
        ]
        cursor.executemany("INSERT INTO Chambre VALUES (?, ?, ?, ?, ?, ?)", chambres)
        
        # Données Reservation
        reservations = [
            (1, '2025-06-15', '2025-06-18', 1),
            (2, '2025-07-01', '2025-07-05', 2),
            (3, '2025-08-10', '2025-08-14', 3),
            (4, '2025-09-05', '2025-09-07', 4),
            (5, '2025-09-20', '2025-09-25', 5),
            (7, '2025-11-12', '2025-11-14', 2),
            (9, '2026-01-15', '2026-01-18', 4),
            (10, '2026-02-01', '2026-02-05', 2)
        ]
        cursor.executemany("INSERT INTO Reservation VALUES (?, ?, ?, ?)", reservations)
        
        # Liaison Reservation-Chambre (assignation simple pour l'exemple)
        reservations_chambres = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (7, 6), (9, 7), (10, 8)
        ]
        cursor.executemany("INSERT INTO Reservation_Chambre VALUES (?, ?)", reservations_chambres)
        
        # Données Evaluation
        evaluations = [
            (1, '2025-06-15', 5, 'Excellent séjour, personnel très accueillant.', 1),
            (2, '2025-07-01', 4, 'Chambre propre, bon rapport qualité/prix.', 2),
            (3, '2025-08-10', 3, 'Séjour correct mais bruyant la nuit.', 3),
            (4, '2025-09-05', 5, 'Service impeccable, je recommande.', 4),
            (5, '2025-09-20', 4, 'Très bon petit-déjeuner, hôtel bien situé.', 5)
        ]
        cursor.executemany("INSERT INTO Evaluation VALUES (?, ?, ?, ?, ?)", evaluations)
        
        conn.commit()
        conn.close()
    
    def get_reservations(self):
        """Récupérer la liste des réservations avec détails"""
        conn = self.get_connection()
        query = '''
            SELECT 
                r.id_reservation,
                r.date_debut,
                r.date_fin,
                c.nom AS client_nom,
                c.email,
                h.ville AS hotel_ville,
                h.pays AS hotel_pays,
                ch.numero AS chambre_numero,
                tc.nom AS type_chambre
            FROM Reservation r
            JOIN Client c ON r.id_client = c.id_client
            JOIN Reservation_Chambre rc ON r.id_reservation = rc.id_reservation
            JOIN Chambre ch ON rc.id_chambre = ch.id_chambre
            JOIN Hotel h ON ch.id_hotel = h.id_hotel
            JOIN TypeChambre tc ON ch.id_type = tc.id_type
            ORDER BY r.date_debut DESC
        '''
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    
    def get_clients(self):
        """Récupérer la liste des clients"""
        conn = self.get_connection()
        query = "SELECT * FROM Client ORDER BY nom"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    
    def get_available_rooms(self, date_debut, date_fin):
        """Récupérer les chambres disponibles pour une période"""
        conn = self.get_connection()
        query = '''
            SELECT 
                ch.id_chambre,
                ch.numero,
                ch.nb_personnes,
                CASE WHEN ch.balcon THEN 'Oui' ELSE 'Non' END as balcon,
                h.ville AS hotel_ville,
                tc.nom AS type_chambre,
                tc.prix
            FROM Chambre ch
            JOIN Hotel h ON ch.id_hotel = h.id_hotel
            JOIN TypeChambre tc ON ch.id_type = tc.id_type
            WHERE ch.id_chambre NOT IN (
                SELECT rc.id_chambre
                FROM Reservation_Chambre rc
                JOIN Reservation r ON rc.id_reservation = r.id_reservation
                WHERE (r.date_debut <= ? AND r.date_fin >= ?)
                   OR (r.date_debut <= ? AND r.date_fin >= ?)
                   OR (r.date_debut >= ? AND r.date_fin <= ?)
            )
            ORDER BY h.ville, tc.nom, ch.numero
        '''
        df = pd.read_sql_query(query, conn, params=[date_fin, date_debut, date_debut, date_debut, date_debut, date_fin])
        conn.close()
        return df
    
    def add_client(self, nom, email, telephone, adresse, ville, code_postal):
        """Ajouter un nouveau client"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Client (nom, email, telephone, adresse, ville, code_postal)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (nom, email, telephone, adresse, ville, code_postal))
            conn.commit()
            return True, "Client ajouté avec succès"
        except sqlite3.IntegrityError:
            return False, "Erreur: Email déjà existant"
        except Exception as e:
            return False, f"Erreur: {str(e)}"
        finally:
            conn.close()
    
    def add_reservation(self, date_debut, date_fin, id_client, id_chambre):
        """Ajouter une nouvelle réservation"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            # Vérifier la disponibilité de la chambre
            cursor.execute('''
                SELECT COUNT(*) FROM Reservation_Chambre rc
                JOIN Reservation r ON rc.id_reservation = r.id_reservation
                WHERE rc.id_chambre = ?
                AND ((r.date_debut <= ? AND r.date_fin >= ?)
                OR (r.date_debut <= ? AND r.date_fin >= ?)
                OR (r.date_debut >= ? AND r.date_fin <= ?))
            ''', (id_chambre, date_fin, date_debut, date_debut, date_debut, date_debut, date_fin))
            
            if cursor.fetchone()[0] > 0:
                return False, "Chambre non disponible pour cette période"
            
            # Ajouter la réservation
            cursor.execute('''
                INSERT INTO Reservation (date_debut, date_fin, id_client)
                VALUES (?, ?, ?)
            ''', (date_debut, date_fin, id_client))
            
            id_reservation = cursor.lastrowid
            
            # Lier la réservation à la chambre
            cursor.execute('''
                INSERT INTO Reservation_Chambre (id_reservation, id_chambre)
                VALUES (?, ?)
            ''', (id_reservation, id_chambre))
            
            conn.commit()
            return True, "Réservation ajoutée avec succès"
        except Exception as e:
            return False, f"Erreur: {str(e)}"
        finally:
            conn.close()
    
    def get_client_by_id(self, id_client):
        """Récupérer un client par son ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nom FROM Client WHERE id_client = ?", (id_client,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
