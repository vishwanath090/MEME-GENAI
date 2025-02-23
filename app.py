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
        width, _ = draw.textsize(test_line, font=font)

        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines

def generate_meme(user_input):
    """Generate a meme with an AI-generated caption and display it."""
    # Convert input to sequence
    sequence = tokenizer.texts_to_sequences([user_input])
    padded = pad_sequences(sequence, maxlen=20, padding="post")

    # Predict caption
    prediction = model.predict(padded)
    predicted_index = np.argmax(prediction)
    caption = tokenizer.index_word.get(predicted_index, "No caption generated")

    # Select a random meme template
    image_files = os.listdir(images_folder)
    selected_image = random.choice(image_files)
    image_path = os.path.join(images_folder, selected_image)
    image = Image.open(image_path)

    # Prepare text overlay
    draw = ImageDraw.Draw(image)

    # Load font
    try:
        font = ImageFont.truetype(font_path, 40)  # Load "Impact" font
    except IOError:
        font = ImageFont.load_default()  # Fallback if Impact font is missing

    # Wrap text for better readability
    max_width = image.width - 40  # Keep padding from edges
    wrapped_text = wrap_text(draw, caption, font, max_width)

    # Calculate text height
    total_text_height = sum(draw.textsize(line, font=font)[1] for line in wrapped_text)
    text_y = image.height - total_text_height - 20  # Position at bottom

    # Draw text on meme
    for line in wrapped_text:
        text_width, text_height = draw.textsize(line, font=font)
        text_x = (image.width - text_width) // 2  # Center text
        draw.text((text_x, text_y), line, fill="white", font=font, stroke_width=2, stroke_fill="black")
        text_y += text_height  # Move to the next line

    return image, caption

# Streamlit UI
st.title("🖼️ AI-Powered Meme Generator 🤖")
user_text = st.text_input("Enter a meme idea:")

if st.button("Generate Meme"):
    if user_text:
        meme_image, generated_caption = generate_meme(user_text)
        st.image(image_path, caption="Generated Meme", use_container_width=True)

        # Save the generated meme
        meme_image.save("generated_meme.jpg")
        st.success("Meme saved as 'generated_meme.jpg'! 🎉")
    else:
        st.warning("Please enter a meme idea.")
