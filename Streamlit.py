import streamlit as st
import pickle
import pandas as pd
from Recommender_sys import recommend_table, get_movie_poster
from streamlit import session_state as session

titles_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame({'title': titles_list})

with open('similarity_matrix.pkl', 'rb') as f:
    similarity = pickle.load(f)

dataframe = None

st.title("""
Netflix Recommendation System
This is an Content Based Recommender System made on implicit ratings :smile:.
 """)

st.text("")
st.text("")
st.text("")

session.options = st.multiselect(label="Select Movies", options=movies['title'].values)

if st.button('Recommend'):
    recommended_movies = recommend_table(session.options, similarity_matrix=similarity, movie_titles=titles_list,
                                         movie_count=5)
    st.markdown("<h3 style='font-weight: bold;'>Recommended Movies:</h3>", unsafe_allow_html=True)
    cols = st.columns(len(recommended_movies))
    for idx, movie in enumerate(recommended_movies):
        with cols[idx]:
            st.write(movie)
            poster_url = get_movie_poster(movie)
            if poster_url:
                st.image(poster_url)


