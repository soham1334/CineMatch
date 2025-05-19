# CineMatch

CineMatch is a content-based movie recommendation system built with Streamlit, offering intelligent movie suggestions based on metadata like genre, cast, keywords, and more. It provides an interactive experience with movie poster previews, overviews, and direct links to official sites.

### 🌐 Live Demo: https://cinematch-r5qyyuswzgqhz2bfbcwscu.streamlit.app/
### 🌙 Best viewed in dark theme for optimal visual experience.

## 📌 Features
🔍 Movie Search: Choose from a dropdown list of available movies.

🧠 Content-Based Filtering: Recommends similar movies using vectorized metadata.

🖼️ Poster Display: Dynamically retrieves movie posters via the TMDB API.

📝 Overview & Details: Presents a short description of the selected movie.

🔗 Watch Button: Redirects users to the official homepage (if available).

♻️ Interactive Flow: Selecting a recommendation refreshes suggestions.

## 📂 Dataset Notes
📁 Original Dataset: Based on TMDB’s dataset of 5,000 movies.

✂️ Sample Used: Reduced to 1,800 movies to optimize performance and minimize file size for deployment.

This was necessary to keep the cosine similarity matrix and tag vector file sizes manageable within Streamlit hosting constraints.

## ⚙️ How It Works
Textual Metadata from genres, cast, crew, production info, and overviews is preprocessed into unified "tags".

These tags are vectorized using CountVectorizer.

Cosine similarity is computed across all vectors to find the top 5 closest matches for any selected movie.

Posters and overview details are fetched in real-time from the TMDB API.

## 🛠 Tech Stack
Frontend: Streamlit

Backend: Python, pandas, scikit-learn, requests

NLP: NLTK for tokenization & lemmatization

Similarity Engine: CountVectorizer + cosine similarity

External API: TMDB for poster and homepage data

## 📦 Deployment Notes
The project is deployed on Streamlit Cloud.

Only the top 1800 movies are included to ensure quick loading and API responsiveness.

TMDB API key is currently hardcoded — for production use, secure it with environment variables.




