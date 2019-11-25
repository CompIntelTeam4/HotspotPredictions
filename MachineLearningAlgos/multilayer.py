
import pandas as pd
import numpy as numpy
from sklearn import tree
from sklearn.metrics import accuracy_score, adjusted_rand_score
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import time

                    #C:\Users\Lucian Murdock\Desktop\Computational_Intelligence\Crime_Prediction\Data\Crime_Data\ReadyDataSets
train = pd.read_csv('C:\\Users\\willi\\Documents\\Data\\crime_tallys_2016_withNear.csv')
test = pd.read_csv('C:\\Users\\willi\\Documents\\Data\\crime_tallys_2017_withNear.csv')


#Remove the Grid column in the data sets and use indices instead to keep track of the grids
train.pop('Grid')
test.pop('Grid')
#Remove all the rows with entire row being 0 --This should keep proper indices
#train = train[(train.T != 0).any()]
#test = test[(test.T != 0).any()]

#Get the Y values
Y_train = train.pop('Hotspot')
X_train = train
Y_test = test.pop('Hotspot')
X_test = test
#This was used when only using one dataset
#X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.05)

#3445 grids total
#1505 have actual values
#O index is the index of the 1st grid

#KNearestNeighbors Tree Classifier
MLP = MLPClassifier(
                    hidden_layer_sizes=(12,))



start = time.time()*1000
MLP = MLP.fit(X_train,Y_train)
end = time.time()*1000

print("Training time for Multilayer Perceptron: ", end-start)
MLP_prediction = MLP.predict(X_test)
#Compute the accuracy by comparing the actual values to the prediction values
score = accuracy_score(Y_test,MLP_prediction)
score2 = accuracy_score(Y_test,MLP_prediction, normalize=False)
print("Accuracy: ", score)
print("Misses: ", len(Y_test)-score2)


#print(len(Y_test))
#print(Y_test.index.values)
#print(X_test.head())
#print(len(dt_prediction))



pred_series = pd.Series(MLP_prediction, index=Y_test.index, name="predictions")

final_output = pd.concat([Y_test,pred_series],axis=1)
final_output.insert(0,'Grid',range(1,1+len(final_output)))
#print(final_output)


final_output.to_csv("C:\\Users\\willi\\Documents\\Data\\KNNinitial2017Test.csv",index=False,encoding='utf8')

#Need to add the index as a column for the output and increase by one to get the actual grid

#the mapping CSV file should basically append on hotspot or not to the grid CSV
