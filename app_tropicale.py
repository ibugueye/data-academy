
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
    page_title="DataCtrl Tropic Academy",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Fonctions pour chaque Module ---

def module_1_previsions():
    st.title("Module 1 : Prévisions Budgétaires et Saisonnalité 🌧️☀️")
    st.write("### Contexte : Naija Beverages Ltd (Afrique de l'Ouest)")
    st.info("Les marchés tropicaux sont influencés par la saisonnalité (Sèche/Pluie) et les fêtes religieuses. Ajustez les paramètres pour voir l'impact sur les ventes.")

    # 1. Génération de données synthétiques
    np.random.seed(42)
    data = pd.DataFrame({
        'Budget_Marketing_KCFA': np.random.randint(500, 5000, 24),
        'Saison': np.random.choice(['Sèche', 'Pluie'], 24), 
        'Fête': np.random.choice([0, 1], 24),
        'Ventes_Base': np.random.randint(10000, 50000, 24)
    })
    
    # Logique métier tropicalisée
    data['Est_Saison_Seche'] = (data['Saison'] == 'Sèche').astype(int)
    data['Ventes'] = data['Ventes_Base'] + (data['Est_Saison_Seche'] * 8000) + (data['Fête'] * 20000)

    # Modélisation
    X = data[['Budget_Marketing_KCFA', 'Est_Saison_Seche', 'Fête']]
    y = data['Ventes']
    model = LinearRegression().fit(X, y)

    # Interface Utilisateur
    st.sidebar.header("Paramètres de Simulation")
    budget = st.sidebar.slider("Budget Marketing (K FCFA)", 500, 10000, 2000)
    saison = st.sidebar.radio("Saison à venir", ['Sèche', 'Pluie'])
    fete = st.sidebar.checkbox("Période de Fête (Ramadan / Tabaski / Noël) ?")

    # Calcul Prédiction
    est_seche = 1 if saison == 'Sèche' else 0
    prediction = model.predict([[budget, est_seche, int(fete)]])[0]

    # Affichage Résultats
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📈 Prévision des Ventes", value=f"{int(prediction):,} FCFA")
    
    with col2:
        # Graphique d'impact
        impact_data = pd.DataFrame({
            'Facteur': ['Marketing', 'Saison', 'Fêtes'],
            'Impact': [model.coef_[0] * budget, model.coef_[1] * est_seche, model.coef_[2] * int(fete)]
        })
        fig_impact = px.bar(impact_data, x='Facteur', y='Impact', title="Contribution à la vente (FCFA)")
        st.plotly_chart(fig_impact, use_container_width=True)

    st.markdown("---")
    st.write("#### 📊 Données Historiques Utilisées")
    st.dataframe(data[['Budget_Marketing_KCFA', 'Saison', 'Fête', 'Ventes']].head(10))

def module_2_rentabilite():
    st.title("Module 2 : Analyse des Coûts et Projet Agricole 🥜")
    st.write("### Contexte : TropiCashew (Filière Noix de Cajou)")
    st.warning("L'objectif est de prédire la rentabilité d'un projet d'achat en fonction de la qualité des infrastructures routières.")

    # Données simulées
    data = pd.DataFrame({
        'Prix_Achat_Paysan': [350, 400, 380, 450, 300, 420, 500, 310],
        'Qualite_Route': ['Bon', 'Mauvais', 'Moyen', 'Mauvais', 'Bon', 'Moyen', 'Mauvais', 'Bon'],
        'Rendement_Production': [0.40, 0.25, 0.35, 0.20, 0.45, 0.38, 0.22, 0.42],
        'Rentable': [1, 0, 1, 0, 1, 1, 0, 1]
    })
    
    # Encodage et Modèle
    map_route = {'Bon': 2, 'Moyen': 1, 'Mauvais': 0}
    data['Qualite_Route_Num'] = data['Qualite_Route'].map(map_route)
    
    X = data[['Prix_Achat_Paysan', 'Qualite_Route_Num', 'Rendement_Production']]
    y = data['Rentable']
    clf = DecisionTreeClassifier(max_depth=3).fit(X, y)

    # Interface
    col1, col2, col3 = st.columns(3)
    with col1:
        prix = st.slider("Prix d'achat aux producteurs (FCFA/kg)", 200, 600, 350)
    with col2:
        route = st.select_slider("État de la route vers l'usine", options=['Mauvais', 'Moyen', 'Bon'])
    with col3:
        rendement = st.slider("Rendement prévu (%)", 20, 50, 35) / 100

    # Prédiction
    route_num = map_route[route]
    prediction = clf.predict([[prix, route_num, rendement]])[0]
    proba = clf.predict_proba([[prix, route_num, rendement]])[0][1]

    # Résultat
    if prediction == 1:
        st.success(f"✅ Verdict : Projet Rentable (Confiance : {proba*100:.1f}%)")
        st.balloons()
    else:
        st.error(f"🚨 Verdict : Projet à Risque (Confiance : {(1-proba)*100:.1f}%)")
        st.write("💡 **Recommandation :** Négocier le prix d'achat ou améliorer la logistique.")

    # Visualisation de l'arbre
    with st.expander("🔍 Voir la logique de décision de l'IA (Arbre de décision)"):
        fig, ax = plt.subplots(figsize=(10, 6))
        plot_tree(clf, feature_names=['Prix (FCFA)', 'Qualité Route', 'Rendement'], 
                  class_names=['Perte', 'Gain'], filled=True, ax=ax)
        st.pyplot(fig)

def module_3_logistique():
    st.title("Module 3 : Optimisation de la Logistique Urbaine 🛵")
    st.write("### Contexte : JijiExpress (Livraison par Moto-Taxi)")
    st.info("Optimisation de la répartition de la flotte de motos entre Centre-Ville (embouteillages) et Banlieue.")

    # Paramètres
    st.sidebar.header("Contraintes")
    total_motos = st.sidebar.number_input("Taille de la flotte totale", 10, 200, 50)
    
    # Données du problème
    quartiers = ["Centre-Ville", "Banlieue_Nord", "Zone_Industrielle"]
    temps_trajet = {"Centre-Ville": 45, "Banlieue_Nord": 30, "Zone_Industrielle": 20} # minutes par livraison
    demande_min = {"Centre-Ville": 10, "Banlieue_Nord": 5, "Zone_Industrielle": 15} # Demandes minimales

    # Résolution avec PuLP
    prob = LpProblem("Optimisation_Flotte_Tropicale", LpMinimize)
    motos_vars = LpVariable.dicts("Motos", quartiers, 0, None, LpInteger)

    # Fonction Objectif : Minimiser le temps total passé sur la route
    prob += lpSum([motos_vars[q] * temps_trajet[q] for q in quartiers])

    # Contraintes
    prob += lpSum([motos_vars[q] for q in quartiers]) <= total_motos, "Taille_Flotte"
    for q in quartiers:
        prob += motos_vars[q] >= demande_min[q], f"Demande_Min_{q}"

    prob.solve()

    # Affichage des résultats
    st.write("#### 📍 Allocation Optimale des Motos")
    results = []
    for q in quartiers:
        count = int(motos_vars[q].value())
        results.append({"Quartier": q, "Motos Allouées": count, "Temps Estimé (min)": count * temps_trajet[q]})
    
    df_results = pd.DataFrame(results)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.dataframe(df_results, hide_index=True)
    with col2:
        st.metric("⏱️ Temps Total Optimisé", f"{int(value(prob.objective))} min")

    fig = px.pie(df_results, values='Motos Allouées', names='Quartier', title='Répartition de la Flotte')
    st.plotly_chart(fig, use_container_width=True)

def module_4_dashboard():
    st.title("Module 4 : Tableau de Bord Commercial & Mobile Money 📱")
    st.write("### Contexte : MarchéPlus (Grande Distribution)")
    
    # Données simulées
    data = pd.DataFrame({
        'Region': ['Dakar', 'Abidjan', 'Cotonou', 'Dakar', 'Abidjan', 'Cotonou', 'Lomé'] * 10,
        'Produit': ['Riz', 'Smartphone', 'Huile', 'Smartphone', 'Riz', 'Jus', 'Farine'] * 10,
        'Paiement': np.random.choice(['Mobile Money', 'Cash'], 70, p=[0.6, 0.4]), # 60% Mobile Money
        'CA_XOF': np.random.randint(50000, 500000, 70)
    })

    # Filtres
    regions = st.multiselect("Filtrer par Région", data['Region'].unique(), default=data['Region'].unique())
    df_filtered = data[data['Region'].isin(regions)]

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Chiffre d'Affaires Total", f"{df_filtered['CA_XOF'].sum():,} FCFA")
    
    mobile_money_ca = df_filtered[df_filtered['Paiement'] == 'Mobile Money']['CA_XOF'].sum()
    total_ca = df_filtered['CA_XOF'].sum()
    pct_mobile = (mobile_money_ca / total_ca) * 100 if total_ca > 0 else 0
    
    col2.metric("📱 Part Mobile Money", f"{pct_mobile:.1f}%")
    col3.metric("🛒 Nombre de Transactions", f"{len(df_filtered)}")

    # Graphiques
    tab1, tab2 = st.tabs(["Ventes par Produit", "Mode de Paiement"])
    
    with tab1:
        fig_prod = px.bar(df_filtered.groupby('Produit')['CA_XOF'].sum().reset_index(), 
                          x='Produit', y='CA_XOF', color='Produit',
                          title="Performance par Produit")
        st.plotly_chart(fig_prod, use_container_width=True)
        
    with tab2:
        fig_pay = px.pie(df_filtered, names='Paiement', values='CA_XOF', 
                         title="Répartition CA par Mode de Paiement")
        st.plotly_chart(fig_pay, use_container_width=True)

def module_5_strategie():
    st.title("Module 5 : Décision Stratégique & Risque de Change 💱")
    st.write("### Contexte : Investissement Minier / Infrastructure")
    
    st.markdown("""
    Le projet dépend du cours mondial (USD) mais les coûts sont en monnaie locale (FCFA).
    Le risque de change est un facteur critique.
    """)

    # Inputs
    col1, col2 = st.columns(2)
    with col1:
        invest_usd = st.number_input("Investissement Initial (USD)", value=1_000_000, step=100000)
        revenu_annuel_usd = st.number_input("Revenu Annuel Espéré (USD)", value=250_000, step=10000)
    with col2:
        taux_change = st.slider("Taux de change actuel (FCFA/USD)", 500, 1000, 650)
        volatilite = st.slider("Volatilité attendue du taux (%)", 1, 30, 10)
        horizon = st.slider("Durée du projet (Années)", 1, 20, 5)

    if st.button("🎰 Lancer la Simulation de Risque (Monte Carlo)"):
        with st.spinner("Calcul de 10,000 scénarios..."):
            np.random.seed(42)
            simulations = []
            
            for _ in range(10000):
                # Simulation de l'évolution du taux de change année par année
                taux_annees = [taux_change]
                for _ in range(horizon):
                    variation = np.random.normal(0, volatilite / 100)
                    new_taux = taux_annees[-1] * (1 + variation)
                    taux_annees.append(new_taux)
                
                # Calcul du flux financier
                revenus_total_fcfa = sum([revenu_annuel_usd * t for t in taux_annees[1:]])
                invest_fcfa = invest_usd * taux_change
                
                roi = (revenus_total_fcfa - invest_fcfa) / invest_fcfa
                simulations.append(roi)

            # Affichage
            fig = go.Figure()
            fig.add_trace(go.Histogram(x=simulations, nbinsx=50, name="ROI Distribution"))
            st.plotly_chart(fig, use_container_width=True)

            prob_perte = (np.array(simulations) < 0).mean() * 100
            roi_moyen = np.mean(simulations)

            st.write(f"#### Résultats sur {horizon} ans")
            col_res1, col_res2 = st.columns(2)
            col_res1.metric("ROI Moyen Simulé", f"{roi_moyen*100:.1f}%")
            col_res2.metric("Probabilité de Perte", f"{prob_perte:.1f}%")

            if prob_perte > 40:
                st.error("🚨 Projet à Haut Risque. La volatilité du change menace la rentabilité.")
            elif prob_perte > 20:
                st.warning("⚠️ Risque Modéré. Couverture de change recommandée.")
            else:
                st.success("✅ Projet Robuste face aux fluctuations monétaires.")

# --- Navigation Principale ---

def main():
    st.sidebar.title("DataCtrl Tropic Academy 🌴")
    st.sidebar.write("Formation intégrée Contrôle de Gestion & Data Science")
    
    menu = st.sidebar.radio(
        "📚 Choisissez un Module",
        ["Accueil", 
         "1. Prévisions & Saisonnalité", 
         "2. Rentabilité Agricole", 
         "3. Optimisation Logistique", 
         "4. Dashboard Commercial", 
         "5. Risque Stratégique"]
    )

    if menu == "Accueil":
        st.title("Bienvenue dans le Simulateur DataCtrl Tropic 🌍")
        st.image("https://images.unsplash.com/photo-1504639725590-34d0984388bd?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", 
                 caption="Analyse de données en zone tropicale")
        
        st.markdown("""
        Cette application vous permet d'apprendre à intégrer la **Data Science** dans le **Contrôle de Gestion**, 
        adaptée aux réalités économiques de l'Afrique de l'Ouest et des zones tropicales.
        
        ### 🗺️ Parcours Pédagogique :
        1. **Prévisions Budgétaires** : Impact de la saisonnalité et des fêtes religieuses.
        2. **Analyse des Coûts** : Rentabilité agricole et qualité des infrastructures.
        3. **Optimisation** : Gestion de flotte moto et logistique urbaine.
        4. **Visualisation** : Dashboard des ventes et Mobile Money.
        5. **Stratégie** : Investissement et couverture de risque de change.
        
        👈 **Sélectionnez un module dans le menu latéral pour commencer.**
        """)

    elif menu == "1. Prévisions & Saisonnalité":
        module_1_previsions()
    elif menu == "2. Rentabilité Agricole":
        module_2_rentabilite()
    elif menu == "3. Optimisation Logistique":
        module_3_logistique()
    elif menu == "4. Dashboard Commercial":
        module_4_dashboard()
    elif menu == "5. Risque Stratégique":
        module_5_strategie()

if __name__ == "__main__":
    main()
