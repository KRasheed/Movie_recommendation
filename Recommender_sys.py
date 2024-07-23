import pandas as pd
from Pre_processor import TextProcessor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get('MOVIE_POSTER')

vectorizer = TfidfVectorizer(min_df=2, max_df=0.7)


def transform_data(dataframe):
    x = vectorizer.fit_transform(dataframe['combined'])
    # Compute the cosine similarity matrix
    similarity = cosine_similarity(x, x)
    with open('similarity_matrix.pkl', 'wb') as f:
        pickle.dump(similarity, f)


def recommend_table(list_of_movie_enjoyed, similarity_matrix, movie_titles, movie_count=20):
    enjoyed_indices = [movie_titles.index(movie) for movie in list_of_movie_enjoyed]
    user_similarity = np.mean(similarity_matrix[enjoyed_indices], axis=0)
    similarity_df = pd.DataFrame(user_similarity, index=movie_titles, columns=["similarity_score"])
    similarity_df = similarity_df.drop(list_of_movie_enjoyed)
    sorted_similarity_df = similarity_df.sort_values(by="similarity_score", ascending=False).head(movie_count)

    recommended_movies = sorted_similarity_df.index.tolist()

    return recommended_movies


def get_movie_poster(movie_title):
    # Step 1: Search for the movie by title
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    search_response = requests.get(search_url).json()

    if search_response['results']:
        # Step 2: Get the movie ID from the search results
        movie_id = search_response['results'][0]['id']

        # Step 3: Fetch movie details using the movie ID
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        details_response = requests.get(details_url).json()

        # Step 4: Get the poster path and construct the full image URL
        poster_path = details_response.get('poster_path')
        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return poster_url
    return None


all_data = pd.read_csv('Data//netflix_titles.csv')

all_data['combined'] = all_data[['title', 'director', 'cast', 'description']].apply(lambda x: ' '.join(x.dropna()),
                                                                                    axis=1)

all_data['combined'] = all_data['combined'].apply(lambda x: TextProcessor(x).pre_processor(x))
pickle.dump(all_data['title'].to_list(), open('movie_dict.pkl', 'wb'))
# transform_data(all_data)
