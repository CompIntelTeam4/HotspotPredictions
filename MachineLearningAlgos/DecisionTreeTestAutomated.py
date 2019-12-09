
import pandas as pd
import numpy as numpy
from sklearn import tree
from sklearn.metrics import accuracy_score, adjusted_rand_score
from sklearn.model_selection import train_test_split
import time
import pickle


def trainData(inputDF, model):

    #test = pd.read_csv('C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\crimeTallys\\crime_tallys_2017_withNear.csv')
    #test = pd.read_csv(input_csv)
    test = inputDF

    #Drop the grid and hotspot columns
    test.pop('Grid')
    test.pop('Hotspot')


    #Remove all the rows with entire row being 0 --This should keep proper indices
    #test = test[(test.T != 0).any()]

    #Set X to the featureset (week, month, year, near(entire year))
    X = test
    #Import the saved model to use to make predictions
    #saved_model = "./trained_models/DST_saved_model.sav"
    decision_tree = pickle.load(open(model,'rb'))

    #Make the predictions
    dt_prediction = decision_tree.predict(X)

    #Export the results 
    pred_series = pd.Series(dt_prediction,name="predictions")

    #final_output = pd.concat([Y_test,pred_series],axis=1)
    return pred_series
    #pred_series.to_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_prediction\\Data\\Crime_data\\Results\\TESTTTT.csv",index=True,encoding='utf8',header="predictions")
