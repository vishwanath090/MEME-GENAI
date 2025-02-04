import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Sample Data: Genres and Story Count
genre_data = {
    "Genre": [
        "Fantasy", "Sci-Fi", "Horror", "Romance", "Mystery", "Adventure", "Dystopian", "Supernatural", 
        "Thriller", "Western", "Mythology", "Cyberpunk", "Steampunk", "Time Travel", "Post-Apocalyptic", 
        "Dark Fantasy", "Historical Romance", "Slice of Life", "Coming-of-Age", "Magical Realism", 
        "Detective Fiction", "Psychological Thriller", "Legal Drama", "Interactive Fiction", "Satire/Parody"
    ],
    "Stories Generated": [50, 30, 40, 20, 25, 15, 10, 18, 22, 12, 14, 9, 7, 16, 11, 13, 8, 6, 17, 5, 21, 19, 4, 3, 2]
}
df = pd.DataFrame(genre_data)

# Function to Generate a Story
def generate_story(prompt, genre):
    """Generates a simple AI-like story based on prompt and genre."""
    story_templates = {
        "Fantasy": f"Once upon a time in a mystical land, {prompt} embarked on an epic journey...",
        "Sci-Fi": f"In the year 3021, {prompt} discovered a secret that could change humanity forever...",
        "Horror": f"The night was eerie, and {prompt} felt an unknown presence lurking in the dark...",
        "Romance": f"Under the moonlit sky, {prompt} met someone who would change their life forever...",
        "Mystery": f"Detective {prompt} found a clue that led to the biggest revelation of their career...",
        "Adventure": f"With a map in hand, {prompt} set out on a daring quest across uncharted lands...",
        "Dystopian": f"In a world ruled by technology, {prompt} uncovered a hidden resistance...",
        "Supernatural": f"Strange whispers called out to {prompt}, revealing a world beyond the veil...",
        "Thriller": f"A single phone call changed {prompt}'s life forever...",
        "Western": f"In the wild west, {prompt} faced the most feared outlaw of all time...",
        "Mythology": f"According to legend, {prompt} was destined to fulfill an ancient prophecy...",
        "Cyberpunk": f"Neon lights flickered as {prompt} hacked into the most secure system in the city...",
        "Steampunk": f"With steam-powered wings, {prompt} soared above the industrial skyline...",
        "Time Travel": f"A mysterious device transported {prompt} through the centuries...",
        "Post-Apocalyptic": f"Surviving in the wastelands, {prompt} searched for signs of life...",
        "Dark Fantasy": f"The cursed forest whispered secrets only {prompt} could hear...",
        "Historical Romance": f"In the court of kings and queens, {prompt} found an impossible love...",
        "Slice of Life": f"Through everyday moments, {prompt} learned the true meaning of happiness...",
        "Coming-of-Age": f"With each challenge, {prompt} grew into the person they were meant to be...",
        "Magical Realism": f"One day, {prompt} woke up to find the world subtly but unmistakably different...",
        "Detective Fiction": f"A case like no other landed on {prompt}'s desk, and the mystery began...",
        "Psychological Thriller": f"Nothing was as it seemed when {prompt} uncovered the twisted truth...",
        "Legal Drama": f"In the courtroom, {prompt} fought for justice against all odds...",
        "Interactive Fiction": f"The choices {prompt} made would determine their fate...",
        "Satire/Parody": f"In a world full of absurdity, {prompt} became the most unexpected hero..."
    }
    return story_templates.get(genre, "Sorry, genre not found!")

# Function to Save Story
def save_story(prompt, genre, story):
    filename = "generated_stories.csv"
    new_data = pd.DataFrame([[datetime.now(), prompt, genre, story]],
                             columns=["Timestamp", "Prompt", "Genre", "Story"])
    if os.path.exists(filename):
        new_data.to_csv(filename, mode='a', header=False, index=False)
    else:
        new_data.to_csv(filename, mode='w', header=True, index=False)

# Function to Clear Story History
def clear_story_history():
    filename = "generated_stories.csv"
    if os.path.exists(filename):
        os.remove(filename)
        st.success("All story history has been cleared!")
    else:
        st.warning("No history found to clear.")

# Load Saved Stories
def load_stories():
    filename = "generated_stories.csv"
    if os.path.exists(filename):
        return pd.read_csv(filename)
    return pd.DataFrame(columns=["Timestamp", "Prompt", "Genre", "Story"])

# Streamlit UI
st.title("📖 AI Story Generator Dashboard")
st.write("Generate stories based on AI and analyze user trends!")

# Story Input Section
st.subheader("✍️ Generate a Story")
prompt = st.text_input("Enter a story prompt:")
genre = st.selectbox("Choose a genre:", df["Genre"].tolist())

if st.button("Generate Story"):
    generated_story = generate_story(prompt, genre)
    save_story(prompt, genre, generated_story)
    st.success("Story Generated Successfully!")
    st.write(generated_story)

# Clear History Button
if st.button("Clear Story History"):
    clear_story_history()

# Chart: Story Generation Stats
st.subheader("📊 Story Distribution by Genre")
fig = px.bar(df, x="Genre", y="Stories Generated", color="Genre", title="Story Generation Statistics")
st.plotly_chart(fig)

# Matplotlib Pie Chart
st.subheader("🎭 Genre Distribution")
fig_pie, ax_pie = plt.subplots(figsize=(8, 8))
ax_pie.pie(df["Stories Generated"], labels=df["Genre"], autopct='%1.1f%%', startangle=140, pctdistance=0.85)
ax_pie.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.
plt.tight_layout()
st.pyplot(fig_pie)

# Load and Display Recent Stories
st.subheader("📝 Recent User Stories")
story_df = load_stories()
st.dataframe(story_df.tail(5))

# Download Stories Button
st.subheader("⬇️ Download Your Stories")
if not story_df.empty:
    csv = story_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Stories as CSV",
        data=csv,
        file_name="generated_stories.csv",
        mime="text/csv"
    )
