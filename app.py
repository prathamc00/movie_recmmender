import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.DataFrame({
    'title': ['Interstellar','The Martian','Gravity','Titanic','La La Land',
              'The Notebook','The Dark Knight','Avengers','John Wick',
              'Parasite','The Godfather','Schindler\'s List'],
    'sci_fi':   [1.0,0.9,0.9,0.0,0.0,0.0,0.2,0.6,0.0,0.0,0.0,0.0],
    'action':   [0.7,0.6,0.5,0.1,0.0,0.0,1.0,1.0,1.0,0.2,0.3,0.1],
    'romance':  [0.2,0.1,0.3,1.0,0.8,1.0,0.1,0.2,0.0,0.2,0.3,0.1],
    'drama':    [0.6,0.5,0.4,0.8,0.7,0.7,0.7,0.3,0.2,1.0,1.0,1.0],
    'thriller': [0.5,0.3,0.6,0.1,0.0,0.0,1.0,0.5,0.9,0.8,0.9,0.6],
})

features = movies[['sci_fi','action','romance','drama','thriller']]
sim_matrix = cosine_similarity(features)
sim_df = pd.DataFrame(sim_matrix, index=movies['title'], columns=movies['title'])

st.title("Movie Recommender")
selected = st.selectbox("Pick a movie you like:", movies['title'])
top_n = st.slider("How many recommendations?", 1, 5, 3)

scores = sim_df[selected].sort_values(ascending=False).iloc[1:top_n+1]
st.subheader(f"Because you liked '{selected}':")
for title, score in scores.items():
    st.metric(label=title, value=f"{score:.0%} match")