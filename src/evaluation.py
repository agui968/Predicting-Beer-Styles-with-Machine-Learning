import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yaml
import os
import pickle
from sklearn.metrics import (precision_score,recall_score,
                             f1_score, accuracy_score,confusion_matrix, classification_report)

# #IMPORT THE TRAINED MODEL
with open('..\\models\\best_trained_model_gbc.pkl', 'rb') as input:
    model = pickle.load(input) 
#importing test    
test=pd.read_csv('..\\data\\test\\test.csv',index_col=0)

X_test=test[['ABV','IBU','Color']]
y_test=test['Style_color']

# #PREDICT WITH THE MODEL
y_pred=model.predict(X_test)

print('accuracy_score',accuracy_score(y_pred,y_test))
print('precision_score',precision_score(y_pred,y_test, average='weighted'))
print('f1_score',f1_score(y_pred,y_test, average='weighted'))
print('recall_score',recall_score(y_pred,y_test, average='weighted'))
# print(classification_report(yc_test, predictions))

cm = confusion_matrix(y_test, y_pred,normalize='true')
print(cm)