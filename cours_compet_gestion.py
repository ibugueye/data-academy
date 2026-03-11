import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# ============================================================
# CONFIGURATION GLOBALE
# ============================================================
st.set_page_config(
    page_title="MasterClass : Gestion Augmentée",
    page_icon="🎓",
    layout="wide"
)

# CSS Pédagogique
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Open+Sans:wght@400;600&display=swap');
    
    body { font-family: 'Open Sans', sans-serif; background-color: #ffffff; }
    
    h1 { font-family: 'Merriweather', serif; color: #2c3e50; font-size: 2.5rem; border-bottom: 3px solid #2c3e50; padding-bottom: 15px; }
    h2 { font-family: 'Merriweather', serif; color: #e67e22; margin-top: 40px; }
    h3 { color: #34495e; font-weight: 600; }
    
    .theory-box {
        background-color: #f8f9fa;
        border-left: 5px solid #3498db;
        padding: 20px;
        margin: 20px 0;
        border-radius: 0 10px 10px 0;
    }
    
    .concept-def {
        background-color: #e8f8f5;
        border: 1px solid #1abc9c;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    
    .formula-box {
        background-color: #2c3e50;
        color: white;
        padding: 20px;
        text-align: center;
        font-size: 1.5em;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        margin: 20px 0;
    }
    
    .warning-theory {
        background-color: #fef9e7;
        border-left: 5px solid #f1c40f;
        padding: 15px;
        margin: 15px 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-size: 16px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# NAVIGATION DU COURS
# ============================================================

st.sidebar.title("📚 Sommaire du Cours")
st.sidebar.caption("Théorie & Pratique de la Gestion Augmentée")

modules = [
    "Introduction : Le Paradoxe de la Donnée",
    "Chapitre 1 : Les Fondamentaux de la Gestion Classique",
    "Chapitre 2 : Les Limites Structurelles du Modèle Classique",
    "Chapitre 3 : La Data Science - Fondements Théoriques",
    "Chapitre 4 : Le Contrôle de Gestion Augmenté",
    "Chapitre 5 : La Méthode AMIHARBI (Framework Complet)",
    "Chapitre 6 : Application Pratique & Simulations"
]

choice = st.sidebar.radio("Accès Rapide", modules, index=0)

# ============================================================
# INTRODUCTION
# ============================================================
if choice == modules[0]:
    st.title("Introduction : Le Paradoxe de la Donnée")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Contextualisation Globale</h3>
        Nous vivons une transition historique comparable à l'arrivée de l'électricité. Les entreprises possèdent des masses de données considérables (Big Data), 
        issues de leurs ERP, CRM, et désormais de l'IoT (Internet des Objets) et du Mobile Money.
        <br><br>
        Cependant, une étude de McKinsey (2023) révèle que <b>seulement 12% de ces données sont réellement exploitées</b> pour la prise de décision stratégique.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Le Concept de 'Synergie'")
    st.markdown("""
    La <b>Synergie</b>, dans ce contexte, désigne l'interaction entre l'intelligence humaine (expertise métier, intuition, éthique) 
    et l'intelligence artificielle (vitesse, capacité de calcul, détection de motifs). L'objectif n'est pas de remplacer le gestionnaire, 
    mais de l'<b>augmenter</b>.
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("📊 **Données**\n\nLa matière première. Brute, elle est inutile. Traitée, elle devient information.")
    with col2:
        st.success("🧠 **Intelligence**\n\nLa capacité à extraire du sens et des patrons (patterns) de ces données.")

# ============================================================
# CHAPITRE 1 : GESTION CLASSIQUE
# ============================================================
elif choice == modules[1]:
    st.title("Chapitre 1 : Les Fondamentaux de la Gestion Classique")
    
    st.markdown("### 1.1 Définition et Histoire")
    st.markdown("""
    <div class="concept-def">
        <b>Définition (Anthony, 1965)</b> : Le contrôle de gestion est le processus par lequel les dirigeants s'assurent que les ressources 
        sont obtenues et utilisées de manière efficace et efficiente pour réaliser les objectifs de l'organisation.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Historiquement, ce modèle repose sur trois piliers hérités du XXe siècle :")
    
    # Pilier 1
    st.subheader("A. La Décomposition DuPont (1919)")
    st.write("Première architecture analytique visant à décomposer la performance.")
    st.markdown('<div class="formula-box">ROI = Marge Nette × Rotation des Actifs</div>', unsafe_allow_html=True)
    
    with st.expander("📖 Détail théorique de la formule DuPont"):
        st.markdown("""
        L'intérêt de cette formule multiplicative est de diagnostiquer l'origine de la performance :
        - **Marge Nette** : Efficacité économique (combien je gagne par franc vendu).
        - **Rotation des Actifs** : Efficacité capitalistique (combien je vends par franc investi).
        """)

    # Pilier 2
    st.subheader("B. Le Budget et l'Analyse des Écarts")
    st.markdown("""
    Le budget est la traduction financière des plans d'action annuels. Le travail du contrôleur consiste à comparer le Réel au Budget.
    <br><b>Formule de l'Écart sur Marge :</b>
    """, unsafe_allow_html=True)
    st.markdown('<div class="formula-box">Écart = (Prix Réel - Prix Budget) × Quantité Réelle</div>', unsafe_allow_html=True)

    # Pilier 3
    st.subheader("C. Le Tableau de Bord (Balanced Scorecard - 1992)")
    st.write("Kaplan et Norton introduisent la multidimensionnalité : Financier, Client, Processus Interne, Apprentissage.")

# ============================================================
# CHAPITRE 2 : LIMITES
# ============================================================
elif choice == modules[2]:
    st.title("Chapitre 2 : Les Limites Structurelles du Modèle Classique")
    
    st.markdown("### Théorie de la Latence Informationnelle")
    st.markdown("""
    <div class="warning-theory">
        Le contrôle classique souffre d'un <b>défaut congénital</b> : il est rétrospectif. 
        Il regarde le passé pour piloter le futur, ce qui crée une latence (délai) entre l'événement et la décision.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Les 4 Limites Critiques")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 1. La Tyrannie du Rétroviseur")
        st.write("""
        Reporting mensuel disponible J+15. La décision est prise sur des données vieilles de 45 jours.
        **Coût** : Inadaptation aux chocs rapides (variation cours de change, crise).
        """)
        
        st.markdown("#### 2. La Manualité")
        st.write("60 à 70% du temps passé à collecter/coller des données Excel. Peu de valeur ajoutée analytique.")

    with col2:
        st.markdown("#### 3. La Faible Granularité")
        st.write("Les consolidations masquent les disparités locales. Une moyenne cache souvent des problèmes critiques.")
        
        st.markdown("#### 4. L'Approche Normative")
        st.write("Les outils classiques (Budget) sont rigides et ne s'adaptent pas bien à l'incertitude des marchés volatils (ex: Afrique).")

    # Simulateur de coût de la latence
    st.subheader("Démonstration : Le Coût Économique de la Latence")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        ca_jour = st.number_input("CA Journalier (Millions)", value=500)
    with col2:
        latence = st.slider("Latence Détection (Jours)", 1, 30, 10)
    with col3:
        marge = st.slider("Marge Bénéficiaire (%)", 5, 50, 20)
    
    perte = ca_jour * latence * (marge/100) * 0.1 # Simulation arbitraire de l'impact
    st.metric("Perte potentielle liée à la réactivité lente", f"{perte:,.0f} Millions FCFA", delta="Non récupérable")

# ============================================================
# CHAPITRE 3 : DATA SCIENCE
# ============================================================
elif choice == modules[3]:
    st.title("Chapitre 3 : Fondements Théoriques de la Data Science")
    
    st.markdown("### 3.1 Définition de la Data Science")
    st.markdown("""
    <div class="concept-def">
        Discipline interdisciplinaire qui utilise des méthodes scientifiques, des processus, des algorithmes et des systèmes 
        pour extraire des connaissances et des informations à partir de données structurées et non structurées.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("La Pyramide DIKW (Data - Information - Knowledge - Wisdom)")
    
    # Visualisation de la pyramide
    fig = go.Figure(go.Pie(
        values=[40, 30, 20, 10],
        labels=["Données (Brut)", "Information (Contexte)", "Connaissance (Sens)", "Sagesse (Action)"],
        hole=0.5,
        direction='clockwise',
        sort=False
    ))
    fig.update_traces(textinfo='label', textfont_size=12)
    fig.update_layout(showlegend=False, title="La Pyramide de la Valeur")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("3.2 Les Types d'Analyse")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Descriptive", "Diagnostique", "Prédictive", "Prescriptive"])
    
    with tab1:
        st.markdown('<div class="theory-box">Question : <b>Que s\'est-il passé ?</b><br>Outils : Reporting, BI, Agrégation, Moyennes.</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="theory-box">Question : <b>Pourquoi cela s\'est-il passé ?</b><br>Outils : Drill-down, Analyse de corrélation, Tests d\'hypothèses.</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="theory-box">Question : <b>Que va-t-il se passer ?</b><br>Outils : Machine Learning, Séries temporelles (ARIMA, Prophet), Régression.</div>', unsafe_allow_html=True)
        
    with tab4:
        st.markdown('<div class="theory-box">Question : <b>Que devons-nous faire ?</b><br>Outils : Optimisation, Algorithmes génétiques, IA Générative.</div>', unsafe_allow_html=True)

    st.subheader("3.3 Concepts Statistiques Clés")
    st.write("Pour tout gestionnaire augmenté, maîtriser ces concepts est indispensable :")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Corrélation vs Causalité**")
        st.code("""
# Coefficient de corrélation (Pearson)
r = covariance(X, Y) / (ecart_type_X * ecart_type_Y)
# r va de -1 à 1. r=1 corrélation parfaite.
# ATTENTION : Corrélation ne signifie pas causalité !
        """, language='python')
    
    with col2:
        st.markdown("**Détection d'Anomalies (Outliers)**")
        st.code("""
# Méthode IQR (Interquartile Range)
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
Outlier = (x < Q1 - 1.5*IQR) | (x > Q3 + 1.5*IQR)
        """, language='python')

# ============================================================
# CHAPITRE 4 : GESTION AUGMENTÉE
# ============================================================
elif choice == modules[4]:
    st.title("Chapitre 4 : Le Contrôle de Gestion Augmenté")
    
    st.markdown("""
    <div class="concept-def">
        <h3>Définition</h3>
        Le Contrôle de Gestion Augmenté est l'intégration systémique des capacités analytiques avancées (Data Science, ML, IA) 
        dans les processus de pilotage pour transformer le contrôleur en architecte de la performance.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Les 3 Dimensions de la Transformation")
    
    # Tableau comparatif
    data_dim = pd.DataFrame({
        'Dimension': ['Temporelle', 'Volumétrique', 'Cognitive'],
        'Avant (Classique)': ['Rétrospective (Passé)', 'Échantillonnage', 'Intuition & Expérience'],
        'Après (Augmenté)': ['Prédictive (Futur)', 'Exhaustivité (Big Data)', 'Preuves de données & Algorithmes']
    })
    st.table(data_dim)

    st.subheader("Le Nouveau Profil du Contrôleur : Le 'Data Translator'")
    st.write("Le contrôleur moderne doit être un pont entre la technique et le business.")
    
    # Visualisation compétences
    labels = ['Finance', 'Data Science', 'Business', 'IT', 'Soft Skills']
    values_classique = [9, 1, 7, 3, 6]
    values_augmente = [8, 7, 8, 6, 8]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=values_classique, theta=labels, fill='toself', name='Profil Classique'))
    fig.add_trace(go.Scatterpolar(r=values_augmente, theta=labels, fill='toself', name='Profil Augmenté'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="warning-theory"><b>Point clé :</b> L\'IA ne remplace pas l\'expertise finance, elle l\'amplifie. Le jugement reste humain.</div>', unsafe_allow_html=True)

# ============================================================
# CHAPITRE 5 : MÉTHODE AMIHARBI
# ============================================================
elif choice == modules[5]:
    st.title("Chapitre 5 : La Méthode AMIHARBI - Framework Complet")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Philosophie de la Méthode</h3>
        Née d'un constat de paradoxe africain (abondance de données, pénurie d'analyse), la méthode AMIHARBI propose une architecture progressive 
        pour transformer les données en impact économique.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("L'Équation de la Performance")
    st.markdown('<div class="formula-box">Performance = Données × Intelligence × Décision</div>', unsafe_allow_html=True)
    st.write("Nature multiplicative : si un facteur est nul, la performance est nulle.")

    st.subheader("Architecture en 8 Étapes (Le Pipeline)")
    
    etapes = {
        "A - Acquisition": "Cartographie des sources (ERP, CRM, IoT, Mobile Money). Audit qualité.",
        "M - Modélisation": "Feature Engineering. Transformation de la donnée brute en indicateurs métier.",
        "I - Intelligence": "Exploration (EDA). Visualisation. Compréhension des patrons.",
        "H - Hybridation": "Couplage Intelligence Humaine + Machine. Validation des hypothèses.",
        "A - Analyse Prédictive": "Utilisation de modèles (ML) pour anticiper (Forecast, Churn).",
        "R - Recommandations": "Passage de l'alerte à la suggestion d'action (Prescriptif).",
        "B - Business Decision": "Intégration dans le processus décisionnel (Committees, Dashboards).",
        "I - Impact": "Mesure du ROI analytique. Combien de valeur a été créée par la donnée ?"
    }
    
    # Affichage dynamique des étapes
    cols = st.columns(2)
    for i, (nom, desc) in enumerate(etapes.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div style="border:1px solid #eee; padding:15px; border-radius:10px; margin-bottom:10px; background-color:#fff;">
                <h4>{nom}</h4>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# ============================================================
# CHAPITRE 6 : APPLICATION
# ============================================================
elif choice == modules[6]:
    st.title("Chapitre 6 : Application Pratique & Simulations")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Cas Pratique : Optimisation du BFR</h3>
        Scénario : Une entreprise africaine de distribution veut améliorer sa trésorerie en optimisant ses délais de paiement clients 
        grâce à l'analyse de données.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("1. Simulation de Prévision de Trésorerie")
    
    # Génération données
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=90, freq='D')
    treso = 500000 + np.cumsum(np.random.randn(90) * 20000)
    df = pd.DataFrame({'Date': dates, 'Trésorerie Réelle': treso})
    
    # Prévision simple (Moyenne mobile) vs ML (Simulé)
    df['Prévision Classique'] = df['Trésorerie Réelle'].rolling(7).mean().shift(1)
    df['Prévision ML'] = df['Trésorerie Réelle'] * 0.95 + np.random.rand(90) * 10000 # Simulé
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Trésorerie Réelle'], name='Réel', mode='lines'))
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Prévision ML'], name='Prévision ML', line=dict(dash='dot', color='red')))
        fig.update_layout(title="Courbe de Trésorerie : Prédictive vs Réelle")
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.metric("Gain de Précision (ML)", "+15%", delta="vs Méthode Classique")
        st.info("Le modèle ML détecte des cycles invisibles à l'œil nu (saisonnalité, jours de marché).")

    st.subheader("2. Analyse de Cohorte (Retention Client)")
    st.write("Comprendre quelles cohortes de clients (par mois d'acquisition) génèrent le plus de valeur.")
    
    # Heatmap simulée
    cohort_data = np.random.randint(100, 1000, size=(5, 5))
    cohort_data = np.triu(cohort_data) # Rendre triangulaire
    df_cohort = pd.DataFrame(cohort_data, columns=['M+1', 'M+2', 'M+3', 'M+4', 'M+5'],
                             index=['Janv', 'Fév', 'Mar', 'Avr', 'Mai'])
    
    fig = px.imshow(df_cohort, text_auto=True, title="Rétention Client par Cohorte (Data Science)", color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)
    
    st.code("""
# Code Python pour créer une analyse de cohorte réelle
import pandas as pd
# 1. Acquisition : Charger les transactions
df = pd.read_csv('transactions.csv')

# 2. Modélisation : Créer les variables
df['OrderPeriod'] = df['OrderDate'].dt.to_period('M')
df['CohortGroup'] = df.groupby('UserId')['OrderDate'].transform('min').dt.to_period('M')

# 3. Intelligence : Grouper et compter
grouped = df.groupby(['CohortGroup', 'OrderPeriod'])
cohorts = grouped.agg({'UserId': pd.Series.nunique})
    """, language='python')

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <b>FIN DU COURS THÉORIQUE</b><br>
    Ce contenu est basé sur la méthode AMIHARBI et le guide pratique de la Gestion Augmentée.<br>
    <i>© 2024 - Tous droits réservés.</i>
</div>
""", unsafe_allow_html=True)