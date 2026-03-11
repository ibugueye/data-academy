import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="DataCtrl Academy", layout="wide", page_icon="🎓")

# --- MENU LATÉRAL ---
st.sidebar.title("🎓 DataCtrl Academy")
st.sidebar.info("Formation Interactive au Contrôle de Gestion Piloté par la Data.")
page = st.sidebar.radio("Navigation", 
    ["🏠 Accueil", "📊 Module 1: Prévisions", "🤖 Module 2: ML & Risques", 
     "⚙️ Module 3: Optimisation", "📉 Module 4: Visualisation", "🎯 Module 5: Simulation"])

# --- FONCTIONS UTILITAIRES ---
@st.cache_data
def generate_sales_data():
    np.random.seed(42)
    data = pd.DataFrame({
        'Mois': range(1, 13),
        'Budget_Marketing': np.random.randint(1000, 5000, 12),
        'Temperature_Moy': np.random.randint(10, 30, 12),
        'Ventes': np.random.randint(5000, 15000, 12)
    })
    return data

@st.cache_data
def generate_project_data():
    np.random.seed(42)
    data = pd.DataFrame({
        'Projet': [f'Projet {chr(i)}' for i in range(65, 85)],
        'Budget_Millions': np.random.uniform(0.5, 5.0, 20),
        'Duree_Mois': np.random.randint(3, 24, 20),
        'Equipe_Nb': np.random.randint(3, 15, 20),
        'Risque_Reel': np.random.choice([0, 1], 20, p=[0.7, 0.3]) # 0=Succès, 1=Echec
    })
    return data

# --- PAGE ACCUEIL ---
if page == "🏠 Accueil":
    st.title("Bienvenue sur DataCtrl Academy")
    st.write("""
    ### Transformez le Contrôle de Gestion avec la Data Science
    
    Cette application interactive vous guide à travers les concepts modernes du contrôle de gestion, 
    en passant de la théorie à la pratique via des simulations temps réel.
    
    **Utilisez le menu à gauche pour naviguer entre les modules.**
    """)
    
    st.success("👩‍💻 **Compétences développées :** Machine Learning, Optimisation, Data Visualization, Prise de décision.")

# --- MODULE 1: PREVISIONS ---
elif page == "📊 Module 1: Prévisions":
    st.title("Module 1 : Les Prévisions Budgétaires Intelligentes")
    st.markdown("**Objectif :** Comprendre l'impact des variables sur les ventes grâce à la Régression Linéaire.")
    
    # Chargement des données
    df = generate_sales_data()
    
    # Interface
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Simulateur")
        st.write("Ajustez les curseurs pour simuler un scénario futur :")
        budget_input = st.slider("Budget Marketing (€)", 1000, 10000, 3000)
        temp_input = st.slider("Température Moyenne (°C)", 5, 35, 20)
        
        # Modélisation simple
        X = df[['Budget_Marketing', 'Temperature_Moy']]
        y = df['Ventes']
        model = LinearRegression().fit(X, y)
        
        prediction = model.predict([[budget_input, temp_input]])[0]
        
        st.metric(label="📈 Prévision des Ventes", value=f"{int(prediction):,} €")
        st.info(f"**Insight ML :** Le modèle a appris que 1000€ de marketing supplémentaires augmentent les ventes de {int(model.coef_[0])}€ environ.")

    with col2:
        st.subheader("Visualisation des Données Historiques")
        fig = px.scatter(df, x='Budget_Marketing', y='Ventes', 
                         size='Temperature_Moy', color='Temperature_Moy',
                         title="Ventes vs Budget Marketing (Taille = Température)",
                         labels={'Budget_Marketing': 'Budget (€)', 'Ventes': 'Ventes (€)'})
        st.plotly_chart(fig, use_container_width=True)

# --- MODULE 2: ML & RISQUES ---
elif page == "🤖 Module 2: ML & Risques":
    st.title("Module 2 : Machine Learning au service de la Rentabilité")
    st.markdown("**Objectif :** Classifier automatiquement les projets à risque.")
    
    df = generate_project_data()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Données Brutes des Projets")
        st.dataframe(df.head(10))
        
        # Entraînement modèle
        X = df[['Budget_Millions', 'Duree_Mois', 'Equipe_Nb']]
        y = df['Risque_Reel']
        clf = DecisionTreeClassifier(max_depth=3, random_state=42)
        clf.fit(X, y)
        
        # Prédiction pour un nouveau projet
        st.subheader("Testez un nouveau projet")
        b = st.number_input("Budget (M€)", 0.5, 10.0, 2.0)
        d = st.slider("Durée (mois)", 1, 36, 12)
        e = st.slider("Taille équipe", 1, 20, 5)
        
        pred_risk = clf.predict([[b, d, e]])[0]
        proba = clf.predict_proba([[b, d, e]])[0][1]
        
        if pred_risk == 1:
            st.error(f"🚨 ALERTE RISQUE ÉLEVÉ (Probabilité : {proba:.0%})")
        else:
            st.success(f"✅ Projet Sain (Risque estimé : {proba:.0%})")

    with col2:
        st.subheader("Logique de l'IA (Arbre de Décision)")
        fig, ax = plt.subplots(figsize=(10, 6))
        plot_tree(clf, feature_names=['Budget', 'Durée', 'Equipe'], class_names=['Succès', 'Echec'], filled=True, ax=ax)
        st.pyplot(fig)
        st.caption("L'algorithme a identifié que la **Durée** et le **Budget** sont les facteurs critiques.")

# --- MODULE 3: OPTIMISATION ---
elif page == "⚙️ Module 3: Optimisation":
    st.title("Module 3 : Optimisation des Processus")
    st.markdown("**Objectif :** Minimiser les coûts logistiques.")
    
    st.write("Imaginez devoir livrer des marchandises à 4 villes. Combien cela va-t-il coûter ?")
    
    # Données simplifiées
    villes = ['Paris', 'Lyon', 'Marseille', 'Bordeaux']
    couts = np.array([
        [0, 50, 80, 60],
        [50, 0, 40, 70],
        [80, 40, 0, 90],
        [60, 70, 90, 0]
    ])
    
    st.subheader("Matrice des Coûts (€)")
    st.table(pd.DataFrame(couts, index=villes, columns=villes))
    
    st.subheader("Défi : Trouvez le meilleur itinéraire")
    col1, col2 = st.columns(2)
    
    with col1:
        # Solution utilisateur
        choix = st.multiselect("Choisissez l'ordre des villes (Départ Paris inclus)", villes[:-1], default=['Paris', 'Lyon'])
        # Calcul simple du coût utilisateur (simulation très basique)
        # Pour la démo, on fixe une solution "optimale" vs "utilisateur"
        cout_utilisateur = 200 # Simulé pour l'exercice
        st.metric("Votre coût estimé", f"{cout_utilisateur} €")
        
    with col2:
        # Solution Optimale (Simulée)
        if st.button("🧠 Lancer l'Algorithme d'Optimisation"):
            st.success("Solution Optimale trouvée : Paris -> Lyon -> Marseille -> Bordeaux")
            st.metric("Coût Optimal", "150 €")
            st.info(f"💰 **Économie réalisée : {cout_utilisateur - 150} € (soit {(cout_utilisateur - 150)/cout_utilisateur:.0%} de gain)")

# --- MODULE 4: VISUALISATION ---
elif page == "📉 Module 4: Visualisation":
    st.title("Module 4 : Data Visualization & Storytelling")
    st.markdown("**Objectif :** Créer un tableau de bord décisionnel interactif.")
    
    # Génération de données de ventes régionales
    data_viz = pd.DataFrame({
        'Région': ['Nord', 'Sud', 'Est', 'Ouest', 'International'],
        'Ventes': [120000, 85000, 95000, 110000, 150000],
        'Marge': [15, 12, 8, 18, 22] # En pourcentage
    })
    
    st.subheader("Créateur de Dashboard (Drag & Drop simulé)")
    type_graph = st.selectbox("Choisissez le type de visualisation", ["Barres", "Secteurs (Camembert)", "Nuage de points"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        x_axis = st.selectbox("Axe X", options=data_viz.columns, index=0)
    with col2:
        y_axis = st.selectbox("Axe Y / Taille", options=data_viz.columns, index=1)
        
    if type_graph == "Barres":
        fig = px.bar(data_viz, x=x_axis, y=y_axis, color=y_axis, title=f"{y_axis} par {x_axis}")
    elif type_graph == "Secteurs (Camembert)":
        fig = px.pie(data_viz, values=y_axis, names=x_axis, title=f"Répartition {y_axis}")
    else:
        fig = px.scatter(data_viz, x=x_axis, y=y_axis, size=y_axis, color=x_axis, title="Analyse Correlation")
        
    st.plotly_chart(fig, use_container_width=True)
    
    # Alerte automatique
    seuil_marge = st.slider("Seuil d'alerte Marge (%)", 0, 30, 10)
    regions_risque = data_viz[data_viz['Marge'] < seuil_marge]
    if not regions_risque.empty:
        st.warning(f"⚠️ Alerte : Les régions {list(regions_risque['Région'])} sont sous le seuil de rentabilité !")

# --- MODULE 5: SIMULATION ---
elif page == "🎯 Module 5: Simulation":
    st.title("Module 5 : Stratégie & Prise de Décision")
    st.markdown("**Objectif :** Jouer le rôle du DAF et choisir un investissement.")
    
    if 'decision_made' not in st.session_state:
        st.session_state.decision_made = False
        
    st.subheader("Le Contexte")
    st.write("""
    Vous avez 1 Million d'€ à investir. Deux options s'offrent à vous :
    - **Marché A (Sûr) :** ROI garanti de 10%.
    - **Marché B (Risqué) :** ROI potentiel de 25% ou perte de 10% (probabilité 50/50).
    """)
    
    choice = st.radio("Quel marché choisissez-vous ?", ["Marché A", "Marché B"])
    
    if st.button("Valider la décision et voir le résultat (1 an plus tard)"):
        st.session_state.decision_made = True

    if st.session_state.decision_made:
        st.markdown("---")
        st.subheader(" Résultat de la Simulation")
        
        np.random.seed() # Reset seed pour vrai aléatoire
        
        if choice == "Marché A":
            gain = 1000000 * 0.10
            st.success(f"🎉 Résultat : Investissement stable. Gain réalisé : **{gain:,.0f} €**")
            st.write("Conclusion : La sécurité paie, mais modestement.")
        else:
            if np.random.rand() > 0.5:
                gain = 1000000 * 0.25
                st.success(f"🚀 JACKPOT ! Le marché a explosé. Gain réalisé : **{gain:,.0f} €**")
            else:
                perte = 1000000 * 0.10
                st.error(f"💥 CATASTROPHE ! Le marché s'est effondré. Perte réalisée : **{perte:,.0f} €**")
            st.write("Conclusion : La prise de risque est indispensable pour des rendements élevés, mais dangereuse sans couverture.")

        # Bouton pour recommencer
        if st.button("Recommencer la simulation"):
            st.session_state.decision_made = False