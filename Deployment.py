import streamlit as st
import pickle 
import pandas as pd 
import requests


def recommend(musics):
    music_index=music[music['title']==musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)),reverse =True,key = lambda x:x[1])[1:11]
    recommend_music_poster=[]
    recommend_music=[]
    for i in music_list:
        music_title = music.iloc[i[0]].title
        recommend_music.append(music.iloc[i[0]].title)
    return recommend_music, recommend_music_poster

music_dict = pickle.load(open('musicrec.pkl', 'rb'))


music = pd.DataFrame(music_dict)

similarity = pickle.load(open('similarities.pkl','rb'))
st.title('Music Recomendation System')


selected_music_name = st.selectbox('Select a music you like', music['title'].values)

if st.button('Recommend'):
    names = recommend(selected_music_name)
    st.subheader('Recommended Songs')
    st.table(names[0])

