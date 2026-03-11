
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from pulp import LpProblem, LpVariable, LpMinimize, LpInteger, lpSum, value
import matplotlib.pyplot as plt

# --- Configuration Globale ---
st.set_page_config(page_title="DataCtrl Tropic Hub", page_icon="🎓", layout="wide")

# --- Styles CSS Personnalisés ---
st.markdown("""
<style>
    .big-font { font-size:20px !important; }
    .module-box { background-color: #f4f7f9; padding: 20px; border-radius: 10px; border-left: 5px solid #1f77b4; margin-bottom: 10px; }
    .theory-box { background-color: #fff8e1; padding: 15px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 15px; }
    .app-header { color: #2e7d32; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- Fonctions Utilitaires Pédagogiques ---
def show_theory(title, content):
    st.markdown(f"<div class='theory-box'><b>📖 Théorie : {title}</b><br>{content}</div>", unsafe_allow_html=True)

def show_metrics_grid(col, label, value, delta=None):
    col.metric(label=label, value=value, delta=delta)

# ==============================================================================
# APPLICATION 1 : RETAIL / COMMERCIAL
# ==============================================================================

def app_commercial():
    st.sidebar.markdown("---")
    st.sidebar.title("🏪 Modules Retail")
    module = st.sidebar.radio("Choisissez le module :", 
                              ["1. Prévisions des Ventes", "2. Dashboard Commercial"])
    
    if module == "1. Prévisions des Ventes":
        st.title("🌤️ Module : Prévisions Budgétaires & Saisonnalité")
        st.markdown("### Entreprise : **Naija Beverages Ltd**")
        
        # PARTIE COURS
        show_theory("L'Analyse Prédictive", 
            "Dans le contrôle de gestion, les budgets sont souvent statiques. L'analyse prédictive utilise l'historique pour projeter l'avenir. "
            "En zone tropicale, les variables clés sont la <b>Saison</b> (Sèche/Pluie) et les <b>Événements</b> (Ramadan, Fêtes).")
        
        st.markdown("---")
        
        # PARTIE PRATIQUE
        st.markdown("#### 💻 Simulateur de Prévisions")
        
        np.random.seed(42)
        data = pd.DataFrame({
            'Budget': np.random.randint(500, 5000, 24),
            'Saison': np.random.choice(['Sèche', 'Pluie'], 24), 
            'Fete': np.random.choice([0, 1], 24),
            'Ventes': np.random.randint(10000, 50000, 24)
        })
        
        # Création de la variable encodée
        data['Est_Seche'] = (data['Saison'] == 'Sèche').astype(int)
        
        # CORRECTION ICI : Utilisation correcte de 'Est_Seche'
        data['Ventes'] = data['Ventes'] + (data['Est_Seche'] * 8000) + (data['Fete'] * 15000)

        X = data[['Budget', 'Est_Seche', 'Fete']]
        y = data['Ventes']
        model = LinearRegression().fit(X, y)

        c1, c2, c3 = st.columns(3)
        budget = c1.slider("Budget Marketing (K FCFA)", 500, 10000, 2000)
        saison = c2.radio("Saison", ['Sèche', 'Pluie'])
        fete = c3.checkbox("Période de Fête ?")

        est_seche = 1 if saison == 'Sèche' else 0
        pred = model.predict([[budget, est_seche, int(fete)]])[0]

        st.info(f"📈 **Prévision Calculée : {int(pred):,} FCFA**")
        st.line_chart(data['Ventes'])

    elif module == "2. Dashboard Commercial":
        st.title("📱 Module : Dashboard & Mobile Money")
        st.markdown("### Entreprise : **MarchéPlus**")
        
        show_theory("La Visualisation de Données", 
            "Un tableau de bord efficace doit répondre à 3 questions : <b>Où en sommes-nous ?</b> (KPIs), "
            "<b>Pourquoi ?</b> (Graphiques d'analyse), <b>Que faire ?</b> (Alertes).")

        # Génération données
        data = pd.DataFrame({
            'Region': np.random.choice(['Dakar', 'Abidjan', 'Cotonou'], 100),
            'Produit': np.random.choice(['Riz', 'Smartphone', 'Jus'], 100),
            'Paiement': np.random.choice(['Mobile Money', 'Cash'], 100, p=[0.7, 0.3]),
            'CA': np.random.randint(10000, 100000, 100)
        })

        # Filtres
        region = st.multiselect("Filtrer Région", data['Region'].unique(), default=data['Region'].unique())
        df = data[data['Region'].isin(region)]

        # KPIs
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric("CA Total", f"{df['CA'].sum():,} FCFA")
        kpi2.metric("Part Mobile Money", f"{(df[df['Paiement']=='Mobile Money']['CA'].sum() / df['CA'].sum())*100:.0f}%")
        kpi3.metric("Transactions", len(df))

        fig = px.bar(df.groupby('Produit')['CA'].sum().reset_index(), x='Produit', y='CA', color='Produit')
        st.plotly_chart(fig, use_container_width=True)

# ==============================================================================
# APPLICATION 2 : LOGISTIQUE / OPERATIONS
# ==============================================================================

def app_logistique():
    st.sidebar.markdown("---")
    st.sidebar.title("🚚 Modules Logistique")
    module = st.sidebar.radio("Choisissez le module :", 
                              ["1. Optimisation de Flotte", "2. Risque de Change"])

    if module == "1. Optimisation de Flotte":
        st.title("🛵 Module : Optimisation Linéaire")
        st.markdown("### Entreprise : **JijiExpress**")

        show_theory("La Recherche Opérationnelle", 
            "L'optimisation linéaire permet de trouver la solution mathématique <b>la meilleure</b> parmi des millions de possibilités, "
            "tout en respectant des contraintes (budget, capacité des camions, temps).")

        st.markdown("#### ⚙️ Paramètres du Problème")
        total_motos = st.number_input("Flotte Totale Disponible", 10, 100, 50)
        
        # Modèle Optimisation
        prob = LpProblem("Flotte", LpMinimize)
        zones = ["Centre-Ville", "Banlieue", "Industriel"]
        temps = {"Centre-Ville": 45, "Banlieue": 30, "Industriel": 20}
        
        # Variables
        motos = LpVariable.dicts("Motos", zones, 0, None, LpInteger)
        
        # Objectif
        prob += lpSum([motos[z] * temps[z] for z in zones])
        
        # Contraintes
        prob += lpSum([motos[z] for z in zones]) <= total_motos
        prob += motos["Centre-Ville"] >= 10 # Demande minimum
        prob += motos["Banlieue"] >= 5
        
        prob.solve()

        results = [{"Zone": z, "Motos Allouées": int(motos[z].value())} for z in zones]
        df_res = pd.DataFrame(results)

        col1, col2 = st.columns(2)
        col1.write("#### 🗺️ Allocation Optimale")
        col1.dataframe(df_res)
        col2.write("#### 📊 Visualisation")
        col2.bar_chart(df_res.set_index('Zone'))

    elif module == "2. Risque de Change":
        st.title("💱 Module : Décision Stratégique")
        st.markdown("### Projet : Investissement Minier")

        show_theory("Simulation Monte Carlo", 
            "Plutôt qu'une prévision unique (ex: 'Le taux sera 650'), on simule 1000 scénarios aléatoires pour mesurer la <b>probabilité de perte</b>.")

        invest = st.number_input("Investissement (USD)", value=1_000_000)
        taux = st.slider("Taux Actuel (FCFA/USD)", 500, 1000, 650)
        vol = st.slider("Volatilité estimée (%)", 5, 30, 10)

        if st.button("Lancer la Simulation"):
            sims = []
            for _ in range(1000):
                taux_futur = taux * (1 + np.random.normal(0, vol/100))
                revenus = 150000 * taux_futur # Revenus hypothétiques
                roi = (revenus - (invest * taux)) / (invest * taux)
                sims.append(roi)
            
            fig = go.Figure()
            fig.add_trace(go.Histogram(x=sims, name="ROI"))
            st.plotly_chart(fig)

            prob_perte = (np.array(sims) < 0).mean() * 100
            st.metric("Probabilité de Perte", f"{prob_perte:.1f}%", delta_color="inverse")

# ==============================================================================
# APPLICATION 3 : AGRO-INDUSTRIE
# ==============================================================================

def app_agro():
    st.sidebar.markdown("---")
    st.sidebar.title("🌾 Modules Agro-Industrie")
    module = st.sidebar.radio("Choisissez le module :", 
                              ["1. Rentabilité (Machine Learning)", "2. Gestion des Coûts"])

    if module == "1. Rentabilité (Machine Learning)":
        st.title("🥜 Module : Classification & Rentabilité")
        st.markdown("### Entreprise : **TropiCashew**")

        show_theory("L'Arbre de Décision", 
            "C'est un algorithme qui découpe les données en créant des règles 'Si... Alors...'. "
            "C'est un outil puissant pour expliquer pourquoi un projet est rentable ou non.")

        st.markdown("#### 🧪 Testez un nouveau projet d'achat")
        
        # Données
        data = pd.DataFrame({
            'Prix': [350, 400, 380, 450, 300, 420],
            'Route': ['Bon', 'Mauvais', 'Moyen', 'Mauvais', 'Bon', 'Moyen'],
            'Rendement': [0.4, 0.25, 0.35, 0.20, 0.45, 0.38],
            'OK': [1, 0, 1, 0, 1, 1]
        })
        map_route = {'Bon': 2, 'Moyen': 1, 'Mauvais': 0}
        data['Route_Num'] = data['Route'].map(map_route)
        
        clf = DecisionTreeClassifier().fit(data[['Prix', 'Route_Num', 'Rendement']], data['OK'])

        prix = st.slider("Prix d'achat (FCFA/kg)", 200, 600, 350)
        route = st.select_slider("Qualité Route", options=['Mauvais', 'Moyen', 'Bon'])
        rendement = st.slider("Rendement", 0.1, 0.5, 0.3)

        pred = clf.predict([[prix, map_route[route], rendement]])[0]

        if pred == 1:
            st.success("✅ Projet Rentable selon le modèle")
        else:
            st.error("🚨 Projet à Risque selon le modèle")

    elif module == "2. Gestion des Coûts":
        st.title("💰 Module : Analyse des Écarts")
        st.markdown("### Contexte : Analyse mensuelle")

        show_theory("L'Écart sur Coût", 
            "L'écart est la différence entre le Coût Standard (Prévu) et le Coût Réel. "
            "Écart = (Coût Réel - Coût Standard) x Quantité Réelle.")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Budget Initial**")
            st.write("Coût Matière : 300 FCFA/kg")
            st.write("Quantité : 1000 kg")
        with col2:
            st.markdown("**Réalité**")
            real_cost = st.number_input("Coût Réel (FCFA/kg)", value=320)
            real_qty = st.number_input("Quantité Réelle (kg)", value=950)

        ecart = (real_cost - 300) * real_qty
        st.metric("Écart Total sur Matières", f"{int(ecart):,} FCFA", delta_color="inverse")

# --- MAIN HUB ---

def main():
    st.sidebar.title("🎓 DataCtrl Tropic Hub")
    
    menu = st.sidebar.radio(
        "🏠 Hub Principal",
        ["Accueil", "🏪 App Commerciale", "🚚 App Logistique", "🌾 App Agro-Industrie"]
    )

    if "Accueil" in menu:
        st.title(" Bienvenue dans le Hub de Formation")
        st.markdown("### Intégration Contrôle de Gestion & Data Science")
        
        st.info("Cette application centralise **3 Applications Métiers** distinctes. Sélectionnez une application dans le menu latéral pour accéder à ses modules spécifiques.")
        
        col1, col2, col3 = st.columns(3)
        col1.markdown("""
        #### 🏪 App Commerciale
        *Secteur : Distribution & Retail*
        - Prévisions des ventes
        - Dashboard Mobile Money
        """)
        
        col2.markdown("""
        #### 🚚 App Logistique
        *Secteur : Transport & Import*
        - Optimisation de flotte
        - Gestion du risque de change
        """)
        
        col3.markdown("""
        #### 🌾 App Agro-Industrie
        *Secteur : Transformation*
        - Analyse de rentabilité (IA)
        - Gestion des coûts
        """)
        
        st.write("👈 **Utilisez le menu latéral pour lancer une application.**")

    elif "App Commerciale" in menu:
        app_commercial()
    
    elif "App Logistique" in menu:
        app_logistique()
        
    elif "App Agro-Industrie" in menu:
        app_agro()

if __name__ == "__main__":
    main()
