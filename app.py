import os
import numpy as np
import random
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Define dataset paths
images_folder = r"C:\Users\91807\OneDrive\Desktop\MEME\memes900k\images"
captions_path = r"C:\Users\91807\OneDrive\Desktop\MEME\memes900k\captions.txt"
font_path = "impact.ttf"  # Ensure you have "impact.ttf" in your project directory

# Cache model loading for efficiency
@st.cache_resource
def load_meme_model():
    return load_model("meme_generator.h5")

# Load the trained model
model = load_meme_model()

# Load tokenizer and captions
captions = open(captions_path, encoding="utf-8").read().split("\n")
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(captions)

def wrap_text(draw, text, font, max_width):
    """Wrap text so it fits inside the image width."""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        width, _ = draw.textbbox((0, 0), test_line, font=font)[2:]  # Get text width

        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines

def draw_stylized_text(draw, text, position, font, image_width):
    """Draws meme text with a bold, capitalized, and outlined effect."""
    text = text.upper()  # MEME text is usually in uppercase
    x, y = position

    # Black stroke effect
    outline_range = [-2, 0, 2]
    for dx in outline_range:
        for dy in outline_range:
            draw.text((x + dx, y + dy), text, font=font, fill="black")

    # White text
    draw.text((x, y), text, font=font, fill="white")

def generate_meme(user_input):
    """Generate a meme with an AI-generated caption and overlay text on the image."""
    # Convert input to sequence
    sequence = tokenizer.texts_to_sequences([user_input])
    padded = pad_sequences(sequence, maxlen=20, padding="post")

    # Predict caption
    prediction = model.predict(padded)
    predicted_index = np.argmax(prediction)
    caption = tokenizer.index_word.get(predicted_index, "No caption generated").upper()  # Capitalize for meme effect

    # Select a random meme template
    image_files = os.listdir(images_folder)
    selected_image = random.choice(image_files)
    image_path = os.path.join(images_folder, selected_image)
    image = Image.open(image_path)

    # Resize image if needed
    max_size = (600, 600)
    image.thumbnail(max_size, Image.Resampling.LANCZOS)

    # Prepare text overlay
    draw = ImageDraw.Draw(image)

    # Load font
    try:
        font = ImageFont.truetype(font_path, 40)  # Load "Impact" font
    except IOError:
        font = ImageFont.load_default()  # Fallback if Impact font is missing

    # Wrap text for readability
    max_width = image.width - 40  # Padding from edges
    wrapped_text = wrap_text(draw, caption, font, max_width)

    # Calculate text height
    total_text_height = sum(draw.textbbox((0, 0), line, font=font)[3] for line in wrapped_text)

    # Position the text at top and bottom like a classic meme
    top_y = 10  # Position at the top
    bottom_y = image.height - total_text_height - 10  # Position at the bottom

    # Draw top text
    for line in wrapped_text:
        text_width = draw.textbbox((0, 0), line, font=font)[2]
        x_position = (image.width - text_width) // 2  # Center text
        draw_stylized_text(draw, line, (x_position, top_y), font, image.width)
        top_y += font.size  # Move to next line

    # Draw bottom text
    for line in wrapped_text:
        text_width = draw.textbbox((0, 0), line, font=font)[2]
        x_position = (image.width - text_width) // 2  # Center text
        draw_stylized_text(draw, line, (x_position, bottom_y), font, image.width)
        bottom_y += font.size  # Move to next line

    return image, caption

# Streamlit UI
st.title("🖼️ AI-Powered Meme Generator 🤖")
user_text = st.text_input("Enter a meme idea:")

if st.button("Generate Meme"):
    if user_text:
        meme_image, generated_caption = generate_meme(user_text)
        
        # Display image in Streamlit
        st.image(meme_image, caption=generated_caption, use_container_width=True)

        # Save the generated meme
        meme_image.save("generated_meme.jpg")
        st.success("Meme saved as 'generated_meme.jpg'! 🎉")
    else:
        st.warning("Please enter a meme idea.")
