# Movie Recommender System
In this project, I have built a content-based movie recommender system. The algorithm recommends movies that are similar to the ones that a user has liked in the past. This similarity (generally cosine similarity) is computed from the data we have about the items as well as the user’s past preferences.

## How It Works

### Content-Based Filtering
They suggest similar items based on a particular item. This system uses item metadata, such as genre, director, description, actors, etc. for movies, to make these recommendations. The general idea behind these recommender systems is that if a person liked a particular item, he or she will also like an item that is similar to it.

## Project Overview

The movie recommender system is deployed using Streamlit

- **Content-Based Recommendations**: Provides movie recommendations based on metadata like genre, director, description, actors, etc.
- **User-Friendly Interface**: Interactive UI built with Streamlit for ease of use.

## Directory Structure

- `Pre-processor.py`: Contains the preparation and pre-processing of movie data to work with text information of movies, i.e., 'title', 'director', 'cast', 'description'.
- `Recommender_sys.py`: Contains all the necessary functions for recommending the movies based on the given preferences of users.
- `Streamlit.py`: The Streamlit code to run the application.
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/KRasheed/movie-recommender-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd movie-recommender-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app locally:
    ```bash
    streamlit run Streamlit.py
    ```
2. Open your web browser and go to `http://localhost:8501` to view the app.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api)
- [Scikit-learn](https://scikit-learn.org/)
