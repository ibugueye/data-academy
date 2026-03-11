import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from pulp import LpProblem, LpVariable, LpMinimize, LpInteger, lpSum, value
import matplotlib.pyplot as plt

# --- Configuration de la Page ---
st.set_page_config(
    page_title="DataCtrl Tropic Academy - Formation Complète",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Personnalisé pour le style "Cours" ---
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem; color: #2e7d32; font-weight: bold;
    }
    .concept-box {
        background-color: #f0f7f0; padding: 20px; border-radius: 10px;
        border-left: 5px solid #2e7d32; margin-bottom: 20px;
    }
    .warning-box {
        background-color: #fff3e0; padding: 15px; border-radius: 10px;
        border-left: 5px solid #ef6c00;
    }
    .code-term {
        font-family: monospace; background-color: #e8f5e9; padding: 2px 5px; border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# --- Fonctions Utilitaires ---
def show_concept_box(title, content):
    st.markdown(f"""
    <div class="concept-box">
        <h4>📖 {title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

# --- Modules de Formation ---

def module_1_previsions():
    st.title("Module 1 : Analyse Prédictive & Budgets 📈")
    
    # --- SECTION COURS ---
    st.markdown("### 🎓 Partie 1 : Les Concepts Fondamentaux")
    
    col_theory1, col_theory2 = st.columns(2)
    
    with col_theory1:
        show_concept_box("Le Contrôle de Gestion Classique", 
            "Traditionnellement, les budgets sont basés sur <b>l'analyse glissante</b> (année N vs année N-1). "
            "Cette méthode ignore les variations brutales de l'environnement (inflation, crises, météo).")
            
        show_concept_box("L'apport de la Data Science",
            "L'<b>analyse prédictive</b> utilise les données historiques pour trouver des corrélations cachées. "
            "Par exemple : 'Quand la météo est bonne, les ventes de soda augmentent de 20%', indépendamment de l'année précédente.")

    with col_theory2:
        show_concept_box("Technologie : Régression Linéaire",
            "C'est un algorithme qui trace une droite 'idéale' à travers vos données. "
            "Formule : <code>Y = aX1 + bX2 + c</code>.<br>"
            "Où Y = Ventes, X1 = Marketing, X2 = Saison. L'algorithme calcule les meilleurs coefficients a, b et c.")
            
        show_concept_box("Contexte Tropicalisé 🌴",
            "Dans nos régions, les variables 'exogènes' sont cruciales : <br>"
            "• <b>Saisons</b> (Sèche/Pluie) impactent la logistique et la consommation.<br>"
            "• <b>Fêtes religieuses</b> (Ramadan, Tabaski) créent des pics de consommation imprévus par un calendrier grégorien standard.")

    st.markdown("---")
    
    # --- SECTION PRATIQUE ---
    st.markdown("### 💻 Partie 2 : Simulateur Interactif")
    st.info("👋 *Appliquez les concepts ci-dessus. Modifiez les variables pour voir comment le modèle prédictif réagit.*")

    # Génération données
    np.random.seed(42)
    data = pd.DataFrame({
        'Budget_Marketing_KCFA': np.random.randint(500, 5000, 24),
        'Saison': np.random.choice(['Sèche', 'Pluie'], 24), 
        'Fête': np.random.choice([0, 1], 24),
        'Ventes_Base': np.random.randint(10000, 50000, 24)
    })
    data['Est_Saison_Seche'] = (data['Saison'] == 'Sèche').astype(int)
    data['Ventes'] = data['Ventes_Base'] + (data['Est_Saison_Seche'] * 8000) + (data['Fête'] * 20000)

    # Modèle
    X = data[['Budget_Marketing_KCFA', 'Est_Saison_Seche', 'Fête']]
    y = data['Ventes']
    model = LinearRegression().fit(X, y)

    # Interface
    c1, c2, c3 = st.columns(3)
    with c1:
        budget = st.slider("Budget Marketing (K FCFA)", 500, 10000, 2000)
        st.caption("_Variable contrôlable par le manager_")
    with c2:
        saison = st.radio("Saison", ['Sèche', 'Pluie'])
        st.caption("_Variable externe_")
    with c3:
        fete = st.checkbox("Période de Fête ?")
        st.caption("_Variable événementielle_")

    # Résultat
    est_seche = 1 if saison == 'Sèche' else 0
    prediction = model.predict([[budget, est_seche, int(fete)]])[0]

    st.markdown("#### 📊 Résultat de la Prédiction")
    st.metric(label="Ventes Estimées", value=f"{int(prediction):,} FCFA")

    # Interprétation pédagogique des coefficients
    with st.expander("🔍 Analysons les résultats du modèle (Cliquez pour voir le détail)") :
        st.write(f"Le modèle a calculé mathématiquement l'impact de chaque variable :")
        st.markdown(f"- **Impact Marketing :** Chaque 1 000 FCFA dépensé rapporte environ **{int(model.coef_[0] * 1000)} FCFA** de ventes.")
        st.markdown(f"- **Impact Saison Sèche :** Être en saison sèche ajoute naturellement **{int(model.coef_[1]):,} FCFA** au chiffre d'affaires.")
        st.markdown(f"- **Impact Fête :** Une fête religieuse ajoute un bonus net de **{int(model.coef_[2]):,} FCFA**.")

def module_2_rentabilite():
    st.title("Module 2 : Machine Learning & Analyse des Coûts 🥜")

    # --- SECTION COURS ---
    st.markdown("### 🎓 Partie 1 : De l'analyse statique à la classification")
    
    show_concept_box("La problématique de rentabilité",
        "En contrôle de gestion, on analyse souvent la rentabilité <i>a posteriori</i> (après que le projet est terminé). "
        "L'objectif ici est de prédire la rentabilité <i>avant</i> de s'engager.")

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("#### ❌ Méthode classique (Seuils)")
        st.write("On fixe des règles rigides : 'Si Prix > 400, Projet Refusé'.")
        st.warning("Problème : Cela ignore les interactions. Un prix élevé est acceptable si la qualité de la route est bonne.")
    
    with col_t2:
        st.markdown("#### ✅ Méthode Data Science (Arbre de décision)")
        st.write("L'algorithme apprend des projets passés pour créer des règles optimales complexes.")
        st.success("Avantage : Il comprend que 'Route Mauvaise + Prix Élevé' = Perte, mais 'Route Bonne + Prix Élevé' = Gain possible.")

    st.markdown("---")

    # --- SECTION PRATIQUE ---
    st.markdown("### 💻 Partie 2 : Laboratoire de Prédiction")
    
    data = pd.DataFrame({
        'Prix_Achat_Paysan': [350, 400, 380, 450, 300, 420, 500, 310, 550, 390],
        'Qualite_Route': ['Bon', 'Mauvais', 'Moyen', 'Mauvais', 'Bon', 'Moyen', 'Mauvais', 'Bon', 'Mauvais', 'Bon'],
        'Rendement': [0.40, 0.25, 0.35, 0.20, 0.45, 0.38, 0.22, 0.42, 0.18, 0.40],
        'Rentable': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    })
    
    map_route = {'Bon': 2, 'Moyen': 1, 'Mauvais': 0}
    data['Qualite_Route_Num'] = data['Qualite_Route'].map(map_route)
    
    X = data[['Prix_Achat_Paysan', 'Qualite_Route_Num', 'Rendement']]
    y = data['Rentable']
    clf = DecisionTreeClassifier(max_depth=3).fit(X, y)

    st.write("Entrez les paramètres d'un nouveau projet d'achat de noix de cajou :")
    col1, col2, col3 = st.columns(3)
    with col1:
        prix = st.slider("Prix d'achat (FCFA/kg)", 200, 600, 350)
    with col2:
        route = st.select_slider("Qualité de la route", options=['Mauvais', 'Moyen', 'Bon'])
    with col3:
        rendement = st.slider("Rendement (%)", 20, 50, 35) / 100

    route_num = map_route[route]
    prediction = clf.predict([[prix, route_num, rendement]])[0]
    proba = clf.predict_proba([[prix, route_num, rendement]])[0][1]

    # Affichage pédagogique
    if prediction == 1:
        st.success(f"✅ Décision IA : Projet Rentable (Confiance : {proba*100:.0f}%)")
        st.write("💡 **Explication :** Basé sur l'historique, cette combinaison de facteurs a conduit au succès dans la majorité des cas.")
    else:
        st.error(f"🚨 Décision IA : Projet à Risque (Confiance : {(1-proba)*100:.0f}%)")
        st.write("💡 **Explication :** Le modèle détecte un pattern de perte similaire aux projets passés ayant échoué.")

    with st.expander("👁️ Voir la 'Boîte Noire' (Arbre de décision)") :
        st.write("Visualisez comment l'IA prend sa décision. Chaque 'nœud' est une question posée aux données.")
        fig, ax = plt.subplots(figsize=(12, 6))
        plot_tree(clf, feature_names=['Prix', 'Route', 'Rendement'], 
                  class_names=['Perte', 'Gain'], filled=True, ax=ax, impurity=False)
        st.pyplot(fig)
        st.caption("Lecture : Si la condition est VRAI, allez à gauche, sinon à droite. La couleur indique la classe majoritaire.")

def module_3_logistique():
    st.title("Module 3 : Optimisation Linéaire & Processus 🛵")

    # --- SECTION COURS ---
    st.markdown("### 🎓 Partie 1 : La Recherche Opérationnelle")
    
    show_concept_box("Le Problème d'Allocation",
        "Le gestionnaire doit souvent allouer des ressources limitées (camions, budgets, personnel) "
        "pour atteindre un objectif (minimiser les coûts ou maximiser les profits) sous des contraintes (demandes clients, lois).")

    st.markdown("""
    #### 🧱 Les 3 piliers de l'optimisation :
    1. **La Fonction Objectif :** Ce qu'on veut optimiser (ex: Minimiser le temps de trajet total).
    2. **Les Variables de Décision :** Ce qu'on peut changer (ex: Nombre de motos dans le quartier A).
    3. **Les Contraintes :** Les limites infranchissables (ex: On a seulement 50 motos au total, la demande client doit être satisfaite à 80%).
    """)
    
    st.markdown("---")

    # --- SECTION PRATIQUE ---
    st.markdown("### 💻 Partie 2 : Simulateur d'Affectation")
    
    st.info("Contexte : JijiExpress doit répartir sa flotte de motos entre 3 zones urbaines.")

    total_motos = st.number_input("Ressource Totale Disponible (Motos)", 10, 200, 50, key="motos")
    
    st.markdown("#### Données du problème (Paramètres fixes)")
    param_data = pd.DataFrame({
        'Zone': ['Centre-Ville', 'Banlieue', 'Zone Industrielle'],
        'Temps de trajet moyen (min)': [45, 30, 20],
        'Demande Client (min)': [10, 5, 15]
    })
    st.table(param_data)

    # Modèle PuLP
    prob = LpProblem("Optimisation_Logistique", LpMinimize)
    zones = param_data['Zone'].tolist()
    motos_vars = LpVariable.dicts("Motos", zones, 0, None, LpInteger)
    temps = dict(zip(zones, param_data['Temps de trajet moyen (min)']))
    demande = dict(zip(zones, param_data['Demande Client (min)']))

    # Objectif
    prob += lpSum([motos_vars[z] * temps[z] for z in zones]), "Temps_Total_Minutes"
    
    # Contraintes
    prob += lpSum([motos_vars[z] for z in zones]) <= total_motos, "Taille_Flotte"
    for z in zones:
        prob += motos_vars[z] >= demande[z], f"Dem_{z}"

    prob.solve()

    # Résultats
    res_data = []
    for z in zones:
        res_data.append({"Zone": z, "Motos Allouées": int(motos_vars[z].value())})
    
    df_res = pd.DataFrame(res_data)
    
    col_res1, col_res2 = st.columns([1, 1])
    with col_res1:
        st.metric("⏱️ Temps total de travail optimisé", f"{int(value(prob.objective)):,} min")
    with col_res2:
        st.metric("📦 Taux d'utilisation de la flotte", f"{sum(df_res['Motos Allouées']) / total_motos * 100:.0f}%")
    
    st.bar_chart(df_res.set_index('Zone'))
    
    st.markdown("""
    <div class="warning-box">
    <b>💡 Leçon Contrôle de Gestion :</b> 
    Notez que l'allocation n'est pas proportionnelle à la demande. L'algorithme privilégie la <b>Zone Industrielle</b> 
    car le temps de trajet y est le plus faible (20 min). C'est l'essence de l'optimisation : maximiser l'efficacité, 
    pas l'équité.
    </div>
    """, unsafe_allow_html=True)

def module_4_dashboard():
    st.title("Module 4 : Data Visualization & Tableaux de Bord 📱")

    # --- SECTION COURS ---
    st.markdown("### 🎓 Partie 1 : La Data Visualization au service du Management")
    
    show_concept_box("Le Storytelling avec les données",
        "Un contrôleur de gestion ne doit pas seulement produire des chiffres, il doit les <b>faire parler</b>. "
        "La visualisation transforme des lignes Excel en décisions stratégiques.")

    st.markdown("""
    #### 📐 Règles d'or d'un bon Dashboard :
    * **KPIs en haut :** Les indicateurs clés (Chiffre d'affaires, Marge) doivent être visibles immédiatement.
    * **Filtres (Slicers) :** Permettre à l'utilisateur de filtrer par région ou par temps pour explorer.
    * **Contexte :** Comparer avec l'année précédente (N-1) ou avec le budget prévu.
    """)

    st.markdown("---")
    
    # --- SECTION PRATIQUE ---
    st.markdown("### 💻 Partie 2 : Construction d'un Dashboard Commercial")
    
    # Données
    regions = ['Dakar', 'Abidjan', 'Cotonou', 'Lomé', 'Bamako']
    produits = ['Riz', 'Smartphone', 'Huile', 'Jus', 'Farine']
    data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=100),
        'Region': np.random.choice(regions, 100),
        'Produit': np.random.choice(produits, 100),
        'Paiement': np.random.choice(['Mobile Money', 'Cash', 'Carte'], 100, p=[0.6, 0.3, 0.1]),
        'CA_XOF': np.random.randint(20000, 200000, 100)
    })

    # Filtres
    c1, c2 = st.columns(2)
    with c1:
        region_filter = st.multiselect("Filtrer par Région", data['Region'].unique(), default=data['Region'].unique())
    with c2:
        produit_filter = st.multiselect("Filtrer par Produit", data['Produit'].unique(), default=data['Produit'].unique())

    # Application filtres
    df = data[data['Region'].isin(region_filter) & data['Produit'].isin(produit_filter)]

    # KPIs
    st.markdown("#### 📊 Indicateurs de Performance (KPIs)")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("💰 CA Total", f"{df['CA_XOF'].sum():,} FCFA")
    kpi2.metric("📱 Part Mobile Money", f"{(df[df['Paiement']=='Mobile Money']['CA_XOF'].sum() / df['CA_XOF'].sum()) * 100:.1f}%")
    kpi3.metric("📦 Panier Moyen", f"{df['CA_XOF'].mean():,.0f} FCFA")

    # Graphiques
    tab1, tab2 = st.tabs(["Analyse Produits", "Analyse Paiement"])
    with tab1:
        fig_prod = px.bar(df.groupby('Produit')['CA_XOF'].sum().reset_index(), 
                          x='Produit', y='CA_XOF', color='Produit', title="Ventes par Famille de Produit")
        st.plotly_chart(fig_prod, use_container_width=True)
        st.markdown("**Interprétation :** Identifiez rapidement les produits locomotives vs les produits d'appel.")
    
    with tab2:
        fig_pay = px.pie(df, names='Paiement', values='CA_XOF', title="Répartition des Modes de Paiement")
        st.plotly_chart(fig_pay, use_container_width=True)
        st.markdown("**Interprétation :** L'importance du Mobile Money justifie-t-elle une baisse des coûts de gestion d'espèces ?")

def module_5_strategie():
    st.title("Module 5 : Aide à la Décision Stratégique & Risques 💱")

    # --- SECTION COURS ---
    st.markdown("### 🎓 Partie 1 : Gestion du Risque et Probabilités")
    
    show_concept_box("L'incertitude en contrôle de gestion",
        "Contrairement à la comptabilité qui est 'exacte', la gestion est 'probable'. "
        "Les décisions d'investissement se basent sur des prévisions incertaines (taux de change, politique, météo).")

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("#### ❌ L'Erreur Classique")
        st.write("Utiliser une valeur unique : 'Le Dollar sera à 650 FCFA'.")
        st.write("Risque : Si le Dollar passe à 700, tout le projet s'effondre.")
    
    with col_t2:
        st.markdown("#### ✅ La Méthode Monte Carlo")
        st.write("Simuler **10 000 scénarios** différents où le taux de change varie selon une loi de probabilité.")
        st.write("Résultat : On obtient une probabilité de réussite (ex: '80% de chance d'être rentable').")

    st.markdown("---")

    # --- SECTION PRATIQUE ---
    st.markdown("### 💻 Partie 2 : Simulateur d'Investissement")
    
    col_inputs, col_params = st.columns(2)
    with col_inputs:
        invest_usd = st.number_input("Investissement Initial (USD)", value=1_000_000, step=50000)
        revenu_annuel_usd = st.number_input("Revenu Annuel Espéré (USD)", value=250_000, step=10000)
    with col_params:
        taux_change = st.slider("Taux de change actuel (FCFA/USD)", 500, 1000, 650)
        volatilite = st.slider("Volatilité annuelle estimée (%)", 1, 40, 15)
        horizon = st.slider("Durée du projet (Années)", 1, 20, 5)

    if st.button("🎰 Lancer la Simulation (10 000 scénarios)", type="primary"):
        with st.spinner("Calcul en cours..."):
            np.random.seed(0)
            sims = []
            for _ in range(10000):
                # Evolution du taux sur 'horizon' années
                taux_proj = [taux_change]
                for _ in range(horizon):
                    change = np.random.normal(0, volatilite/100)
                    taux_proj.append(taux_proj[-1] * (1 + change))
                
                flux_fcfa = sum([revenu_annuel_usd * t for t in taux_proj[1:]])
                invest_fcfa = invest_usd * taux_change
                sims.append((flux_fcfa - invest_fcfa) / invest_fcfa) # ROI

            # Affichage
            st.markdown("#### Distribution des Retours sur Investissement (ROI)")
            fig = go.Figure()
            fig.add_trace(go.Histogram(x=sims, nbinsx=50, marker_color='#2e7d32', name="ROI"))
            fig.add_vrect(x0=0, x1=max(sims), fillcolor="green", opacity=0.1, layer="below", line_width=0, name="Zone Profit")
            fig.add_vrect(x0=min(sims), x1=0, fillcolor="red", opacity=0.1, layer="below", line_width=0, name="Zone Perte")
            st.plotly_chart(fig, use_container_width=True)

            prob_perte = (np.array(sims) < 0).mean() * 100
            
            st.markdown("#### 🏁 Conclusion Stratégique")
            if prob_perte > 40:
                st.error(f"🚨 Risque Élevé. Il y a **{prob_perte:.0f}%** de chances de perdre de l'argent.")
                st.write("**Décision recommandée :** Abandonner ou demander une couverture de change (Assurance).")
            elif prob_perte > 20:
                st.warning(f"⚠️ Risque Modéré. Probabilité de perte : **{prob_perte:.0f}%**.")
                st.write("**Décision recommandée :** Négocier les coûts d'entrée pour créer un 'coussin de sécurité'.")
            else:
                st.success(f"✅ Projet Solide. Probabilité de perte : seulement **{prob_perte:.0f}%**.")
                st.write("**Décision recommandée :** Investir (Go).")

# --- Navigation Principale ---

def main():
    st.sidebar.title("🎓 DataCtrl Tropic Academy")
    st.sidebar.write("Formation Intégrée")
    st.sidebar.markdown("---")
    
    menu = st.sidebar.radio(
        "📚 Sommaire du Cours",
        ["Accueil", 
         "1. Prévisions & Budgets", 
         "2. Coûts & Machine Learning", 
         "3. Optimisation & Processus", 
         "4. Dashboards & Visualisation", 
         "5. Stratégie & Risques"]
    )

    if menu == "Accueil":
        st.markdown('<p class="main-title">Bienvenue dans la Formation DataCtrl</p>', unsafe_allow_html=True)
        st.write("##### L'intégration du Contrôle de Gestion et de la Data Science en contexte tropical.")
        
        st.markdown("""
        Cette application est un **cours interactif**. Pour chaque module, vous trouverez :
        1. **📖 La Théorie :** Explication détaillée des concepts (Qu'est-ce qu'une régression ? Qu'est-ce qu'un KPI ?).
        2. **🛠️ La Pratique :** Un simulateur interactif pour appliquer le concept en temps réel.
        3. **💡 L'Interprétation :** Comment lire les résultats pour prendre une décision.

        ### 🚦 Comment utiliser cette application ?
        Commencez par le module 1 dans le menu latéral et progressez à votre rythme.
        """)

        st.info("👋 **Public cible :** Étudiants, Contrôleurs de Gestion, Managers, Analystes Data.")

    elif menu == "1. Prévisions & Budgets":
        module_1_previsions()
    elif menu == "2. Coûts & Machine Learning":
        module_2_rentabilite()
    elif menu == "3. Optimisation & Processus":
        module_3_logistique()
    elif menu == "4. Dashboards & Visualisation":
        module_4_dashboard()
    elif menu == "5. Stratégie & Risques":
        module_5_strategie()

if __name__ == "__main__":
    main()