AI-Based Story Generation Using Writing Prompts
Project Overview
AI-based story generation leverages advanced artificial intelligence models, such as GPT (Generative Pre-trained Transformers), to automatically create narratives. These models are trained on extensive datasets of human-written text, enabling them to produce coherent and contextually relevant stories across various genres. This project focuses on generating creative stories based on user-provided writing prompts using a transformer-based model. The final model is deployed via a Streamlit application for an interactive user experience.

Features
Story Generation: Generates creative and contextually relevant stories from user-provided prompts.

Training on Large Dataset: The model is trained on a comprehensive dataset of writing prompts and corresponding human-written stories.

User-Friendly Interface: Utilizes Streamlit for an intuitive and interactive user experience.

Model Efficiency: Supports model saving and loading for efficient reuse and deployment.

Dataset
The dataset used for this project is sourced from Kaggle and consists of writing prompts paired with human-generated stories. The dataset is structured into three subsets: training, validation, and test sets.

Dataset Link
Writing Prompts Dataset on Kaggle

Dataset Files
The dataset is divided into the following files:

Training Set:

train.wp_source: Contains writing prompts.

train.wp_target: Contains corresponding human-written stories.

Validation Set:

valid.wp_source: Contains writing prompts.

valid.wp_target: Contains corresponding human-written stories.

Test Set:

test.wp_source: Contains writing prompts.

test.wp_target: Contains corresponding human-written stories.

Dataset Description
Writing Prompts: Short, creative prompts provided to human authors to inspire story creation.

Human-Written Stories: Stories written by humans in response to the provided prompts.

Purpose: The dataset is used to train, validate, and test the AI model, ensuring it can generate coherent and engaging narratives.

Installation
Prerequisites
Ensure you have Python 3.x installed. Then, install the required dependencies using the following command:

bash
Copy
pip install -r requirements.txt
Dependencies
The project relies on the following Python libraries:

torch: For deep learning model training and inference.

transformers: For using pre-trained transformer models like GPT.

flask: For creating the API (if needed).

numpy: For numerical computations.

pandas: For data manipulation and analysis.

tqdm: For progress bars during training.

scikit-learn: For evaluation metrics (if needed).

streamlit: For the interactive web application.

Model Training
To train the AI model, run the following command:

bash
Copy
python train.py
Training Process
Data Loading: The script loads the dataset from the provided files.

Model Training: A transformer-based architecture is used to train the model on the writing prompts and corresponding stories.

Model Saving: The trained model is saved as model.pth for future use.

Running the Streamlit Application
To deploy the AI story generator as an interactive Streamlit application, run:

bash
Copy
streamlit run app.py
Streamlit Interface
Input: Users can enter a writing prompt in the provided text box.

Output: The AI-generated story is displayed in real-time.

API Endpoints (Optional)
If you choose to deploy the model as an API using Flask, the following endpoint is available:

Generate Story: Send a POST request to /generate with a JSON payload containing a prompt.

json
Copy
{
  "prompt": "Once upon a time..."
}
Response: The API returns a JSON object containing the generated story.

Model Saving & Loading
Saving: The trained model is saved as model.pth after training.

Loading: The model is loaded in app.py or the API script before generating stories.

Usage
Start the Streamlit Application: Run streamlit run app.py to launch the interactive interface.

Enter a Prompt: Provide a writing prompt in the input field.

Generate a Story: The AI will generate a narrative based on the provided prompt.

Explore: Experiment with different prompts to see the variety of stories the AI can create.

Future Enhancements
Fine-Tuning: Fine-tune the model on specific genres or writing styles.

User Feedback: Incorporate user feedback to improve story quality.

Multi-Language Support: Extend the model to generate stories in multiple languages.

Advanced Features: Add options for controlling story length, tone, or character development.

Contributing
Contributions to this project are welcome! Please follow these steps:

Fork the repository.

Create a new branch for your feature or bug fix.

Submit a pull request with a detailed description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
The dataset is sourced from Kaggle.

Special thanks to the developers of the transformers library by Hugging Face for providing pre-trained models.

