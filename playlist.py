import streamlit as st
import os

st.header("Your Emotion Based Playlist")

# Extract mood from URL query parameters
query_params = st.experimental_get_query_params()
mood = query_params.get("mood", [None])[0]

if mood:
    st.success(f"Feeling {mood} !")
    st.success(f"Here are some {mood} songs for you")
    song_list = os.listdir(f"./song/{mood}/")
    str_song_path = f"./song/{mood}/"
    for i in song_list:
        st.write(i.replace(".mp3", "") + ":")
        st.audio(str_song_path + i)
else:
    st.warning("Mood not specified in the URL. Please go back and select a mood.")
