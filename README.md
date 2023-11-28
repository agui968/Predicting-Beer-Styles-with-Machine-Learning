#### Welcome to the Beer Style Prediction Project! 🍻

This repository hosts several machine learning models designed to classify beer styles based on key features like Alcohol By Volume (ABV), International Bitterness Units (IBU), and color (SRM). Our goal is to provide a robust and accurate tool for predicting beer styles, assisting brewers and enthusiasts alike in understanding and categorizing different brews.

### Key Features:

+ Machine learning models for beer style classification
+ Utilizes ABV, IBU, and color (SRM) as predictive features
+ Data and details sourced from  [Brewersfriend.com](https://www.brewersfriend.com/beer-charts/).
  
### Structure of the repository:
data: This folder contains subdirectories for different data-related purposes.

    raw: Holds the original dataset (dataset.csv).
    processed: Reserved for processed data.
    train: Intended for training data.
    test: Reserved for test data.
notebooks: Includes Jupyter notebooks used for different stages of the project.

    01_Fuentes.ipynb: Likely a notebook for data exploration or early-stage analysis.
    02_LimpiezaEDA.ipynb: Notebook covering data cleaning and exploratory data analysis.
    03_Entrenamiento_Evaluacion.ipynb: Notebook related to model training and evaluation.
src: This directory holds the source code files.

    data_processing.py: A script for data processing.
    training.py: Script for training machine learning models.
    evaluation.py: Script for evaluating model performance.
models: Reserved for storing trained models and related files.

    trained_model.pkl: A file containing the trained machine learning model.
    model_config.yaml: YAML file holding configuration details for the model.
app: This directory is for the application code.

    app.py: A Streamlit application for interactive use.
    requirements.txt: A file specifying dependencies for running the application.
docs: Contains documentation files.

    negocio.ppt: PowerPoint file related to business aspects.
    ds.ppt: PowerPoint file with a focus on data science.
    memoria.md: A Markdown file containing project-related notes.

### Deployment of the model on Streamlit
    (Under construction)
    
Cheers to Data!

(Most of the contents of this repository are in Spanish).