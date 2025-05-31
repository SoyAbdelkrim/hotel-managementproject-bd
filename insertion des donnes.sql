INSERT INTO Hotel (id_Hotel, Ville, Pays, Code_postal) VALUES
(1, 'Paris', 'France', '75001'),
(2, 'Lyon', 'France', '69002');

INSERT INTO Client (Nom_complet, Adresse, Ville, Code_postal, E_mail, Numero_de_telephone) VALUES
('Jean Dupont', '12 Rue de Paris', 'Paris', '75001', 'jean.dupont@email.fr', '0612345678'),
('Marie Leroy', '5 Avenue Victor Hugo', 'Lyon', '69002', 'marie.leroy@email.fr', '0623456789'),
('Paul Moreau', '8 Boulevard Saint-Michel', 'Marseille', '13005', 'paul.moreau@email.fr', '0634567890'),
('Lucie Martin', '27 Rue Nationale', 'Lille', '59800', 'lucie.martin@email.fr', '0645678901'),
('Emma Giraud', '3 Rue des Fleurs', 'Nice', '06000', 'emma.giraud@email.fr', '0656789012');

INSERT INTO Prestation (id_Prestation, Prix, id_Hotel) VALUES
(1, 15, 1),
(2, 30, 1),
(3, 0, 1),
(4, 50, 1),
(5, 20, 1);

INSERT INTO Type_Chambre (id_Type, Type, Tarif) VALUES
(1, 'Simple', 80),
(2, 'Double', 120);

INSERT INTO Chambre (id_Chambre, Etage, Surface, id_Hotel, id_Type) VALUES
(1, 2, 201, 1, 1),
(2, 5, 502, 1, 2),
(3, 3, 305, 2, 1),
(4, 4, 410, 2, 2),
(5, 1, 104, 2, 2),
(6, 2, 202, 1, 1),
(7, 3, 307, 1, 2),
(8, 1, 101, 1, 1);

INSERT INTO Reservation (id_Reservation, Date_arrivee, Date_de_depart, Nom_complet, id_Chambre) VALUES
(1, '2025-06-15', '2025-06-18', 'Jean Dupont', 1),
(2, '2025-07-01', '2025-07-05', 'Marie Leroy', 2),
(7, '2025-11-12', '2025-11-14', 'Marie Leroy', 2),
(10, '2026-02-01', '2026-02-05', 'Marie Leroy', 2),
(3, '2025-08-10', '2025-08-14', 'Paul Moreau', 3),
(4, '2025-09-05', '2025-09-07', 'Lucie Martin', 4),
(9, '2026-01-15', '2026-01-18', 'Lucie Martin', 4),
(5, '2025-09-20', '2025-09-25', 'Emma Giraud', 5);

INSERT INTO Evaluation (id_Evaluation, Date_arrivee, La_note, Texte_descriptif, Nom_complet, id_Hotel) VALUES
(1, '2025-06-15', 5, 'Excellent séjour, personnel très accueillant.', 'Jean Dupont', 1),
(2, '2025-07-01', 4, 'Chambre propre, bon rapport qualité/prix.', 'Marie Leroy', 2),
(3, '2025-08-10', 3, 'Séjour correct mais bruyant la nuit.', 'Paul Moreau', 1),
(4, '2025-09-05', 5, 'Service impeccable, je recommande.', 'Lucie Martin', 2),
(5, '2025-09-20', 4, 'Très bon petit-déjeuner, hôtel bien situé.', 'Emma Giraud', 1);

SELECT * FROM evaluation;
