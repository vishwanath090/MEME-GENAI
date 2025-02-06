# AI-Based Story Generator

## Overview
The AI-Based Story Generator is a web application designed to generate creative short stories based on user-provided prompts. This project utilizes a fine-tuned Sequence-to-Sequence (Seq2Seq) model trained on the Writing Prompts dataset to produce engaging and contextually relevant narratives. The application provides users with an intuitive web interface to experiment with AI-generated storytelling, making it accessible to writers, hobbyists, and AI enthusiasts.

## Features
- **AI-Powered Story Generation**: Generates unique, engaging stories from user prompts.
- **Fine-Tuned Seq2Seq Model**: Improves story coherence, creativity, and fluency.
- **Web-Based Interface**: Developed using Streamlit for ease of use.
- **Customizable Creativity Settings**: Adjustable parameters such as temperature, top-k, and top-p.
- **Story Management**: Save, copy, or share generated stories.
- **GPU Acceleration Support**: Optional for faster inference times.

## Installation

### Prerequisites
- Python 3.8+
- Pip (Python package manager)
- Virtual environment (optional but recommended)
- GPU (optional for faster processing)

### Clone the Repository
```bash
git clone https://github.com/vishwanath090/Storygeneration
cd storygenerator
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Dataset: Writing Prompts
The **Writing Prompts dataset** is a large-scale dataset designed for creative writing and storytelling. It contains diverse prompts paired with user-generated responses, making it an excellent resource for training AI models in generating coherent and imaginative narratives.

The dataset consists of the following files:
- `train.wp.source`: Training set prompts
- `train.wp.target`: Corresponding stories for training prompts
- `valid.wp.source`: Validation set prompts
- `valid.wp.target`: Corresponding stories for validation prompts
- `test.wp.source`: Test set prompts
- `test.wp.target`: Corresponding stories for test prompts

## Model Training and Fine-Tuning
The model is fine-tuned on the Writing Prompts dataset using **Hugging Face's Transformers library**.

### Training Steps:
1. **Preprocess the Dataset**: Clean and tokenize the data.
2. **Fine-Tune the Model**:
```bash
python train.py --model_name seq2seq --epochs 3 --batch_size 8
```
3. **Save the Trained Model**: The trained model is stored for later inference.

## Running the Web App
### Start the Application
```bash
streamlit run app.py
```

### Access the Web Interface
After running the above command, open your browser and navigate to the Streamlit-provided URL.

## Usage
- **Enter a Writing Prompt**: Provide a creative idea or sentence.
- **Click "Generate"**: The AI creates a unique story.
- **Adjust Creativity Parameters**: Modify temperature and top-k settings for varied outputs.
- **Save, Copy, or Share**: Manage generated stories easily.

## Technologies Used
- **Backend**: Python, TensorFlow/PyTorch, Hugging Face Transformers
- **Frontend**: Streamlit, HTML, CSS, JavaScript
- **Model Architecture**: Seq2Seq for text generation
- **Deployment**: Local execution (future cloud-based options)

## Future Improvements
- Enhance model performance with **larger datasets** and **fine-tuning techniques**.
- Implement **user feedback-based reinforcement learning** for iterative improvement.
- Support **multiple story genres** for personalized storytelling experiences.
- Develop a **mobile-friendly UI** for accessibility on all devices.
- Deploy as a **cloud-based service** for wider usability.

## License
This project is open-source and available under the **MIT License**.



