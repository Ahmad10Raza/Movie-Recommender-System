
import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=0cf5a477980b8ea89472711e5a913d64&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System Using Machine Learning')
movies = pickle.load(open('artifacts/movies_list.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Create two rows of 5 columns
    row1_col1, row1_col2, row1_col3, row1_col4, row1_col5 = st.columns(5)
    row2_col1, row2_col2, row2_col3, row2_col4, row2_col5 = st.columns(5)

    # Populate the first row
    with row1_col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with row1_col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with row1_col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with row1_col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with row1_col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

    # Populate the second row
    with row2_col1:
        # Add logic to check if there are more recommendations available
        if len(recommended_movie_names) > 5:
            st.text(recommended_movie_names[5])
            st.image(recommended_movie_posters[5])
    with row2_col2:
        # Add logic to check if there are more recommendations available
        if len(recommended_movie_names) > 6:
            st.text(recommended_movie_names[6])
            st.image(recommended_movie_posters[6])
    with row2_col3:
        # Add logic to check if there are more recommendations available
        if len(recommended_movie_names) > 7:
            st.text(recommended_movie_names[7])
            st.image(recommended_movie_posters[7])
    with row2_col4:
        # Add logic to check if there are more recommendations available
        if len(recommended_movie_names) > 8:
            st.text(recommended_movie_names[8])
            st.image(recommended_movie_posters[8])
    with row2_col5:
        # Add logic to check if there are more recommendations available
        if len(recommended_movie_names) > 9:
            st.text(recommended_movie_names[9])
            st.image(recommended_movie_posters[9])
