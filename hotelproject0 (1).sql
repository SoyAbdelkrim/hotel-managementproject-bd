-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: hotel_management
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chambre`
--

DROP TABLE IF EXISTS chambre;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE chambre (
  Etage int DEFAULT NULL,
  Surface decimal(8,2) DEFAULT NULL,
  id_Chambre int NOT NULL,
  id_Type int DEFAULT NULL,
  id_Hotel int DEFAULT NULL,
  PRIMARY KEY (id_Chambre),
  KEY id_Type (id_Type),
  KEY id_Hotel (id_Hotel),
  CONSTRAINT chambre_ibfk_1 FOREIGN KEY (id_Type) REFERENCES type_chambre (id_Type),
  CONSTRAINT chambre_ibfk_2 FOREIGN KEY (id_Hotel) REFERENCES hotel (id_Hotel)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chambre`
--

LOCK TABLES chambre WRITE;
/*!40000 ALTER TABLE chambre DISABLE KEYS */;
INSERT INTO chambre VALUES (2,201.00,1,1,1),(5,502.00,2,2,1),(3,305.00,3,1,2),(4,410.00,4,2,2),(1,104.00,5,2,2),(2,202.00,6,1,1),(3,307.00,7,2,1),(1,101.00,8,1,1);
/*!40000 ALTER TABLE chambre ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS client;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  Adresse varchar(255) DEFAULT NULL,
  Ville varchar(255) DEFAULT NULL,
  Code_postal varchar(10) DEFAULT NULL,
  E_mail varchar(255) DEFAULT NULL,
  Numero_de_telephone varchar(20) DEFAULT NULL,
  Nom_complet varchar(255) NOT NULL,
  PRIMARY KEY (Nom_complet)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES client WRITE;
/*!40000 ALTER TABLE client DISABLE KEYS */;
INSERT INTO client VALUES ('3 Rue des Fleurs','Nice','06000','emma.giraud@email.fr','0656789012','Emma Giraud'),('12 Rue de Paris','Paris','75001','jean.dupont@email.fr','0612345678','Jean Dupont'),('27 Rue Nationale','Lille','59800','lucie.martin@email.fr','0645678901','Lucie Martin'),('5 Avenue Victor Hugo','Lyon','69002','marie.leroy@email.fr','0623456789','Marie Leroy'),('8 Boulevard Saint-Michel','Marseille','13005','paul.moreau@email.fr','0634567890','Paul Moreau');
/*!40000 ALTER TABLE client ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation`
--

DROP TABLE IF EXISTS evaluation;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE evaluation (
  Date_arrivee date DEFAULT NULL,
  La_note decimal(3,2) DEFAULT NULL,
  Texte_descriptif text,
  id_Evaluation int NOT NULL,
  Nom_complet varchar(255) DEFAULT NULL,
  id_Hotel int DEFAULT NULL,
  PRIMARY KEY (id_Evaluation),
  KEY Nom_complet (Nom_complet),
  KEY id_Hotel (id_Hotel),
  CONSTRAINT evaluation_ibfk_1 FOREIGN KEY (Nom_complet) REFERENCES `client` (Nom_complet),
  CONSTRAINT evaluation_ibfk_2 FOREIGN KEY (id_Hotel) REFERENCES hotel (id_Hotel)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation`
--

LOCK TABLES evaluation WRITE;
/*!40000 ALTER TABLE evaluation DISABLE KEYS */;
INSERT INTO evaluation VALUES ('2025-06-15',5.00,'Excellent séjour, personnel très accueillant.',1,'Jean Dupont',1),('2025-07-01',4.00,'Chambre propre, bon rapport qualité/prix.',2,'Marie Leroy',2),('2025-08-10',3.00,'Séjour correct mais bruyant la nuit.',3,'Paul Moreau',1),('2025-09-05',5.00,'Service impeccable, je recommande.',4,'Lucie Martin',2),('2025-09-20',4.00,'Très bon petit-déjeuner, hôtel bien situé.',5,'Emma Giraud',1);
/*!40000 ALTER TABLE evaluation ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel`
--

DROP TABLE IF EXISTS hotel;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE hotel (
  Ville varchar(255) DEFAULT NULL,
  Pays varchar(255) DEFAULT NULL,
  Code_postal varchar(10) DEFAULT NULL,
  id_Hotel int NOT NULL,
  PRIMARY KEY (id_Hotel)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel`
--

LOCK TABLES hotel WRITE;
/*!40000 ALTER TABLE hotel DISABLE KEYS */;
INSERT INTO hotel VALUES ('Paris','France','75001',1),('Lyon','France','69002',2);
/*!40000 ALTER TABLE hotel ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestation`
--

DROP TABLE IF EXISTS prestation;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE prestation (
  Prix decimal(10,2) DEFAULT NULL,
  id_Prestation int NOT NULL,
  id_Hotel int DEFAULT NULL,
  PRIMARY KEY (id_Prestation),
  KEY id_Hotel (id_Hotel),
  CONSTRAINT prestation_ibfk_1 FOREIGN KEY (id_Hotel) REFERENCES hotel (id_Hotel)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestation`
--

LOCK TABLES prestation WRITE;
/*!40000 ALTER TABLE prestation DISABLE KEYS */;
INSERT INTO prestation VALUES (15.00,1,1),(30.00,2,1),(0.00,3,1),(50.00,4,1),(20.00,5,1);
/*!40000 ALTER TABLE prestation ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS reservation;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE reservation (
  Date_arrivee date DEFAULT NULL,
  Date_de_depart date DEFAULT NULL,
  id_Reservation int NOT NULL,
  Nom_complet varchar(255) DEFAULT NULL,
  id_Chambre int DEFAULT NULL,
  PRIMARY KEY (id_Reservation),
  KEY Nom_complet (Nom_complet),
  KEY id_Chambre (id_Chambre),
  CONSTRAINT reservation_ibfk_1 FOREIGN KEY (Nom_complet) REFERENCES `client` (Nom_complet),
  CONSTRAINT reservation_ibfk_2 FOREIGN KEY (id_Chambre) REFERENCES chambre (id_Chambre)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES reservation WRITE;
/*!40000 ALTER TABLE reservation DISABLE KEYS */;
INSERT INTO reservation VALUES ('2025-06-15','2025-06-18',1,'Jean Dupont',1),('2025-07-01','2025-07-05',2,'Marie Leroy',2),('2025-08-10','2025-08-14',3,'Paul Moreau',3),('2025-09-05','2025-09-07',4,'Lucie Martin',4),('2025-09-20','2025-09-25',5,'Emma Giraud',5),('2025-11-12','2025-11-14',7,'Marie Leroy',2),('2026-01-15','2026-01-18',9,'Lucie Martin',4),('2026-02-01','2026-02-05',10,'Marie Leroy',2);
/*!40000 ALTER TABLE reservation ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_chambre`
--

DROP TABLE IF EXISTS type_chambre;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE type_chambre (
  `Type` varchar(255) DEFAULT NULL,
  Tarif decimal(10,2) DEFAULT NULL,
  id_Type int NOT NULL,
  PRIMARY KEY (id_Type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_chambre`
--

LOCK TABLES type_chambre WRITE;
/*!40000 ALTER TABLE type_chambre DISABLE KEYS */;
INSERT INTO type_chambre VALUES ('Simple',80.00,1),('Double',120.00,2);
/*!40000 ALTER TABLE type_chambre ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-30 22:38:12
