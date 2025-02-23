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
    """Wraps text to fit within the image width."""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=font)
        text_width = bbox[2] - bbox[0]  # Get width from bbox

        if text_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines

def draw_stylized_text(draw, lines, position, font, image_width):
    """Draws meme text with bold, capitalized, and outlined effects."""
    y = position[1]  # Starting y-position

    for line in lines:
        line = line.upper()  # MEME text is usually in uppercase
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]

        x = (image_width - text_width) // 2  # Center text horizontally

        # Create a black stroke outline for text readability
        for dx in [-2, 0, 2]:
            for dy in [-2, 0, 2]:
                draw.text((x + dx, y + dy), line, font=font, fill="black")

        # Draw white text on top
        draw.text((x, y), line, font=font, fill="white")

        y += font.size  # Move down for the next line

def generate_meme(user_input):
    """Generates a meme with AI-generated caption and overlays it on an image."""
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

    # Calculate total text height
    total_text_height = sum(font.size for _ in wrapped_text)

    # Position text at top and bottom
    top_y = 10  # Top margin
    bottom_y = image.height - total_text_height - 20  # Bottom margin

    # Draw top text
    draw_stylized_text(draw, wrapped_text, (0, top_y), font, image.width)

    # Draw bottom text
    draw_stylized_text(draw, wrapped_text, (0, bottom_y), font, image.width)

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
