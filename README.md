## Welcome to the Beer Style Prediction Project! 🍻

This repository hosts several machine learning models designed to classify beer styles based on key features like Alcohol By Volume (ABV), International Bitterness Units (IBU), and color (SRM). Our goal is to provide a robust and accurate tool for predicting beer styles, assisting brewers and enthusiasts alike in understanding and categorizing different brews.

### Key Features:

+ Machine learning models for beer style classification
+ Utilizes ABV, IBU, and color (SRM) as predictive features
+ Data and details sourced from  [Brewersfriend.com](https://www.brewersfriend.com/beer-charts/).
  
### Structure of the repository:

>data: This folder contains subdirectories for different data-related purposes.
> 
>>   raw: Holds the original dataset (dataset.csv).
>>
>>   processed: Reserved for processed, final data used to train the models
>>
>>   train: The part of the processed data used for training
>>
>>   test:  The part of the processed data used for testing and evaluating
>
> notebooks: Includes Jupyter notebooks used for different stages of the project.
>
>>    01_Fuentes.ipynb: Sources for the data
>>
>>   02_LimpiezaEDA.ipynb: Data cleaning and exploratory data analysis
>>
>>   03-06_Entrenamiento_Evaluacion.ipynb: Model training and evaluation
>
> src: This directory holds the source code files.
>
>>    data_processing.py: A script for data processing
>>
>>    training.py: Script for training the final machine learning model
>>
>>    evaluation.py: Script for evaluating model performance
>
> models: Reserved for storing trained models (.pkl) and related files (.yaml configuration files)
>
>>    trained_model.pkl: A file containing a trained machine learning model, followed by an identifier
>>
>>    model_config.yaml: YAML file holding configuration details for the model (with the same identifier)
>
> app: Directory for Streamlit application code.
>
>>    app.py: A Streamlit application for interactive use
>>
>>    requirements.txt: A file specifying dependencies for running the application
>>
>>    resources: other files related to the Streamlit app
>
> docs: Other documentation files.
>
>>    bi.ppt: BI presentation
>>
>>    ds.ppt: Data science technical presentation
>>
>>    memo.md: Project-related notes
    
#### Cheers to Data! 🍻

(Some of the contents of this repository are in Spanish).