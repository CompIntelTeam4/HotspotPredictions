
import pandas as pd
import numpy as numpy
from sklearn import tree
from sklearn.metrics import accuracy_score, adjusted_rand_score
from sklearn.model_selection import train_test_split
import time


train = pd.read_csv('C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\crime_tallys_2017.csv')


train.pop('Grid')
#Remove all the rows with entire row being 0 --This should keep proper indices
train = train[(train.T != 0).any()]

#Get the Y values
Y = train.pop('Hotspot')
X = train

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.05)

#3445 grids total
#1505 have actual values
#O index is the index of the 1st grid

#Decision Tree Classifier
decision_tree = tree.DecisionTreeClassifier(criterion="entropy")



start = time.time()*1000
decision_tree = decision_tree.fit(X_train,Y_train)
end = time.time()*1000

print("Training time for decision tree: ", end-start)
dt_prediction = decision_tree.predict(X_test)
#Compute the accuracy by comparing the actual values to the prediction values
score = accuracy_score(Y_test,dt_prediction)
score2 = accuracy_score(Y_test,dt_prediction, normalize=False)
print("Accuracy: ", score)
print("Misses: ", len(Y_test)-score2)


#print(len(Y_test))
#print(Y_test.index.values)
#print(X_test.head())
#print(len(dt_prediction))

#Y_test['e'] = pd.Series(0,index=Y_test.index)
#Y_test['test'] = 0

pred_series = pd.Series(dt_prediction, index=Y_test.index, name="predictions")

final_output = pd.concat([Y_test,pred_series],axis=1)
#print(final_output)


final_output.to_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_prediction\\Data\\Crime_data\\DST.csv",index=True,encoding='utf8')

#Need to add the index as a column for the output and increase by one to get the actual grid

#the mapping CSV file should basically append on hotspot or not to the grid CSV