import streamlit as st
import pandas as pd
import random

# Load the CSV file
csv_filename = 'top_songs_sorted(13_february_2025).csv'  # Replace with the actual file path
df = pd.read_csv(csv_filename)

# Sort the DataFrame by 'Views' in descending order
df_sorted = df.sort_values(by='Views', ascending=False)

# Streamlit App
st.title("(Sachin's Fav Music)---Music")

# Music player
selected_song = st.selectbox("Select a song to play:", df_sorted['Title'])
selected_song_url = df_sorted[df_sorted['Title']
                              == selected_song]['Video_URL'].values[0]

# Check if the URL is a YouTube video URL
if "youtube.com" in selected_song_url or "youtu.be" in selected_song_url:
    st.video(selected_song_url)

# Display the title of the selected song
st.write(f"Now playing: {selected_song}")

# Button to play a random song
if st.button("Play Random Song"):
    random_index = random.randint(0, len(df_sorted) - 1)
    selected_song = df_sorted.iloc[random_index]['Title']
    selected_song_url = df_sorted.iloc[random_index]['Video_URL']
    st.write(f"Now playing: {selected_song}")

    # Check if the URL is a YouTube video URL
    if "youtube.com" in selected_song_url or "youtu.be" in selected_song_url:
        st.video(selected_song_url)

# Display CSV file at the end
st.write("**CSV File:**")
st.write(df_sorted)
