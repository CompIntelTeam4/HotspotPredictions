
import pandas as pd
import numpy as numpy
from sklearn import tree
from sklearn.metrics import accuracy_score, adjusted_rand_score, confusion_matrix, precision_recall_fscore_support
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import time

                    #C:\Users\Lucian Murdock\Desktop\Computational_Intelligence\Crime_Prediction\Data\Crime_Data\ReadyDataSets
"""
train = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')
"""
"""
train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')
train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2018_wCrimeTallysOct2017-Sep2018.csv')
train = pd.concat([train1,train2,train3], ignore_index=True)  
test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')"""


train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')
train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2018_wCrimeTallysOct2017-Sep2018.csv')
train4 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictSep2018_wCrimeTallysSep2017-Aug2018.csv')
train5 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictAug2018_wCrimeTallysAug2017-Jul2018.csv')
train6 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJul2018_wCrimeTallysJul2017-Jun2018.csv')

train = pd.concat([train1,train2,train3, train4,train5,train6], ignore_index=True)  
test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')


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



"""
train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2019_wCrimeTallysOct2018-Sep2019.csv')
train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictSep2019_wCrimeTallysSep2018-Aug2019.csv')
train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictAug2019_wCrimeTallysAug2018-Jul2019.csv')
train4 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJul2019_wCrimeTallysJul2018-Jun2019.csv')
train5 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJun2019_wCrimeTallysJun2018-May2019.csv')
train6 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictMay2019_wCrimeTallysMay2018-Apr2019.csv')
train7 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictApr2019_wCrimeTallysApr2018-Mar2019.csv')
train8 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictMar2019_wCrimeTallysMar2018-Feb2019.csv')
train9 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictFeb2019_wCrimeTallysFeb2018-Jan2019.csv')
train10 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')
train11 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
train12 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')


train = pd.concat([train1,train2,train3, train4,train5,train6,train7,train8,train9,train10,train11,train12], ignore_index=True)  
test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictNov2019_wCrimeTallysNov2018-Oct2019.csv')
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
KNN = KNeighborsClassifier(n_neighbors=35)



start = time.time()*1000
KNN = KNN.fit(X_train,Y_train)
end = time.time()*1000


KNN_prediction = KNN.predict(X_test)
#Compute the accuracy by comparing the actual values to the prediction values
score = accuracy_score(Y_test,KNN_prediction)
score2 = accuracy_score(Y_test,KNN_prediction, normalize=False)



pred_series = pd.Series(KNN_prediction, index=Y_test.index, name="predictions")

final_output = pd.concat([Y_test,pred_series],axis=1)
final_output.insert(0,'Grid',range(1,1+len(final_output)))


print("--final iteration--")
print("accuracy: ", score)
print("Prec, recall, fscore: ", precision_recall_fscore_support(Y_test,KNN_prediction,pos_label=1,average='binary'))
con = confusion_matrix(Y_test,KNN_prediction)
print(con)



#print(final_output)


final_output.to_csv("C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\Results\\Jan2019_KNN_wPredictPrev6Mon.csv",index=False,encoding='utf8')

#Need to add the index as a column for the output and increase by one to get the actual grid

#the mapping CSV file should basically append on hotspot or not to the grid CSV