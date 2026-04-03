import streamlit as st
import pickle
import pandas as pd
import time
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(page_title="TED Insight Engine", layout="wide")


st.markdown("""
<style>

/* MAIN APP BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

/* SIDEBAR BASE */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #1e1b4b);
    padding: 20px 15px;
    border-right: 1px solid rgba(220,38,38,0.3);
}

/* GLASS EFFECT CONTAINER */
.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius: 15px;
    padding: 18px;
    margin-bottom: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    transition: 0.3s;
}

.glass:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 25px rgba(220,38,38,0.2);
}

/* HEADER */
.sidebar-header {
    text-align: center;
    margin-bottom: 25px;
}

.sidebar-title {
    font-size: 22px;
    font-weight: bold;
    color: white;
}

.ted-highlight {
    color: #dc2626;
}

/* ICON ROW */
.icon-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #dc2626, #7f1d1d);
    color: white;
    border-radius: 8px;
    padding: 10px 18px;
    border: none;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #b91c1c, #450a0a);
}

/* MAIN CARDS */
.card {
    background: linear-gradient(145deg, #111827, #1f2937);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    border-left: 5px solid #dc2626;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.6);
    transition: transform 0.2s ease;
}

.card:hover {
    transform: scale(1.02);
}

/* TITLE */
h1 {
    text-align: center;
    color: #dc2626;
}

.subtext {
    text-align: center;
    color: #9ca3af;
}

</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_data():
    tfidf = pickle.load(open('tfidf.pkl','rb'))
    tfidf_matrix = pickle.load(open('matrix.pkl','rb'))
    indices = pickle.load(open('indices.pkl','rb'))
    df = pd.read_pickle('data.pkl')
    return tfidf, tfidf_matrix, indices, df

tfidf, tfidf_matrix, indices, df = load_data()


def recommend_talk(title, top_n=5):
    if title not in indices:
        return None
    
    idx = indices[title]
    
    similarity = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    
    weighted_score = (
        0.8 * similarity +
        0.2 * (df['views'] / df['views'].max())
    )
    
    similar_idx = weighted_score.argsort()[::-1][1:top_n*2]
    
    results = df[['title','main_speaker','views']].iloc[similar_idx]
    results = results.drop_duplicates(subset='title')
    
    return results.head(top_n)

st.markdown("<h1>🎤 TED Insight Engine</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>AI-powered TED Talk discovery platform</p>", unsafe_allow_html=True)


st.sidebar.markdown("""
<div class="sidebar-header">
    <div style="font-size:40px;">🎤</div>
    <div class="sidebar-title">
        <span class="ted-highlight">TED</span> AI Recommender
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="glass">
    <h4 style="color:#dc2626;">📌 About Project</h4>
    <div class="icon-row">🤖 AI-based Recommendation</div>
    <div class="icon-row">🧠 NLP Processing</div>
    <div class="icon-row">📊 Smart Ranking System</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="glass">
    <h4 style="color:#dc2626;">✨ Features</h4>
    <div class="icon-row">🎯 Personalized Suggestions</div>
    <div class="icon-row">🔥 Popularity Boost</div>
    <div class="icon-row">⚡ Fast Results</div>
</div>
""", unsafe_allow_html=True)


selected_talk = st.selectbox("Choose a TED Talk", df['title'].values)


if st.button("Get Recommendations"):
    
    with st.spinner("Analyzing content..."):
        time.sleep(1.2)
        recommendations = recommend_talk(selected_talk)

    if recommendations is None:
        st.error("Talk not found")
    else:
        st.success("Recommendations ready!")

        st.markdown("## 🎬 Recommended Talks")

        for _, row in recommendations.iterrows():
            st.markdown(f"""
            <div class="card">
                <h3>{row['title']}</h3>
                <p>👤 <b>Speaker:</b> {row['main_speaker']}</p>
                <p>👁 <b>Views:</b> {row['views']}</p>
            </div>
            """, unsafe_allow_html=True)