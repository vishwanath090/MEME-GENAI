# AI-Powered Meme Generator

An AI-powered meme generator using deep learning and NLP to create memes with captions. Built with TensorFlow, Streamlit, and the Memes900k dataset.

## Features
- AI-generated meme captions using NLP and deep learning  
- Randomly selects a meme template from the dataset  
- Uses Impact font for meme styling  
- Streamlit-based UI for easy interaction  
- Meme generation and image overlay with PIL  
- Saves generated memes locally  

## Dataset Structure (Memes900k)
This project utilizes the Memes900k dataset, which consists of the following files:

```
memes900k/
├── images/                # Folder containing meme template images
├── captions.txt           # All available captions
├── captions_train.txt     # Training dataset
├── captions_val.txt       # Validation dataset
├── captions_test.txt      # Test dataset
├── templates.txt          # Meme template references
```
Ensure you download and place the dataset in the correct directory before running the project.

## Installation

### 1. Clone the Repository  
```sh
git clone https://github.com/yourusername/ai-meme-generator.git
cd ai-meme-generator
```

### 2. Install Dependencies  
```sh
pip install -r requirements.txt
```

### 3. Download Dataset  
Place the Memes900k dataset in the correct directory as mentioned above.

### 4. Run the Meme Generator  
```sh
streamlit run app.py
```

## Project Files  

| File                 | Description                           |
|----------------------|--------------------------------------|
| `app.ipynb`         | Jupyter notebook for model training  |
| `dep.py`            | Core script for meme generation      |
| `meme_generator.h5` | Pre-trained deep learning model      |
| `requirements.txt`  | Dependencies for the project        |
| `impact.ttf`        | Font used for meme generation       |
| `generated_meme.jpg`| Output meme file                    |

## How It Works  

1. The user inputs a meme idea into the Streamlit UI.  
2. The model processes the text and predicts a funny caption.  
3. A random meme template is selected from the dataset.  
4. The caption is overlaid on the image using PIL (Pillow).  
5. The final meme is displayed and saved as `generated_meme.jpg`.  

## Dependencies  

Ensure you have the following libraries installed:
- tensorflow
- numpy
- streamlit
- pillow
- random
- os

Install them via:  
```sh
pip install tensorflow numpy streamlit pillow
```

## Contributing  

Want to improve the meme generator? Follow these steps:

1. Fork the repo  
2. Create a new branch:  
   ```sh
   git checkout -b feature-xyz
   ```
3. Commit your changes:  
   ```sh
   git commit -m "Add new feature"
   ```
4. Push to the branch:  
   ```sh
   git push origin feature-xyz
   ```
5. Submit a Pull Request  

## License  
This project is licensed under the MIT License.  

For any issues, feel free to open an issue or contact me.  

**Enjoy Generating AI-Powered Memes!**

