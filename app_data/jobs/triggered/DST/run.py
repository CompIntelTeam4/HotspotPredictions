
import pandas as pd
import numpy as numpy
from sklearn import tree
from sklearn.metrics import accuracy_score, adjusted_rand_score, confusion_matrix, precision_recall_fscore_support
from sklearn.model_selection import train_test_split
import time


totalScore = 0
totalMisses = 0
totalFP = 0
totalFN = 0
for i in range(3):

    """
    train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJan2017_wCrimeTallysJan2016-Dec2016.csv')
    train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictFeb2017_wCrimeTallysFeb2016-Jan2017.csv')
    train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictMar2017_wCrimeTallysMar2016-Feb2017.csv')
    train4 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictApr2017_wCrimeTallysApr2016-Mar2017.csv')
    train5 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictMay2017_wCrimeTallysMay2016-Apr2017.csv')

    train6 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJun2017_wCrimeTallysJun2016-May2017.csv')
    train7 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJul2017_wCrimeTallysJul2016-Jun2017.csv')
    train8 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictAug2017_wCrimeTallysAug2016-Jul2017.csv')
    train9 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictSep2017_wCrimeTallysSep2016-Aug2017.csv')
    train10 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2017_wCrimeTallysOct2016-Sep2017.csv')
    train11 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2017_wCrimeTallysNov2016-Oct2017.csv')
    train12 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2017_wCrimeTallysDec2016-Nov2017.csv')"""
    

    """
    xtrain1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJan2018_wCrimeTallysJan2017-Dec2017.csv')
    xtrain2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictFeb2018_wCrimeTallysFeb2017-Jan2018.csv')
    xtrain3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictMar2018_wCrimeTallysMar2017-Feb2018.csv')
    xtrain4 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictApr2018_wCrimeTallysApr2017-Mar2018.csv')
    xtrain5 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictMay2018_wCrimeTallysMay2017-Apr2018.csv')

    xtrain6 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJun2018_wCrimeTallysJun2017-May2018.csv')
    xtrain7 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJul2018_wCrimeTallysJul2017-Jun2018.csv')
    xtrain8 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictAug2018_wCrimeTallysAug2017-Jul2018.csv')
    xtrain9 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictSep2018_wCrimeTallysSep2017-Aug2018.csv')
    xtrain10 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2018_wCrimeTallysOct2017-Sep2018.csv')
    xtrain11 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')
    xtrain12 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')"""
    
    """
    train = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
    test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')"""

    """
    train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
    train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')
    train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2018_wCrimeTallysOct2017-Sep2018.csv')
    train = pd.concat([train1,train2,train3], ignore_index=True)  
    test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')"""

    """
    train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
    train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')
    train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2018_wCrimeTallysOct2017-Sep2018.csv')
    train4 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictSep2018_wCrimeTallysSep2017-Aug2018.csv')
    train5 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictAug2018_wCrimeTallysAug2017-Jul2018.csv')
    train6 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJul2018_wCrimeTallysJul2017-Jun2018.csv')

    train = pd.concat([train1,train2,train3, train4,train5,train6], ignore_index=True)  
    test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')"""

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


    train1 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictDec2018_wCrimeTallysDec2017-Nov2018.csv')
    train2 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictNov2018_wCrimeTallysNov2017-Oct2018.csv')
    train3 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictOct2018_wCrimeTallysOct2017-Sep2018.csv')
    train4 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictSep2018_wCrimeTallysSep2017-Aug2018.csv')
    train5 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictAug2018_wCrimeTallysAug2017-Jul2018.csv')
    train6 = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictJul2018_wCrimeTallysJul2017-Jun2018.csv')

    train = pd.concat([train1,train2,train3, train4,train5,train6], ignore_index=True)  
    test = pd.read_csv('D:\\\\home\\site\\wwwroot\\\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictJan2019_wCrimeTallysJan2018-Dec2018.csv')



    #train = pd.concat([train1,train2,train3,train4,train5,train6,train7,train8,train9,train10,train11,train12], ignore_index=True)  
    #train = pd.concat([train1,train2,train3,train4,train5,train6,train7,train8,train9,train10, train11,train12,
     #           xtrain1,xtrain2,xtrain3,xtrain4,xtrain5,xtrain6,xtrain7,xtrain8,xtrain9,xtrain9,xtrain10,xtrain11,xtrain12], ignore_index=True)    


    #test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDataSets\\predictOct2017_wCrimeTallysOct2016-Sep2017.csv')



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

    #Decision Tree Classifier
    decision_tree = tree.DecisionTreeClassifier(criterion="entropy")



    start = time.time()*1000
    decision_tree = decision_tree.fit(X_train,Y_train)
    end = time.time()*1000

    #print("Training time for decision tree: ", end-start)
    dt_prediction = decision_tree.predict(X_test)
    #Compute the accuracy by comparing the actual values to the prediction values
    score = accuracy_score(Y_test,dt_prediction)

    totalScore += score

    score2 = accuracy_score(Y_test,dt_prediction, normalize=False)
    #print("Accuracy: ", score)
    #print("Misses: ", len(Y_test)-score2)
    con = confusion_matrix(Y_test,dt_prediction)

    totalMisses += len(Y_test)-score2
    totalFP += con[0][1]
    totalFN += con[1][0]



import pickle
pickle.dump(KNN,open("D:\\\\home\\site\\wwwroot\\trained_models\\DST_MODEL_JAN6MONTHS.sav",'wb'))

print("Average accuracy: ", totalScore/3)
print("Average FP", totalFP/3)
print("Average FN", totalFN/3)
print("--final iteration--")
print("accuracy: ", score)
print("Prec, recall, fscore: ", precision_recall_fscore_support(Y_test,dt_prediction,pos_label=1,average='binary'))
con = confusion_matrix(Y_test,dt_prediction)
print(con)

#print(len(Y_test))
#print(Y_test.index.values)
#print(X_test.head())
#print(len(dt_prediction))



pred_series = pd.Series(dt_prediction, index=Y_test.index, name="predictions")

final_output = pd.concat([Y_test,pred_series],axis=1)
final_output.insert(0,'Grid',range(1,1+len(final_output)))
#print(final_output)


final_output.to_csv("D:\\\\home\\site\\wwwroot\\Data\\Crime_data\\Results\\Jan2019_DST_wPredictPrev6Mon.csv",index=False,encoding='utf8')

#Need to add the index as a column for the output and increase by one to get the actual grid

#the mapping CSV file should basically append on hotspot or not to the grid CSV