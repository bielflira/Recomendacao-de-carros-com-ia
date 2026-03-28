import streamlit as st
from data import load_data
from recommender import CarRecommender

st.set_page_config(page_title="Car AI", layout="centered")

st.title("🚗 Car AI Recommender")
st.subheader("Descubra o carro ideal com inteligência artificial")

df = load_data()
recommender = CarRecommender(df)

# Inputs do usuário
budget = st.slider("💰 Orçamento", 30000, 120000, 70000)

st.write("🎯 Prioridades:")
economia = st.slider("Economia", 1, 10, 5)
conforto = st.slider("Conforto", 1, 10, 5)
espaco = st.slider("Espaço", 1, 10, 5)

if st.button("Recomendar"):
    prefs = {
        "economia": economia,
        "conforto": conforto,
        "espaco": espaco,
    }

    result = recommender.recommend(budget, prefs)

    st.write("## 🔥 Top recomendações:")
    st.dataframe(result)
