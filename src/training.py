import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier


beer=pd.read_csv('..\\data\\processed\\clean_limited.csv',index_col=0)
# beer.drop(columns='Style_ibu',inplace=True)

train,test=train_test_split(beer,test_size=0.25,random_state=42)

#exporting train & test
# train.to_csv('..\\data\\train\\train.csv')
# test.to_csv('..\\data\\test\\test.csv')

# importing train
# train=pd.read_csv('..\\data\\train\\train.csv',index_col=0)

X_train=train[['ABV','IBU','Color']]
y_train=train['Style_color']

rus = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = rus.fit_resample(X_train, y_train)

#IMPORT THE TRAINED MODEL
with open('..\\models\\best_trained_model_gbc.pkl', 'rb') as input:
    model = pickle.load(input) 

#TRAIN THE MODEL
model.fit(X_resampled, y_resampled)

#EXPORT THE MODEL
with open('..\\models\\best_trained_model_gbc.pkl', 'wb') as output:
    pickle.dump(model, output)