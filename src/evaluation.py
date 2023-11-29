from time import sleep
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pickle
from sklearn.metrics import (precision_score,recall_score,
                             f1_score, accuracy_score,confusion_matrix)

# #IMPORT THE TRAINED MODEL
with open('..\\models\\final_model_gbc.pkl', 'rb') as input:
    model = pickle.load(input) 
#importing test    
test=pd.read_csv('..\\data\\test\\test.csv',index_col=0)
colorcode=pd.read_csv('../data/processed/color_code.csv',index_col=0)


X_test=test[['ABV','IBU','Color']]
y_test=test['Style_color']

# #PREDICT WITH THE MODEL
y_pred=model.predict(X_test)

print('Metrics overview:')
sleep(0.75)
print('\n')
print('Accuracy_score:',accuracy_score(y_pred,y_test))
print('\n')
sleep(0.25)
print('Precision_score:',precision_score(y_pred,y_test, average='weighted'))
print('\n')
sleep(0.25)
print('F1_score:',f1_score(y_pred,y_test, average='weighted'))
print('\n')
sleep(0.25)
print('Recall_score:',recall_score(y_pred,y_test, average='weighted'))

precision = precision_score(y_test, y_pred, average=None)
recall = recall_score(y_test, y_pred, average=None)
f1 = f1_score(y_test, y_pred, average=None)
accuracy = accuracy_score(y_pred,y_test)
sleep(0.5)
print('\n')
print('*'*50)

class_mapping = colorcode[['Color_code', 'Style']]

metrics_df = pd.DataFrame({
    'Precision': precision,
    'Recall': recall,
    'F1-Score': f1,
    'Accuracy': accuracy
}, index=class_mapping['Style'])
sleep(0.5)
print('\n')
print('Detailed metrics:')
sleep(0.75)
print(metrics_df)
sleep(0.25)
print('\n')
print('Exporting to csv file in src folder. Close the image to finish.')
metrics_df.to_csv('metrics.csv',)

cm = confusion_matrix(y_test, y_pred,normalize='true')
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, linewidths=.5, square = True, cmap = 'YlOrBr')
plt.ylabel('Actual style')
plt.xlabel('Predicted style')
all_sample_title = (f'Precision: {precision_score(y_test, y_pred, average="weighted")}\nRecall:{recall_score(y_test, y_pred, average="weighted")}\nF1:{f1_score(y_test, y_pred, average="weighted")}')
plt.title(all_sample_title, size = 10);
plt.xticks(ticks=range(len(colorcode.index)), labels=colorcode['Style'], rotation=55,fontsize=8);
plt.yticks(ticks=range(len(colorcode.index)), labels=colorcode['Style'],rotation=25,fontsize=8);
plt.show()
sleep(0.25)
print('\n')
print('Done')