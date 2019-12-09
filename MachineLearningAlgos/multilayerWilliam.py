
import pandas as pd
import numpy as numpy
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, adjusted_rand_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import time

                    #C:\Users\Lucian Murdock\Desktop\Computational_Intelligence\Crime_Prediction\Data\Crime_Data\ReadyDataSets
train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')
train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2018_wCrimeTallysOct2017-Sep2018.csv')
train4 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictSep2018_wCrimeTallysSep2017-Aug2018.csv')
train5 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictAug2018_wCrimeTallysAug2017-Jul2018.csv')
train6 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJul2018_wCrimeTallysJul2017-Jun2018.csv')

train = pd.concat([train1,train2,train3, train4,train5,train6], ignore_index=True)  
test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')


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
MLP = MLPClassifier(hidden_layer_sizes=(15,30,15))



start = time.time()*1000
MLP = MLP.fit(X_train,Y_train)
end = time.time()*1000
acc=0
fp=0
fn=0
misses=0
for i in range(1):
#print("Training time for Multilayer Perceptron: ", end-start)
    MLP = MLP.fit(X_train,Y_train)
    MLP_prediction = MLP.predict(X_test)
#Compute the accuracy by comparing the actual values to the prediction values
    score = accuracy_score(Y_test,MLP_prediction)
    score2 = accuracy_score(Y_test,MLP_prediction, normalize=False)
    con= confusion_matrix(Y_test,MLP_prediction)
    pre=precision_recall_fscore_support(Y_test,MLP_prediction,pos_label=1,average='binary')
    acc=acc+score
    misses+=len(Y_test)-score2
    fp+=con[0][1]
    fn+=con[1][0]
print("Pre: ",pre)
#print("F1: ", f1)
#print("Recall: ", re)
print("Accuracy: ", acc/1)
print("misses: ",misses/1)
print("fp: ", fp/1)
print("fn: ", fn/1)
print("Accurcay was: ",score)
print(con)


#print(len(Y_test))
#print(Y_test.index.values)
#print(X_test.head())
#print(len(dt_prediction))



pred_series = pd.Series(MLP_prediction, index=Y_test.index, name="predictions")

final_output = pd.concat([Y_test,pred_series],axis=1)
final_output.insert(0,'Grid',range(1,1+len(final_output)))
#print(final_output)


#final_output.to_csv("C:\\Users\\willi\\Documents\\Data\\MLP.csv",index=False,encoding='utf8')


#Need to add the index as a column for the output and increase by one to get the actual grid

#the mapping CSV file should basically append on hotspot or not to the grid CSV
