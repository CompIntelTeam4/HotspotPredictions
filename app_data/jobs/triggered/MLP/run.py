



import sys
site_packages = "D:\\\\home\\site\\wwwroot\\env\\Lib\\site-packages"
sys.path.append(site_packages)


import pandas as pd
import numpy as numpy
from sklearn import tree
from sklearn.metrics import accuracy_score, adjusted_rand_score, confusion_matrix, precision_recall_fscore_support
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import time

                    #C:\Users\Lucian Murdock\Desktop\Computational_Intelligence\Crime_Prediction\Data\Crime_Data\ReadyDataSets

"""
train = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')"""


"""
train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')
train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2018_wCrimeTallysOct2017-Sep2018.csv')
train = pd.concat([train1,train2,train3], ignore_index=True)  
test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')"""




train1 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
train2 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')
train3 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2018_wCrimeTallysOct2017-Sep2018.csv')
train4 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictSep2018_wCrimeTallysSep2017-Aug2018.csv')
train5 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictAug2018_wCrimeTallysAug2017-Jul2018.csv')
train6 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJul2018_wCrimeTallysJul2017-Jun2018.csv')

train = pd.concat([train1,train2,train3, train4,train5,train6], ignore_index=True)  
test = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')


"""

train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')
train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2018_wCrimeTallysOct2017-Sep2018.csv')
train4 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictSep2018_wCrimeTallysSep2017-Aug2018.csv')
train5 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictAug2018_wCrimeTallysAug2017-Jul2018.csv')
train6 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJul2018_wCrimeTallysJul2017-Jun2018.csv')
train7 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJun2018_wCrimeTallysJun2017-May2018.csv')
train8 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictMay2018_wCrimeTallysMay2017-Apr2018.csv')
train9 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictApr2018_wCrimeTallysApr2017-Mar2018.csv')
train10 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictMar2018_wCrimeTallysMar2017-Feb2018.csv')
train11 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictFeb2018_wCrimeTallysFeb2017-Jan2018.csv')
train12 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJan2018_wCrimeTallysJan2017-Dec2017.csv')


train = pd.concat([train1,train2,train3, train4,train5,train6,train7,train8,train9,train10,train11,train12], ignore_index=True)  
test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')
"""

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
MLP = MLPClassifier(alpha=.001,hidden_layer_sizes=(15,30,15))



start = time.time()*1000
MLP = MLP.fit(X_train,Y_train)
end = time.time()*1000


MLP_prediction = MLP.predict(X_test)
#Compute the accuracy by comparing the actual values to the prediction values
score = accuracy_score(Y_test,MLP_prediction)
score2 = accuracy_score(Y_test,MLP_prediction, normalize=False)





pred_series = pd.Series(MLP_prediction, index=Y_test.index, name="predictions")

final_output = pd.concat([Y_test,pred_series],axis=1)
final_output.insert(0,'Grid',range(1,1+len(final_output)))
#print(final_output)


import pickle
pickle.dump(KNN,open("D:\\\\home\\site\\wwwroot\\trained_models\\MLP_MODEL_JAN6MONTHS.sav",'wb'))


print("--final iteration--")
print("accuracy: ", score)
print("Prec, recall, fscore: ", precision_recall_fscore_support(Y_test,MLP_prediction,pos_label=1,average='binary'))
con = confusion_matrix(Y_test,MLP_prediction)
print(con)

final_output.to_csv("D:\\\\home\\site\\wwwroot\\Data\\Crime_data\\Results\\Jan2019_MLP_wPredictPrev6Mon.csv",index=False,encoding='utf8')




#Need to add the index as a column for the output and increase by one to get the actual grid

#the mapping CSV file should basically append on hotspot or not to the grid CSV
