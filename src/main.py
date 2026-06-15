import json
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details


config = json.load(open("config.json"))

# OMDB api key
OMDB_API_KEY = config["OMDB_API_KEY"]

st.set_page_config(
    page_title="CineMatch AI",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 CineMatch AI")
st.caption("Discover your next favorite movie with AI-powered recommendations")

movie_list = sorted(df['title'].dropna().unique())
selected_movie = st.selectbox("🎬 Select a movie:", movie_list)

if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend_movies(selected_movie)
        if recommendations is None or recommendations.empty:
            st.warning("Sorry, no recommendations found.")
        else:
            st.success("Top similar movies:")
            for _, row in recommendations.iterrows():
                movie_title = row['title']
                plot, poster, runtime, language, released, imdbRating = get_movie_details(movie_title, OMDB_API_KEY)

                movie_query = movie_title.replace(" ", "+")
                youtube_url = f"https://www.youtube.com/results?search_query={movie_query}+Official+Trailer"

                with st.container():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if poster != "N/A":
                            st.image(poster, width=300)
                        else:
                            st.write("❌ No Poster Found") 
                    with col2:
                        st.markdown(f"### {movie_title}")
                        st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")
                        st.markdown(f"**⏱ Duration:** {runtime}")
                        st.markdown(f"**🌐Language:** {language}")
                        st.markdown(f"**📅Released:** {released}")
                        st.markdown(f"**⭐ IMDb Rating:** {imdbRating}")
                        st.markdown(f"[▶ Watch Trailer]({youtube_url})")