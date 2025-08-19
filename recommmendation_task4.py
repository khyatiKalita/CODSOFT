import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


data = {
    'title': [
        'The Shawshank Redemption',
        'The Godfather', 
        'The Dark Knight',
        'Pulp Fiction',
        'Forrest Gump',
        'Inception',
        'The Matrix'
    ],
    'genre': [
        'Drama Crime',
        'Crime Drama',
        'Action Crime Drama',
        'Crime Drama',
        'Drama Romance',
        'Action Sci-Fi Thriller',
        'Action Sci-Fi'
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['genre'])


cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def recommend_movies(title, cosine_sim=cosine_sim):
    if title not in df['title'].values:
        return "Movie not found in database."
    
    idx = df.index[df['title'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # top 3 recommendations
    
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

user_input = input("Enter the movie name of your choice: ")
print(f"Recommendations for: {user_input}")
print(recommend_movies(user_input))
