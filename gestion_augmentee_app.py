import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime

# ============================================================
# CONFIGURATION & DESIGN
# ============================================================
st.set_page_config(
    page_title="Guide Pratique : Gestion Augmentée",
    page_icon="📈",
    layout="wide"
)

# CSS Personnalisé pour un style "Livre Pratique"
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap');
    body { font-family: 'Lato', sans-serif; background-color: #f9fafb; }
    
    h1 { color: #0f172a; font-weight: 700; border-bottom: 2px solid #3b82f6; padding-bottom: 10px; }
    h2 { color: #1e40af; font-weight: 600; }
    h3 { color: #334155; }
    
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
        border-top: 4px solid #3b82f6;
    }
    
    .ia-card {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-left: 5px solid #0ea5e9;
        padding: 20px;
        border-radius: 8px;
        margin: 10px 0;
    }

    .warning-box {
        background-color: #fffbeb;
        border-left: 5px solid #f59e0b;
        padding: 15px;
        margin: 10px 0;
    }
    
    .stMetric > label { font-size: 16px; color: #64748b; font-weight: bold; }
    .stMetric > value { font-size: 24px; color: #0f172a; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# NAVIGATION (Menu Principal)
# ============================================================

st.sidebar.title("📊 Guide de la Gestion Augmentée")
st.sidebar.caption("Basé sur les frameworks AMIHARBI & IA")

sections = [
    "🏠 1. Introduction : La Révolution de la Gestion",
    "📐 2. Le Cadre : Contrôle Classique vs Augmenté",
    "🛠️ 3. Outils : La Boîte à Outils Data-Driven",
    "🔬 4. Laboratoire de Stratégie (Simulateur)",
    "🌍 5. Implémentation & Réalités Africaines"
]

choice = st.sidebar.radio("Parcours du Guide", sections)

# ============================================================
# SECTION 1 : INTRODUCTION
# ============================================================
if choice == sections[0]:
    st.title("La Révolution de la Gestion Augmentée")
    st.markdown("*Quand l'intelligence artificielle rencontre le pilotage d'entreprise.*")
    
    st.markdown("""
    <div class="card">
        <h3>📝 Définition Fondamentale</h3>
        La <b>Gestion Augmentée</b> ne remplace pas le gestionnaire. Elle l'augmente en déléguant à l'IA les tâches de 
        calcul, de surveillance et de prédiction, libérant ainsi l'humain pour la décision stratégique.
        <br><br>
        <i>"Il y aura ceux qui auront fait le choix de l'électricité et ceux qui seront restés à la vapeur."</i>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Le Paradoxe Actuel")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Données Disponibles", "Explosion +500%", delta="Big Data, IoT, Mobile")
        st.error("⚠️ **Sous-exploitation**\n\nSeulement 12% des données sont réellement analysées pour la décision.")
        
    with col2:
        st.metric("Capacité Analytique", "Rareté", delta_color="inverse")
        st.success("💡 **L'Opportunité**\n\nLes outils modernes (No-Code, AI) démocratisent l'accès à l'intelligence.")

    st.markdown("---")
    st.markdown("### Les 3 Dimensions de l'Augmentation")
    
    cols = st.columns(3)
    dims = [
        ("⏪ Temporelle", "Passé → Futur", "Passer du 'Que s'est-il passé ?' au 'Que va-t-il se passer ?'."),
        ("📐 Volumétrique", "Échantillon → Totalité", "Analyser 100% des transactions au lieu d'extrapolations."),
        ("🎯 Prescription", "Constat → Action", "L'IA suggère l'action optimale, l'humain valide.")
    ]
    
    for i, col in enumerate(cols):
        col.metric(dims[i][0], dims[i][1])
        col.info(dims[i][2])

# ============================================================
# SECTION 2 : LE CADRE
# ============================================================
elif choice == sections[1]:
    st.title("Le Cadre : Du Traditionnel à l'Augmenté")
    
    st.markdown("""
    <div class="ia-card">
        <h3>Le Modèle AMIHARBI : L'Équation de la Performance</h3>
        <h2 style="text-align:center; color:#0f172a;">Performance = Données × Intelligence × Décision</h2>
    </div>
    """, unsafe_allow_html=True)

    # Comparatif
    st.subheader("Comparatif des Approches")
    
    df_compare = pd.DataFrame({
        'Critère': ['Temporalité', 'Source de Vérité', 'Processus Décisionnel', 'Format Sortie', 'Rôle du Gestionnaire'],
        'Gestion Classique': ['Rétrospective (Mensuel)', 'Comptabilité Générale', 'Top-down (Intuition)', 'Excel / PDF', 'Producteur de rapports'],
        'Gestion Augmentée': ['Temps Réel / Prédictive', 'Data Lake (ERP+CRM+IoT)', 'Data-driven (Preuves)', 'Dashboards Interactifs', 'Architecte de la performance']
    })
    
    st.table(df_compare)

    # Démonstration des limites
    st.subheader("⚠️ Les Limites du Modèle Classique (Exemple Chiffré)")
    st.write("Le coût caché de la latence informationnelle.")
    
    with st.expander("🔬 Simulateur de Latence", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            ca_jour = st.number_input("CA Journalier (M FCFA)", value=500)
            variation_prix = st.slider("Choc prix marché (%)", -30, 0, -15)
        
        with col2:
            latence_jours = st.slider("Délai de détection (Jours)", 1, 30, 15)
            marge_base = st.slider("Marge de base (%)", 5, 40, 20)
        
        with col3:
            impact_latence = (ca_jour * latence_jours) * (abs(variation_prix)/100) * (marge_base/100)
            st.metric("Perte évitable", f"{impact_latence:,.0f} M FCFA", delta_color="inverse")
            
            if latence_jours > 7:
                st.error("Système trop lent pour réagir aux chocs.")
            else:
                st.success("Réactivité acceptable.")

# ============================================================
# SECTION 3 : OUTILS
# ============================================================
elif choice == sections[2]:
    st.title("La Boîte à Outils Data-Driven")
    st.markdown("*Les briques technologiques pour passer à l'acte.*")
    
    st.subheader("1. Le Pipeline Analytique")
    
    etapes = ["Acquisition (A)", "Nettoyage (M)", "Analyse (I)", "Modélisation (A)", "Décision (R)"]
    for i, etape in enumerate(etapes):
        cols = st.columns(5)
        cols[i].markdown(f"""
        <div style="text-align:center; background:#f1f5f9; padding:10px; border-radius:10px; border:1px solid #cbd5e1;">
            <h4>{etape.split(' (')[0]}</h4>
            <small>{etape.split('(')[1][:-1]}</small>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Focus sur les algos
    st.subheader("2. Algorithmes Clés pour la Gestion")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Prévision (Forecast)", "👥 Segmentation", "🚨 Détection Anomalies", "🤖 Génération de Rapports"])

    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**Objectif :** Anticiper la trésorerie ou les ventes.")
        st.code("""
# Exemple simplifié avec Python (Prophet)
from prophet import Prophet
df = pd.read_csv("ventes.csv")
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)
        """, language='python')
        st.info("Remplace les moyennes mobiles manuelles par des modèles capables de gérer la saisonnalité.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**Objectif :** Cibler les clients à risque (Churn) ou les clients VIP.")
        st.code("""
# Classification K-Means
from sklearn.cluster import KMeans
# Segmentation RFM (Récence, Fréquence, Montant)
kmeans = KMeans(n_clusters=4)
clients["groupe"] = kmeans.fit_predict(clients[["recence", "frequence", "montant"]])
        """, language='python')
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**Objectif :** Détecter la fraude ou les erreurs de saisie automatiquement.")
        st.write("Méthode des écarts interquartiles (IQR) ou Isolation Forest.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="ia-card">', unsafe_allow_html=True)
        st.write("**Objectif :** Automatiser la rédaction des commentaires de gestion (IA Générative).")
        st.code("""
# Exemple avec OpenAI / LLM
prompt = f"Analyse cette variance budget vs reel : {ecart}. Propose une action corrective."
response = llm.generate(prompt)
        """, language='python')
        st.write("Gagne des heures sur la rédaction des reportings mensuels.")
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# SECTION 4 : LABORATOIRE
# ============================================================
elif choice == sections[3]:
    st.title("🔬 Laboratoire de Stratégie Augmentée")
    st.markdown("*Testez l'impact de la Data Science sur vos décisions.*")
    
    st.markdown("""
    <div class="warning-box">
        <b>Scénario</b> : Vous êtes DAF d'un groupe de distribution. Vous devez décider d'une stratégie de stock pour le mois prochain.
    </div>
    """, unsafe_allow_html=True)

    # Génération de données fictives
    np.random.seed(42)
    date_range = pd.date_range(start="2023-01-01", periods=180, freq='D')
    ventes = 500 + np.cumsum(np.random.randn(180) * 10) + np.sin(np.arange(180)/30) * 50
    df = pd.DataFrame({'Date': date_range, 'Ventes_Réelles': ventes})
    
    # Simuler une prévision "Classique" vs "Augmentée"
    df['Méthode Classique (Moyenne Mobile)'] = df['Ventes_Réelles'].rolling(30).mean().shift(1)
    
    # Simuler une prévision ML (plus précise pour la démo)
    df['Méthode Augmentée (ML)'] = df['Ventes_Réelles'] * 0.98 + np.random.randn(180) * 5

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Évolution des Ventes & Prévisions")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Ventes_Réelles'], name='Réel', mode='lines', opacity=0.5))
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Méthode Classique (Moyenne Mobile)'], name='Classique', line=dict(color='orange', dash='dot')))
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Méthode Augmentée (ML)'], name='Augmentée (ML)', line=dict(color='green')))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Analyse des Erreurs de Prévision")
        
        # Calcul MAPE
        df['Erreur_Classique'] = abs((df['Ventes_Réelles'] - df['Méthode Classique (Moyenne Mobile)']) / df['Ventes_Réelles'])
        df['Erreur_Augmentee'] = abs((df['Ventes_Réelles'] - df['Méthode Augmentée (ML)']) / df['Ventes_Réelles'])
        
        mape_classique = df['Erreur_Classique'].mean() * 100
        mape_augmentee = df['Erreur_Augmentee'].mean() * 100
        
        delta_mape = mape_classique - mape_augmentee
        
        col_a, col_b = st.columns(2)
        col_a.metric("Erreur Classique (MAPE)", f"{mape_classique:.1f}%")
        col_b.metric("Erreur Augmentée (MAPE)", f"{mape_augmentee:.1f}%", f"-{delta_mape:.1f}%")
        
        st.info("L'approche augmentée réduit l'incertitude, permettant une gestion de stock plus fine (moins de ruptures, moins de sur-stocks).")

# ============================================================
# SECTION 5 : IMPLÉMENTATION
# ============================================================
elif choice == sections[4]:
    st.title("Implémentation & Réalités Africaines")
    
    st.subheader("Les Défis Spécifiques")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>🚧 Les Freins</h3>
            <ul>
                <li><b>Secteur Informel</b> : Données non structurées (Cash).</li>
                <li><b>Infrastructure</b> : Accès électrique/internet instable.</li>
                <li><b>Talents</b> : Pénurie de Data Scientists.</li>
                <li><b>Silos</b> : La finance ne parle pas au marketing.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card" style="border-top-color: #10b981;">
            <h3>🚀 Les Leviers AMIHARBI</h3>
            <ul>
                <li><b>Mobile Money</b> : Source de données alternatives majeure.</li>
                <li><b>Cloud</b> : Sauter l'étape des serveurs physiques.</li>
                <li><b>No-Code</b> : Démocratiser l'analyse sans coder.</li>
                <li><b>Hybridation</b> : Mixer expertise locale + outils digitaux.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Cas Pratique : Scoring Crédit PME")
    st.write("""
    Comment prêter à une PME qui ne tient pas de comptabilité formelle ?
    La méthode AMIHARBI propose d'utiliser des **proxies analytiques**.
    """)
    
    with st.form("scoring_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            flux_mobile = st.number_input("Flux Mobile Money Mensuel (FCFA)", value=2000000)
        with col2:
            recharge_freq = st.slider("Fréquence Recharge Réseau (Mois)", 0, 50, 15)
        with col3:
            fournisseurs = st.number_input("Nombre Fournisseurs Récurrents", value=5)
            
        submitted = st.form_submit_button("Calculer le Score Risque")
        
        if submitted:
            # Algorithme de scoring fictif
            score = (flux_mobile / 100000) * 0.4 + (recharge_freq * 2) + (fournisseurs * 5)
            
            if score > 150:
                st.success(f"Score : {score:.0f} - Risque Faible. Crédit Accordé.")
            elif score > 80:
                st.warning(f"Score : {score:.0f} - Risque Modéré. Nécessite une garantie.")
            else:
                st.error(f"Score : {score:.0f} - Risque Élevé. Dossier à étudier manuellement.")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b;">
    <small>Guide Pratique de la Gestion Augmentée | Inspiré par la Méthode AMIHARBI & Synergie Data Science</small>
</div>
""", unsafe_allow_html=True)