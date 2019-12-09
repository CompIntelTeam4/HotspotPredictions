
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
                    #C:\Users\Lucian Murdock\Desktop\Computational_Intelligence\Crime_Prediction\Data\Crime_Data\ReadyDataSets

    """
    train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictDec2018_wCrimeTallysNov2017.csv')
    train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictNov2018_wCrimeTallysOct2017.csv')
    train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictOct2018_wCrimeTallysSep2017.csv')
    train = pd.concat([train1,train2,train3],ignore_index=True)
    test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDataSets\\predictJan2019_wCrimeTallysDec2018.csv')
    """

    """
    train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictDec2018_wCrimeTallysNov2017.csv')
    train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictNov2018_wCrimeTallysOct2017.csv')
    train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictOct2018_wCrimeTallysSep2017.csv')
    train4 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictSep2018_wCrimeTallysAug2017.csv')
    train5 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictAug2018_wCrimeTallysJul2017.csv')
    train6 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictJul2018_wCrimeTallysJun2017.csv')

    train = pd.concat([train1,train2,train3,train4,train5,train6],ignore_index=True)
    test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDataSets\\predictJan2019_wCrimeTallysDec2018.csv')"""
    

    
    train1 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictDec2018_wCrimeTallysNov2017.csv')
    train2 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictNov2018_wCrimeTallysOct2017.csv')
    train3 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictOct2018_wCrimeTallysSep2017.csv')
    train4 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictSep2018_wCrimeTallysAug2017.csv')
    train5 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictAug2018_wCrimeTallysJul2017.csv')
    train6 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictJul2018_wCrimeTallysJun2017.csv')
    train7 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictJun2018_wCrimeTallysMay2017.csv')
    train8 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictMay2018_wCrimeTallysApr2017.csv')
    train9 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictApr2018_wCrimeTallysMar2017.csv')
    train10 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictMar2018_wCrimeTallysFeb2017.csv')
    train11 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictFeb2018_wCrimeTallysJan2017.csv')
    train12 = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predictJan2017_wCrimeTallysDec2016.csv')


    train = pd.concat([train1,train2,train3,train4,train5,train6,train7,train8,train9,train10,train11, train12],ignore_index=True)
    test = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDataSets\\predictJan2019_wCrimeTallysDec2018.csv')



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


print("Average accuracy: ", totalScore/3)
print("Average FP", totalFP/3)
print("Average FN", totalFN/3)
print("--final iteration--")
print("accuracy: ", score)
print("Prec, recall, fscore: ", precision_recall_fscore_support(Y_test,dt_prediction,pos_label=1,average='binary'))
con = confusion_matrix(Y_test,dt_prediction)
print(con)



pred_series = pd.Series(dt_prediction, index=Y_test.index, name="predictions")

final_output = pd.concat([Y_test,pred_series],axis=1)
final_output.insert(0,'Grid',range(1,1+len(final_output)))
#print(final_output)


final_output.to_csv("C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\Results\\Jan2019_DST_wPredictPrev12MonthSHORT.csv",index=False,encoding='utf8')

#Need to add the index as a column for the output and increase by one to get the actual grid

#the mapping CSV file should basically append on hotspot or not to the grid CSV