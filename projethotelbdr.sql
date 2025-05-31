-- Create database
CREATE DATABASE hotel_management;
USE hotel_management;
-- Table: Chambre
CREATE TABLE Chambre (
    Etage INT,
    Surface DECIMAL(8,2),
    id_Chambre INT PRIMARY KEY
);

-- Table: Type_Chambre
CREATE TABLE Type_Chambre (
    Type VARCHAR(255),
    Tarif DECIMAL(10,2),
    id_Type INT PRIMARY KEY
);

-- Table: Hotel
CREATE TABLE Hotel (
    Ville VARCHAR(255),
    Pays VARCHAR(255),
    Code_postal VARCHAR(10),
    id_Hotel INT PRIMARY KEY
);

-- Table: Prestation
CREATE TABLE Prestation (
    Prix DECIMAL(10,2),
    id_Prestation INT PRIMARY KEY
);

-- Table: Client
CREATE TABLE Client (
    Adresse VARCHAR(255),
    Ville VARCHAR(255),
    Code_postal VARCHAR(10),
    E_mail VARCHAR(255),
    Numero_de_telephone VARCHAR(20),
    Nom_complet VARCHAR(255) PRIMARY KEY
);

-- Table: Evaluation
CREATE TABLE Evaluation (
    Date_arrivee DATE,
    La_note DECIMAL(3,2),
    Texte_descriptif TEXT,
    id_Evaluation INT PRIMARY KEY
);

-- Table: Reservation
CREATE TABLE Reservation (
    Date_arrivee DATE,
    Date_de_depart DATE,
    id_Reservation INT PRIMARY KEY
);

-- Add foreign key constraints

-- Chambre belongs to Type_Chambre (Etre_de relationship)
ALTER TABLE Chambre 
ADD COLUMN id_Type INT,
ADD FOREIGN KEY (id_Type) REFERENCES Type_Chambre(id_Type);

-- Chambre belongs to Hotel (Contient relationship)
ALTER TABLE Chambre 
ADD COLUMN id_Hotel INT,
ADD FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel);

-- Prestation offered by Hotel (Offre relationship)
ALTER TABLE Prestation 
ADD COLUMN id_Hotel INT,
ADD FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel);

-- Reservation made by Client (Effectuer relationship)
ALTER TABLE Reservation 
ADD COLUMN Nom_complet VARCHAR(255),
ADD FOREIGN KEY (Nom_complet) REFERENCES Client(Nom_complet);

-- Reservation concerns Chambre (Concerner relationship)
ALTER TABLE Reservation 
ADD COLUMN id_Chambre INT,
ADD FOREIGN KEY (id_Chambre) REFERENCES Chambre(id_Chambre);

-- Evaluation provided by Client (Fournir relationship)
ALTER TABLE Evaluation 
ADD COLUMN Nom_complet VARCHAR(255),
ADD FOREIGN KEY (Nom_complet) REFERENCES Client(Nom_complet);

-- Evaluation evaluates Hotel (Evaluer relationship)
ALTER TABLE Evaluation 
ADD COLUMN id_Hotel INT,
ADD FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel);