
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ============================================================
# CONFIGURATION GLOBALE
# ============================================================
st.set_page_config(
    page_title="Académie Data & Gestion",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS pour un design moderne et "Vulgarisation"
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&display=swap');
    
    body { font-family: 'Montserrat', sans-serif; background-color: #f4f7f6; }
    
    h1 { color: #2c3e50; font-weight: 800; }
    h2 { color: #e67e22; border-bottom: 3px solid #e67e22; padding-bottom: 10px; }
    h3 { color: #34495e; }
    
    /* Cartes de concept */
    .concept-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #3498db;
    }
    
    /* Focus Afrique */
    .africa-card {
        background: #fff8e1;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff9800;
        margin: 10px 0;
    }

    /* Définition simple */
    .definition {
        background-color: #e8f6f3;
        padding: 15px;
        border-radius: 10px;
        color: #16a085;
        font-weight: 600;
        text-align: center;
        margin: 10px 0;
    }

    /* Séparateur visuel */
    .separator { height: 2px; background: #eee; margin: 30px 0; }
    
    /* Styliser les métriques */
    .stMetric label { font-size: 18px; color: #7f8c8d; }
    .stMetric value { font-size: 28px; color: #2c3e50; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# NAVIGATION PRINCIPALE
# ============================================================

st.sidebar.title("🏫 Académie de la Performance")
st.sidebar.caption("Vulgarisation Data Science & Gestion")

modules = {
    "🏠 Accueil & Parcours": 0,
    "📚 Module 1 : Culture Gestion (Les Bases)": 1,
    "📊 Module 2 : Culture Data (Vulgarisation)": 2,
    "🔗 Module 3 : La Synergie (Contrôle Augmenté)": 3,
    "🛠️ Module 4 : Outils & Démonstrations": 4,
    "🌍 Module 5 : Focus Réalités Africaines": 5,
    "🎓 Certification & Quizz": 6
}

# Système de progression (simplifié)
if 'progress' not in st.session_state:
    st.session_state.progress = 0

choice = st.sidebar.radio("Choisissez votre module", list(modules.keys()), index=0)
current_module = modules[choice]

# Affichage de la progression
st.sidebar.progress(current_module / (len(modules)-1))
st.sidebar.info(f"Progression globale : {int((current_module / (len(modules)-1))*100)}%")

# ============================================================
# MODULE 0 : ACCUEIL
# ============================================================
if current_module == 0:
    st.title("Bienvenue à l'Académie de la Performance Augmentée")
    st.subheader("Apprendre à piloter avec la donnée, sans être mathématicien.")
    
    st.markdown("""
    <div class="definition">
        "L'intelligence sans données est spéculation. Les données sans intelligence sont du bruit."
        — Ami Arbi
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🎯 **Objectif**\n\nComprendre comment la Data Science transforme la gestion d'entreprise.")
    with col2:
        st.success("🚀 **Prérequis**\n\nAucun. Ce cours est fait pour la vulgarisation.")
    with col3:
        st.warning("⏱️ **Durée**\n\nEnviron 45 minutes de lecture interactive.")

    st.markdown("---")
    st.markdown("### 🗺️ Votre Parcours Pédagogique")
    
    st.write("""
    Ce cours interactif est divisé en 5 modules logiques pour vous emmener du monde de la **Gestion Classique** 
    vers le monde de la **Data Science Augmentée**.
    """)
    
    # Visualisation du parcours
    steps = ["Gestion Classique", "Limites & Besoins", "Découverte Data", "Hybridation", "Performance"]
    for i, step in enumerate(steps):
        cols = st.columns(5)
        cols[i].metric(step, f"Étape {i+1}")

# ============================================================
# MODULE 1 : CULTURE GESTION
# ============================================================
elif current_module == 1:
    st.title("📚 Module 1 : Les Concepts Fondamentaux de la Gestion")
    st.markdown("*Avant de parler data, comprenons ce que l'on cherche à piloter.*")
    
    # Concept 1 : Le ROI
    st.markdown('<div class="concept-card">', unsafe_allow_html=True)
    st.subheader("1. Le ROI (Return on Investment)")
    st.markdown("""
    **En gestion simple :** Est-ce que l'argent que j'ai investi me rapporte plus que si je l'avais laissé en banque ?
    """)
    
    # Simulateur ROI
    col1, col2 = st.columns(2)
    with col1:
        invest = st.number_input("Investissement initial (FCFA)", value=1000000)
        gain = st.number_input("Gain réalisé après 1 an (FCFA)", value=1200000)
    with col2:
        roi = ((gain - invest) / invest) * 100
        st.metric("Votre ROI", f"{roi:.1f}%", delta="Bénéfice" if roi > 0 else "Perte")
        if roi > 10:
            st.success("Excellent investissement !")
        elif roi > 0:
            st.warning("Investissement rentable mais faible.")
        else:
            st.error("Mauvais investissement.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Concept 2 : Marge & Coût
    st.markdown('<div class="concept-card">', unsafe_allow_html=True)
    st.subheader("2. Marge et Coûts")
    st.write("La **Marge** est ce qu'il reste dans la poche après avoir payé les coûts.")
    
    # Démonstration visuelle
    ca = 100
    cout_achat = 40
    cout_transport = 20
    marge = ca - cout_achat - cout_transport
    
    fig = go.Figure(data=[go.Waterfall(
        name = "Cashflow",
        orientation = "v",
        measure = ["relative", "relative", "relative", "total"],
        x = ["Chiffre d'Affaires", "Coût Achat", "Coût Transport", "Marge Nette"],
        textposition = "outside",
        y = [ca, -cout_achat, -cout_transport, 0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    )])
    fig.update_layout(title="Cascade de la Valeur", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Concept 3 : Budget vs Réel
    st.markdown('<div class="concept-card">', unsafe_allow_html=True)
    st.subheader("3. Analyse des Écarts (Budget vs Réel)")
    st.write("""
    Le cœur du contrôle de gestion classique : comparer ce que l'on avait prévu à ce qui s'est vraiment passé.
    """)
    
    data_ecart = pd.DataFrame({
        'Mois': ['Jan', 'Fév', 'Mar'],
        'Budget': [100, 120, 150],
        'Réel': [90, 130, 140]
    })
    data_ecart['Écart'] = data_ecart['Réel'] - data_ecart['Budget']
    
    col1, col2 = st.columns([2,1])
    with col1:
        fig = px.bar(data_ecart, x='Mois', y=['Budget', 'Réel'], barmode='group', 
                     title="Comparaison Budget vs Réel", color_discrete_map={'Budget': '#bdc3c7', 'Réel': '#2ecc71'})
        st.plotly_chart(fig)
    with col2:
        st.dataframe(data_ecart.style.applymap(
            lambda x: 'color: red' if x < 0 else 'color: green', subset=['Écart']
        ))
        st.info("L'écart négatif = Mauvaise nouvelle (Sous-performance).")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# MODULE 2 : CULTURE DATA
# ============================================================
elif current_module == 2:
    st.title("📊 Module 2 : Comprendre la Data Science (Sans maths complexes)")
    st.markdown("*Démystifier les termes : Big Data, Machine Learning, Algorithme.*")
    
    # Concept 1 : Data vs Information
    st.markdown('<div class="concept-card">', unsafe_allow_html=True)
    st.subheader("1. Donnée vs Information")
    
    cols = st.columns(3)
    with cols[0]:
        st.write("**Donnée brute**")
        st.code("25°C")
        st.caption("Un chiffre seul ne veut rien dire.")
    with cols[1]:
        st.write("**Contexte**")
        st.code("Température extérieure à Dakar, 14h")
        st.caption("On ajoute du sens.")
    with cols[2]:
        st.write("**Information / Insight**")
        st.code("Il fait chaud, potentiel de vente de boissons : +20%")
        st.caption("Decision possible !")
    st.markdown('</div>', unsafe_allow_html=True)

    # Concept 2 : Les 3 types d'analyse
    st.subheader("2. Les 3 Niveaux d'Intelligence")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("⏪ **Descriptif**")
        st.write("**Question :** Que s'est-il passé ?")
        st.write("**Outil :** Reporting, Tableau de bord.")
        st.write("**Exemple :** Les ventes ont baissé de 5%.")
        st.progress(33)
        
    with col2:
        st.warning("⏳ **Prédictif**")
        st.write("**Question :** Que va-t-il se passer ?")
        st.write("**Outil :** Machine Learning (Prévision).")
        st.write("**Exemple :** Les ventes vont baisser de 8% le mois prochain.")
        st.progress(66)
        
    with col3:
        st.success("🚀 **Prescriptif**")
        st.write("**Question :** Que dois-je faire ?")
        st.write("**Outil :** Optimisation, IA.")
        st.write("**Exemple :** Augmentez le stock de glaces de 10%.")
        st.progress(100)

    # Concept 3 : C'est quoi le Machine Learning ?
    st.markdown('<div class="concept-card">', unsafe_allow_html=True)
    st.subheader("3. Le Machine Learning vulgarisé")
    st.markdown("""
    <div class="definition">
        Le Machine Learning (Apprentissage Automatique), c'est apprendre à un ordinateur à reconnaître des motifs (patterns) 
        grâce à des exemples, sans lui donner de règles strictes.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("**Exemple simple : Risque de Chômage**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Approche Classique (Règles humaines)**")
        st.code("""
SI salaire < 50k ET dette > 20k
ALORS Risque = OUI
SINON Risque = NON
        """)
        st.error("Limites : Si salaire = 60k mais dette = 80k ? La règle échoue.")
        
    with col2:
        st.write("**Approche Machine Learning**")
        st.code("""
On montre 10 000 dossiers passés :
- 5000 qui ont bien payé
- 5000 qui ont fait défaut

L'IA trouve la frontière optimale seule.
        """)
        st.success("L'IA détecte des nuances invisibles à l'œil nu.")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# MODULE 3 : LA SYNERGIE
# ============================================================
elif current_module == 3:
    st.title("🔗 Module 3 : Le Contrôle de Gestion Augmenté")
    st.markdown("*Quand la Gestion rencontre la Data Science.*")
    
    st.markdown("""
    <div class="definition">
        <h3>L'Équation AMIHARBI</h3>
        Performance = Données × Intelligence × Décision
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Les 4 Piliers de la Transformation")
    
    tabs = st.tabs(["1. Temporel", "2. Volumétrique", "3. Prédictif", "4. Prescriptif"])
    
    with tabs[0]:
        st.write("### Du retard à l'instantané")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Contrôle Classique", "J+30", delta="Reporting mensuel", delta_color="inverse")
        with col2:
            st.metric("Contrôle Augmenté", "Temps Réel", delta="Monitoring continu")
        st.write("Passer d'un pilotage au rétroviseur à un pilotage sur le pare-brise.")
        
    with tabs[1]:
        st.write("### De l'échantillon à l'exhaustivité")
        st.write("Aujourd'hui, nous pouvons analyser **toutes** les transactions, pas juste un échantillon.")
        st.info("Exemple : Analyser 1 million de tickets de caisse en 2 secondes pour trouver le produit 'pivot'.")
        
    with tabs[2]:
        st.write("### Anticiper au lieu de constater")
        # Simulateur simple
        st.write("Prévision des ventes :")
        mois = ['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Juin']
        reel = [10, 12, 14, 13, 16, 18]
        prev = [11, 11.5, 13, 15, 17, 19]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mois, y=reel, name='Réel', mode='lines+markers'))
        fig.add_trace(go.Scatter(x=mois, y=prev, name='Prévision IA', line=dict(dash='dot')))
        st.plotly_chart(fig, use_container_width=True)
        
    with tabs[3]:
        st.write("### Recommander au lieu d'alerter")
        st.write("Le système ne dit plus 'Attention problème', mais 'Voici la solution'.")
        st.markdown("""
        **Exemple Gestion de Stock :**
        - *Classique :* "Stock bas (Alerte Rouge)"
        - *Augmenté :* "Commander 450 unités du produit X au fournisseur Y pour optimiser le coût de transport."
        """)

# ============================================================
# MODULE 4 : OUTILS
# ============================================================
elif current_module == 4:
    st.title("🛠️ Module 4 : Atelier Pratique & Outils")
    st.markdown("*Voir la data en action.*")
    
    st.subheader("Démonstration : Analyse Client (RFM)")
    st.write("""
    La méthode RFM (Récence, Fréquence, Montant) est un classique de la gestion client 
    que la Data Science rend automatisable et dynamique.
    """)
    
    # Génération données
    np.random.seed(42)
    n = 100
    data = pd.DataFrame({
        'Client': [f'C{i}' for i in range(n)],
        'Recence_jours': np.random.randint(5, 365, n),
        'Frequence_achats': np.random.randint(1, 20, n),
        'Montant_total': np.random.uniform(50000, 500000, n)
    })
    
    # Segmentation simple pour la démo
    def segmenter(row):
        if row['Recence_jours'] < 30 and row['Montant_total'] > 300000:
            return 'VIP'
        elif row['Recence_jours'] > 300:
            return 'Perdu'
        else:
            return 'Standard'
    
    data['Segment'] = data.apply(segmenter, axis=1)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        fig = px.scatter(data, x='Recence_jours', y='Montant_total', 
                         color='Segment', size='Frequence_achats',
                         title="Cartographie des Clients",
                         labels={'Recence_jours': "Dernier achat (jours)", 'Montant_total': "CA Total"},
                         hover_data=['Client'])
        fig.add_vline(x=30, line_dash="dash", line_color="green", annotation_text="Récence < 30j")
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.write("**Répartition**")
        st.dataframe(data['Segment'].value_counts())
        
        st.markdown("---")
        st.write("**Action recommandée**")
        st.info("Envoyer un coupon de réduction aux clients 'Perdu'.")

    # Code Snippet
    st.subheader("Le code derrière l'analyse")
    st.code("""
# En Python, cela se fait en quelques lignes
import pandas as pd

# Calcul du score RFM
data['Score_R'] = pd.qcut(data['Recence'], 4, labels=[4, 3, 2, 1])
data['Score_F'] = pd.qcut(data['Frequence'], 4, labels=[1, 2, 3, 4])
data['Score_M'] = pd.qcut(data['Montant'], 4, labels=[1, 2, 3, 4])

data['Score_RFM'] = data['Score_R'].astype(str) + data['Score_F'].astype(str) + data['Score_M'].astype(str)
    """, language='python')

# ============================================================
# MODULE 5 : FOCUS AFRIQUE
# ============================================================
elif current_module == 5:
    st.title("🌍 Module 5 : Adaptation aux Réalités Africaines")
    
    st.markdown("""
    <div class="africa-card">
        <h3>Le contexte spécifique</h3>
        La transformation digitale en Afrique présente des défis uniques mais aussi des opportunités immenses (Leapfrog).
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Les Défis Data en Afrique")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("⚠️ **Les Freins**")
        st.write("""
        1. **Données informelles** : Beaucoup d'activités ne passent pas par les canaux bancaires classiques.
        2. **Qualité des données** : Doublons, données manquantes dans les ERP anciens.
        3. **Infrastructure** : Coupures d'électricité / internet instables.
        """)
        
    with col2:
        st.success("🚀 **Les Leviers**")
        st.write("""
        1. **Mobile Money** : Explosion des données financières (M-Pesa, Orange Money) qui remplacent les relevés bancaires.
        2. **Cloud** : Possibilité de sauter les étapes d'infrastructure lourde.
        3. **Jeunesse** : Population jeune et connectée, facilitant l'adoption des outils.
        """)
        
    st.subheader("Cas d'usage : Le Scoring Crédit via Mobile Money")
    st.write("""
    Dans beaucoup de pays africains, les PME et particuliers ont peu d'historique bancaire (Ficher Bancaire).
    La méthode AMIHARBI propose d'utiliser les données alternatives.
    """)
    
    # Simulateur de crédit
    st.markdown("**Simulateur de Score Crédit Alternatif**")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        solde_moyen = st.slider("Solde moyen Mobile Money (FCFA)", 0, 1000000, 150000)
    with col2:
        regularite = st.slider("Régularité des recharges (%)", 0, 100, 80)
    with col3:
        duree = st.slider("Ancienneté compte (mois)", 1, 60, 12)
        
    # Algo simple
    score = (solde_moyen/10000) + (regularite * 0.5) + (duree * 1.5)
    
    st.metric("Score de Fiabilité Estimé", f"{score:.0f} / 100")
    
    if score > 60:
        st.success("✅ Crédit Accordé (Risque Faible)")
    elif score > 40:
        st.warning("⚡ Crédit avec Caution (Risque Moyen)")
    else:
        st.error("🚫 Crédit Refusé (Risque Élevé)")

# ============================================================
# MODULE 6 : CERTIFICATION
# ============================================================
elif current_module == 6:
    st.title("🎓 Validation des Acquis")
    
    st.subheader("Quizz Rapide")
    
    q1 = st.radio("1. Quelle est la différence principale entre le contrôle classique et augmenté ?", 
                  ["Le coût des outils", "Le passage du rétrospectif au prédictif", "L'utilisation du papier"])
    
    q2 = st.radio("2. Que signifie 'Machine Learning' pour un gestionnaire ?", 
                  ["Un robot qui remplace le gestionnaire", "Un outil qui apprend des données passées pour prédire l'avenir", "Un logiciel de comptabilité"])
    
    q3 = st.radio("3. Dans le contexte africain, quelle donnée est stratégique pour le scoring crédit ?", 
                  ["Le fichier bancaire classique", "L'historique Mobile Money", "La taille de l'entreprise"])
    
    if st.button("Vérifier mes réponses"):
        score = 0
        if q1 == "Le passage du rétrospectif au prédictif":
            score += 1
        if q2 == "Un outil qui apprend des données passées pour prédire l'avenir":
            score += 1
        if q3 == "L'historique Mobile Money":
            score += 1
            
        st.markdown("---")
        if score == 3:
            st.success(f"🏆 Excellent ! Score : 3/3. Vous maîtrisez les concepts de la Gestion Augmentée !")
            st.balloons()
        elif score >= 2:
            st.warning(f"📝 Bon travail ! Score : {score}/3. Quelques révisions conseillées.")
        else:
            st.error(f"📉 Score : {score}/3. Reprenez les modules 1 et 2.")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; opacity: 0.6;">
    <small>© 2024 - Programme de vulgarisation basé sur la Méthode AMIHARBI | Synergie Data & Gestion</small>
</div>
""", unsafe_allow_html=True)
