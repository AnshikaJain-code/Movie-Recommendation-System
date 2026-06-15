# 🎬 CineMatch AI

Discover your next favorite movie with AI-powered recommendations.

## Overview

CineMatch AI is a content-based movie recommendation system that suggests similar movies based on genres, keywords, and plot descriptions. The application leverages Natural Language Processing (NLP), TF-IDF vectorization, and cosine similarity to generate personalized recommendations.

## Features

* 🎥 Content-based movie recommendations
* 🖼️ Movie posters via OMDb API
* 📝 Plot summaries and movie details
* ⭐ IMDb ratings
* 📅 Release date information
* ⏱️ Runtime and language details
* ▶️ Direct trailer search links
* 🌐 Interactive Streamlit web application

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* OMDb API

## Machine Learning Pipeline

1. Data preprocessing and text cleaning
2. Feature engineering using movie metadata
3. TF-IDF vectorization
4. Cosine similarity computation
5. Recommendation generation

## Dataset

* 4,800+ movies
* Genres, keywords, and plot overviews used for recommendation generation

## Installation

```bash
git clone https://github.com/AnshikaJain-code/Movie-Recommendation-System.git
cd Movie-Recommendation-System
pip install -r requirements.txt
```

## Run Locally

```bash
streamlit run src/main.py
```

## Future Enhancements

* Genre-based filtering
* Hybrid recommendation system
* User watchlist
* Personalized recommendations

## Author

Anshika Jain
