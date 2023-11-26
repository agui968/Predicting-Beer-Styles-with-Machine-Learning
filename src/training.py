import pandas as pd
import pickle
from time import sleep
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler

print('Reading the dataset...')
beer=pd.read_csv('..\\data\\processed\\final_dataset.csv',index_col=0)
# beer.drop(columns='Style_ibu',inplace=True)
sleep(0.75)
print('\n')
print('Generating train and test...')
train,test=train_test_split(beer,test_size=0.25,random_state=42)
sleep(0.75)
print('\n')
print('Exporting train and test...')

#exporting train & test
train.to_csv('..\\data\\train\\train.csv')
test.to_csv('..\\data\\test\\test.csv')
sleep(0.75)
print('\n')

# importing train
# train=pd.read_csv('..\\data\\train\\train.csv',index_col=0)

X_train=train[['ABV','IBU','Color']]
y_train=train['Style_color']

print('Balancing train classes...')
rus = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = rus.fit_resample(X_train, y_train)
sleep(0.75)
print('\n')
print('Importing the model...')
#IMPORT THE TRAINED MODEL
with open('..\\models\\best_trained_model_gbc.pkl', 'rb') as input:
    model = pickle.load(input) 
sleep(0.75)
print('\n')
print('Training the model...')
#TRAIN THE MODEL
model.fit(X_resampled, y_resampled)
print('\n')
print('Exporting the model...')
#EXPORT THE MODEL
with open('..\\models\\best_trained_model_gbc.pkl', 'wb') as output:
    pickle.dump(model, output)
sleep(0.8)
print('\n')
print('Done')
#You can now head on to 'evaluation.py'