import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Your dataset from Step 2
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

# Extract just the number columns (the "feature matrix")
features = movies[['sci_fi', 'action', 'romance', 'drama', 'thriller']]

# Compute similarity between every pair of movies — one line of ML!
similarity_matrix = cosine_similarity(features)

# Wrap it in a nice table with movie names
sim_df = pd.DataFrame(similarity_matrix, index=movies['title'], columns=movies['title'])

# --- The recommender function ---
def recommend(movie_title, top_n=3):
    if movie_title not in sim_df:
        print(f"Movie '{movie_title}' not found!")
        return

    # Get similarity scores for this movie, sort them highest first
    scores = sim_df[movie_title].sort_values(ascending=False)

    # Skip the first result (it's always the movie itself, score = 1.0)
    scores = scores.iloc[1:top_n+1]

    print(f"\nBecause you liked '{movie_title}', try:\n")
    for title, score in scores.items():
        print(f"  {title:<25} similarity: {score:.2f}")

# Test it!
recommend('Interstellar')
recommend('Titanic')
recommend('The Dark Knight')