import streamlit as st
import pandas as pd
from datetime import date
from database import HotelDatabase

# Configuration de la page
st.set_page_config(page_title="Gestion d'Hôtels", page_icon="🏨", layout="wide")

@st.cache_resource
def init_database():
    return HotelDatabase()

db = init_database()

# Titre principal
st.title("🏨 Système de Gestion d'Hôtels")
st.markdown("---")

# Menu de navigation
menu = st.sidebar.selectbox(
    "Navigation",
    ["🏠 Accueil", "📋 Réservations", "👥 Clients", "🏨 Chambres Disponibles", "➕ Ajouter Client", "📅 Nouvelle Réservation"]
)

if menu == "🏠 Accueil":
    st.header("Bienvenue dans le Système de Gestion d'Hôtels")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📋 Réservations", len(db.get_reservations()))

    with col2:
        st.metric("👥 Clients", len(db.get_clients()))

    with col3:
        today = date.today()
        available_today = db.get_available_rooms(today, today)
        st.metric("🏨 Chambres Libres Aujourd'hui", len(available_today))

    st.markdown("---")
    st.markdown("""
    ### Fonctionnalités disponibles :
    - 📋 Réservations
    - 👥 Clients
    - 🏨 Chambres Disponibles
    - ➕ Ajouter Client
    - 📅 Nouvelle Réservation
    """)

elif menu == "📋 Réservations":
    st.header("📋 Liste des Réservations")
    try:
        reservations = db.get_reservations()
        if not reservations.empty:
            reservations['date_debut'] = pd.to_datetime(reservations['date_debut']).dt.strftime('%d/%m/%Y')
            reservations['date_fin'] = pd.to_datetime(reservations['date_fin']).dt.strftime('%d/%m/%Y')

            reservations_display = reservations.rename(columns={
                'id_reservation': 'ID',
                'date_debut': 'Date Début',
                'date_fin': 'Date Fin',
                'nom': 'Client',
                'email': 'Email',
                'ville': 'Ville Hôtel',
                'pays': 'Pays',
                'numero': 'N° Chambre',
                'type': 'Type Chambre'
            })

            st.dataframe(reservations_display, use_container_width=True)
            st.success(f"Total: {len(reservations)} réservations")
        else:
            st.info("Aucune réservation trouvée.")
    except Exception as e:
        st.error(f"Erreur: {e}")

elif menu == "👥 Clients":
    st.header("👥 Liste des Clients")
    try:
        clients = db.get_clients()
        if not clients.empty:
            clients_display = clients.rename(columns={
                'id_client': 'ID',
                'nom': 'Nom',
                'email': 'Email',
                'telephone': 'Téléphone',
                'adresse': 'Adresse',
                'ville': 'Ville',
                'code_postal': 'Code Postal'
            })

            st.dataframe(clients_display, use_container_width=True)
            st.success(f"Total: {len(clients)} clients")
        else:
            st.info("Aucun client trouvé.")
    except Exception as e:
        st.error(f"Erreur: {e}")

elif menu == "🏨 Chambres Disponibles":
    st.header("🏨 Chambres Disponibles")

    col1, col2 = st.columns(2)
    with col1:
        date_debut = st.date_input("Date de début", value=date.today())
    with col2:
        date_fin = st.date_input("Date de fin", value=date.today())

    if date_debut <= date_fin:
        try:
            chambres = db.get_available_rooms(date_debut, date_fin)
            if not chambres.empty:
                chambres_display = chambres.rename(columns={
                    'id_chambre': 'ID',
                    'numero': 'N° Chambre',
                    'nb_personnes': 'Nb Personnes',
                    'balcon': 'Balcon',
                    'ville': 'Ville Hôtel',
                    'type': 'Type',
                    'prix': 'Prix (€/nuit)'
                })

                st.dataframe(chambres_display, use_container_width=True)
                st.success(f"Total: {len(chambres)} chambres disponibles")
            else:
                st.warning("Aucune chambre disponible pour cette période.")
        except Exception as e:
            st.error(f"Erreur: {e}")
    else:
        st.error("La date de fin doit être postérieure ou égale à la date de début.")

elif menu == "➕ Ajouter Client":
    st.header("➕ Ajouter un Nouveau Client")
    with st.form("add_client_form"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom complet *")
            email = st.text_input("Email *")
            telephone = st.text_input("Téléphone")
        with col2:
            adresse = st.text_input("Adresse")
            ville = st.text_input("Ville")
            code_postal = st.text_input("Code Postal")

        submitted = st.form_submit_button("Ajouter le Client", type="primary")

        if submitted:
            if nom and email:
                success, message = db.add_client(nom, email, telephone, adresse, ville, code_postal)
                if success:
                    st.success(message)
                    st.balloons()
                else:
                    st.error(message)
            else:
                st.error("Le nom et l'email sont obligatoires.")

elif menu == "📅 Nouvelle Réservation":
    st.header("📅 Nouvelle Réservation")

    col1, col2 = st.columns(2)
    with col1:
        date_debut = st.date_input("Date de début *", value=date.today())
    with col2:
        date_fin = st.date_input("Date de fin *", value=date.today())

    if date_debut <= date_fin:
        clients = db.get_clients()
        if not clients.empty:
            client_options = {f"{row['nom']} ({row['email']})": row['id_client'] for _, row in clients.iterrows()}

            chambres = db.get_available_rooms(date_debut, date_fin)
            if not chambres.empty:
                chambre_options = {f"Chambre {row['numero']} - {row['type']} - {row['ville']} ({row['prix']}€/nuit)": row['id_chambre'] for _, row in chambres.iterrows()}

                with st.form("add_reservation_form"):
                    client_choice = st.selectbox("Client *", list(client_options.keys()))
                    chambre_choice = st.selectbox("Chambre *", list(chambre_options.keys()))
                    submitted = st.form_submit_button("Réserver", type="primary")

                    if submitted:
                        id_client = client_options[client_choice]
                        id_chambre = chambre_options[chambre_choice]
                        success, message = db.add_reservation(date_debut, date_fin, id_client, id_chambre)
                        if success:
                            st.success(message)
                            st.balloons()
                        else:
                            st.error(message)
            else:
                st.warning("Aucune chambre disponible pour cette période.")
        else:
            st.warning("Aucun client trouvé. Ajoutez d'abord un client.")
    else:
        st.error("La date de fin doit être postérieure ou égale à la date de début.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>"
    "Projet Bases de Données - Licence MIP IAP S4 2025 - Pr. J.ZAHIR"
    "</div>",
    unsafe_allow_html=True
)
