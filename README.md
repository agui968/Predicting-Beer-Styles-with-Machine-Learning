## Welcome to the Beer Style Prediction Project! 🍻
![img](./docs/charts/aibeer.jpg)

### Project Overview
## (Skip the boring part and try the model yourself [***here***](https://predicting-beer-styles-with-machine-learning.streamlit.app/) (Streamlit app))

This project focuses on classifying beer styles using machine learning techniques. The dataset, obtained from [Brewersfriend.com](https://www.brewersfriend.com), includes various features related to beer recipes. The goal is to build a model that can accurately predict the style of beer based on key attributes such as Alcohol By Volume (ABV), International Bitterness Units (IBU), and Color (SRM), assisting brewers and enthusiasts alike in understanding and categorizing different brews.

### Data Cleaning
The dataset initially contained several columns, but after a thorough analysis using heatmaps with Pearson, Kendall, and Spearman coefficients, irrelevant columns were discarded. The key variables for the model were identified as ABV, IBU, and Color. The beer styles were mapped into six main categories, and duplicate beers were removed to ensure a clean dataset.

+ Comprehensive mapping of beer styles.
+ Removal of duplicate beers.
+ Visualization of variable distributions by beer styles.

### Data Transformation and Visualizations
Outliers were removed, and incorrect values were corrected, leading to clearer visualizations of variable distributions. This step involved setting limits for the Color variable based on the Standard Reference Method (SRM) scale.

+ Removal of outliers.
+ Correction of incorrect values.
+ Visualizations of variable distributions.
### Model Training

#### Logistic Regression
The initial model training involved logistic regression with a focus on balancing classes using RandomUnderSampler. Two scenarios were tested: scaling the data and not scaling it. The chosen target variable for classification was the style code.

+ Logistic regression with class balancing.
+ Testing scenarios with and without data scaling.

#### Grid Searches, Pipelines, and Final Model
Several machine learning models were considered, and two pipelines with Grid Search were implemented to determine the best classification model and parameters. The winning model was the Gradient Boosting Classifier, which showed excellent metrics, especially in terms of F1 score.

+ Implementation of Grid Searches and Pipelines.
+ Selection of the Gradient Boosting Classifier as the final model.

#### Clustering and KMeans

An attempt was made to create an unsupervised learning model using clustering (KMeans). However, the results were not satisfactory, and the project continued with supervised learning.

+ Unsuccessful attempt at clustering using KMeans.

#### Other Tests and Models
Additional pipelines with Grid Search were created to explore alternative models and parameter adjustments. Despite these efforts, the Gradient Boosting Classifier remained the most effective model for beer style classification.

+ Exploration of alternative models.
+ Parameter adjustments for the Gradient Boosting Classifier.

### Conclusion
In conclusion, the Gradient Boosting Classifier, trained without scaling the data, proved to be the most effective model for beer style classification. The detailed analysis and model configurations can be found in the associated Jupyter notebooks. You can also refer to the [notebooks directory](./notebooks/) for a comprehensive view of the project and detailed metrics. The final model parameters are available in [final_model_config.yaml](./models/final_model_config.yaml).
  
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
>>    01_Sources.ipynb: Sources for the data
>>
>>   (02-03)_cleaningEDA.ipynb: Data cleaning and exploratory data analysis
>>
>>   (04-06)_Training_evaluation_(model).ipynb: Model training and evaluation
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

For additional details, explore the project's source code, data processing scripts, and model training and evaluation notebooks. Feel free to refer to the [docs directory](./docs/) for business and data science presentations.
If you want to test the performance of the model and make your own predictions, follow this link to the [**Streamlit app**](https://predicting-beer-styles-with-machine-learning.streamlit.app/).

#### Cheers to Data! 🍻

(Some of the contents of this repository are in Spanish).
