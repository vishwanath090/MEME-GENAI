import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
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
    return f"{prompt} in a {genre} setting leads to an exciting adventure..."

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

# Display Statistics
st.subheader("📊 Story Statistics")
col1, col2 = st.columns(2)

# Bar Chart
with col1:
    fig_bar = px.bar(df, x="Genre", y="Stories Generated", color="Genre", title="Story Generation Statistics")
    st.plotly_chart(fig_bar)

# Pie Chart
with col2:
    fig_pie = px.pie(df, names="Genre", values="Stories Generated", title="Story Distribution")
    st.plotly_chart(fig_pie)

# Additional Statistical Visualization
st.subheader("📈 Additional Insights")
col3, col4 = st.columns(2)

# Boxplot
with col3:
    fig_box = px.box(df, y="Stories Generated", title="Boxplot of Stories Generated")
    st.plotly_chart(fig_box)

# Histogram & KDE
with col4:
    fig_hist = px.histogram(df, x="Stories Generated", nbins=10, marginal="box", title="Histogram & KDE")
    st.plotly_chart(fig_hist)

# Interactive Scatter Plot
st.subheader("📌 Interactive Scatter Plot")
fig_scatter = px.scatter(df, x="Genre", y="Stories Generated", color="Genre", size="Stories Generated", title="Genre Popularity")
st.plotly_chart(fig_scatter)

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
