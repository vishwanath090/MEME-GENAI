# AI-Based Story Generation Using Writing Prompts

## Project Overview
AI-based story generation refers to the use of artificial intelligence models, like GPT (Generative Pre-trained Transformers) or similar systems, to create narratives automatically. These AI models are trained on vast datasets of human-written text, enabling them to generate coherent and contextually relevant stories across a variety of genres
This project utilizes AI to generate creative stories based on user-provided writing prompts. The model is trained on a dataset of writing prompts. The final model is deployed using Flask for an interactive user experience.

## Features
- Generates creative and contextually relevant stories from prompts.
- Trained on a large dataset of writing prompts and stories.
- User-friendly API using Flask.
- Model saving and loading for efficient reuse.

## Dataset
dataset link: https://www.kaggle.com/datasets/ratthachat/writing-prompts
The dataset consists of writing prompts and human-generated stories, stored in the following files:
- `valid.wp_target`
- `valid.wp_source`
- `train.wp_target`
- `train.wp_source`
- `test.wp_target`
- `test.wp_source`
  
•	Abbreviation	•	Meaning	             •	Example Files

•	wp	          •	Writing Prompts	     •	train.wp.source, train.wp.target

•	rr	          •	Reddit Responses	   •	train.rr.source, train.rr.target

•	vp	          •	Validation Prompts	 •	valid.vp.source, valid.vp.target

•	tt	          •	Title-Text           •	train.tt.source, train.tt.target


### Dataset Description
The dataset is structured into pairs of writing prompts and their corresponding human-written stories. It is divided into three subsets:
- **Train Set**: Used to train the model, ensuring it learns from a diverse set of writing prompts and story responses.
- **Validation Set**: Used to fine-tune and evaluate the model's performance during training.
- **Test Set**: Used to assess the final model's ability to generate coherent and engaging stories.

Each dataset file is split into:
- `.wp_source`: Contains the writing prompts provided to human authors.
- `.wp_target`: Contains the corresponding human-written stories.

## Installation
### Prerequisites
Ensure you have Python installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

### Dependencies
The project requires the following Python libraries:
```txt
torch
transformers
flask
numpy
pandas
tqdm
scikit-learn
```

## Model Training
Train the AI model using the dataset:
```bash
python train.py
```
This script will:
1. Load the dataset.
2. Train the model using a transformer-based architecture.
3. Save the trained model for future use.

## Running the Flask API
To deploy the AI story generator as an API using Flask, run:
```bash
python app.py
```

## API Endpoints
- **Generate Story**: Send a POST request to `/generate` with a JSON payload containing a `prompt`.
  ```json
  {
    "prompt": "Once upon a time..."
  }
  ```
- The API responds with a generated story.

## Model Saving & Loading
- The trained model is saved as `model.pth`.
- You can load the model in `app.py` before generating stories.

## Usage
1. Start the Flask API.
2. Send a request to the `/generate` endpoint with a writing prompt.
3. Receive an AI-generated narrative as a response.



