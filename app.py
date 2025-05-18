import streamlit as st
import pandas as pd
import numpy as np
import requests as rq



st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: white; font-size: 50px;">WELCOME TO <span style = "color :yellow;">CINEMATCH </span> </h1>
    </div>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    movies = pd.read_csv("movie.csv")
    cosine_vect = pd.read_csv("cosine_vect").to_numpy()
    return movies, cosine_vect

movies, cosine_vect = load_data()

Options = movies['title']
selected_movie = st.selectbox("SELECT  MOVIE",Options ,placeholder = "Search for movie" )


if "selected_movie" not in st.session_state:
   st.session_state.selected_movie = movies['title'].iloc[2]
   st.session_state.bool = False
elif st.session_state.bool:
   selected_movie =  st.session_state.selected_movie
   


def container (movie_ind,img_p,overview_hp):
   
   with st.container():
      
      col1,col2 = st.columns(2)

      with col1:
         st.markdown(f'<h1 style="font-size: 28px; text-align: center;">{movies.loc[movie_ind[0], "title"]}</h1>', unsafe_allow_html=True)
         st.write(overview_hp[0][0:350])
         if st.button('Watch'):
            st.markdown(f'<a href="{overview_hp[1]}" target="_blank">Click here to watch</a>', unsafe_allow_html=True)
      
      with col2:
         st.image(f"https://image.tmdb.org/t/p/w500{img_p[0]}",width = 200) 

   st.markdown('<hr style="margin-top: 10px; margin-bottom: 5px;">', unsafe_allow_html=True)   
   st.markdown(f'<h2 style="font-size: 30px;">Recomended Movies</h2>', unsafe_allow_html=True)
   st.markdown('<hr style="margin-top: 0px; margin-bottom: 20px;">', unsafe_allow_html=True)

   with st.container():
      cols = st.columns(4)
      
      
      st.session_state.bool = False 
      st.session_state.selected_movie=None
      

      for i in range(1,len(img_p)):
         with cols[i-1]:

            st.image(f"https://image.tmdb.org/t/p/w500{img_p[i]}", width=400)
            
            if st.button(f" {movies.loc[movie_ind[i], 'title']}"):
                     st.session_state.selected_movie = movies.loc[movie_ind[i], 'title']
                     st.session_state.bool = True
                     
                     st.rerun() 








def run (selected_movie):
   
   img_p = []
   overview_hp = []
   movie_ind = [] 
      


   index = movies.index[movies['title'] == selected_movie]
   c_v = cosine_vect[index][0]
    
   s_cv = sorted(enumerate(c_v) ,key = lambda x:x[1] ,reverse = True)
    
   for i in np.arange(5):
      pos = s_cv[i][0]
      movie_ind.append(pos)

   img_p = []
   overview_hp = []

   
   for i in range(0,len(movie_ind)):
      ind = movie_ind[i]
      movies_id = movies.loc[ind,'movie_id']
   
      movie_url = f"https://api.themoviedb.org/3/movie/{movies_id}?api_key=8265bd1679663a7ea12ac168da84d2e8"
      movie_url_response = rq.get(movie_url)
      movie_details = movie_url_response.json()
      

      image_path = movie_details.get('poster_path')
      img_p.append(image_path)
      
      if i==0:
         overview_hp.append(movie_details.get('overview'))
         overview_hp.append(movie_details.get('hompepage'))

   container(movie_ind,img_p,overview_hp)

run(selected_movie)




  

               
            
            
