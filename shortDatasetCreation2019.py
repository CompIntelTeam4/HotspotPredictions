import pandas as pd
import sys
from datetime import datetime, timedelta
import subprocess
import json 
import mysql.connector
from mysql.connector.constants import ClientFlag
import MySQLdb
from dateutil.relativedelta import relativedelta #for calculating time a year ago
sys.path.insert(1, 'C:\\\\xampp\\htdocs\\HotspotPredictions\\GridDetection\\FeatureTargetCreation')
sys.path.insert(1, "./MachineLearningAlgos")

import feature_creation_with_near as fc
import target_column_creation as targetCreationFunc
sys.path.insert(1, 'C:\\\\xampp\\htdocs\\HotspotPredictions\\GridDetection')
import appendGridNumToCrimeData as test
import time
import calendar 

try:
    db = mysql.connector.connect(host="crimewebsitedatabase.mysql.database.azure.com",
                user="lmurdock12@crimewebsitedatabase",
                password="TheCloudtest2019",
                db="crimes",
                port=3306,
                ssl_ca="C:\\\\xampp\\phpMyAdmin\\ssl\\BaltimoreCyberTrustRoot.crt.pem")
except mysql.connector.Error as err:
    print(err)
"""
db = MySQLdb.connect(host="crimewebsitedatabase.mysql.database.azure.com",user="lmurdock12",
            passwd='TheCloudtest2019',db="crimes",ssl={"ssl":{"ssl-ca":"C:\\\\xampp\\phpMyAdmin\\ssl\\BaltimoreCyberTrustRoot.crt.pem"}})"""



dateMap = {'Jan':'Dec','Feb':'Jan','Mar':'Feb','Apr':'Mar','May':'Apr','Jun':'May','Jul':'Jun','Aug':'Jul','Sep':'Aug','Oct':'Sep','Nov':'Oct',
            'Dec':'Nov'}


dates = [2017,2018,2019]

for j in range(len(dates)):

    for i in range(1,13):
        month_index = calendar.month_abbr[i]


        targ = month_index
        targ_index = list(calendar.month_abbr).index(targ)
        feature = dateMap[targ]

        print("Hot: " + targ + " and feature: " + feature + ", ")


        try:
            db = mysql.connector.connect(host="crimewebsitedatabase.mysql.database.azure.com",
                        user="lmurdock12@crimewebsitedatabase",
                        password="TheCloudtest2019",
                        db="crimes",
                        port=3306,
                        ssl_ca="C:\\\\xampp\\phpMyAdmin\\ssl\\BaltimoreCyberTrustRoot.crt.pem")
        except mysql.connector.Error as err:
            print(err)



        if targ == "Jan":



            start = time.time()*1000

            rawTargetCSVpath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\rawCrimes\\" + targ + str(dates[j]) + "Crimes.csv" #Jan2019Crimes.csv"
            rawsFeatureCSVpath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\rawCrimes\\" + feature + str(dates[j]-1) + "Crimes.csv" #Dec2018Crimes.csv"

            hotspotCSVpath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\hotspotTallys\\" + targ + str(dates[j]) + ".csv" #Jan2019.csv"
            crimeTallysPath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\crimeTallys\\" + feature + str(dates[j]-1) + ".csv" #  "Dec2018tally.csv"
            completedSetPath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predict" + targ + str(dates[j]) + "_wCrimeTallys" + feature + str(dates[j]-1) + ".csv" # Jan2018_wCrimeTallysDec2018.csv"
            


            targMonth = targ_index
            targYear = dates[j]
            targDay = 1
        else: 

            start = time.time()*1000

            rawTargetCSVpath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\rawCrimes\\" + targ + str(dates[j]) + "Crimes.csv" #Jan2019Crimes.csv"
            rawsFeatureCSVpath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\rawCrimes\\" + feature + str(dates[j]) + "Crimes.csv" #Dec2018Crimes.csv"

            hotspotCSVpath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\hotspotTallys\\" + targ + str(dates[j]) + ".csv" #Jan2019.csv"
            crimeTallysPath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\crimeTallys\\" + feature + str(dates[j]-1) + ".csv" #  "Dec2018tally.csv"
            completedSetPath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\readyDatasets\\predict" + targ + str(dates[j]) + "_wCrimeTallys" + feature + str(dates[j]-1) + ".csv" # Jan2018_wCrimeTallysDec2018.csv"


            targMonth = targ_index
            targYear = dates[j]
            targDay = 1



        date = datetime(targYear,targMonth,targDay)
        print("Targ date is: ", str(date))

        startDate = (date-relativedelta(days=30))

        endDate = str(targYear) + "-" + str(targMonth) + "-" + str(targDay) + " 00:00:00"
        print("start query: " + str(startDate) + ", end query: " + endDate)


        

        sql1 = "SELECT * FROM incidents WHERE MONTH(incident_occured) = " + str(targMonth) + " and YEAR(incident_occured) = " + str(targYear)  
        sql2 = "SELECT * FROM incidents WHERE incident_occured >= '" + str(startDate) + "' and incident_occured < '" + endDate + "'"

        #print("Hotspot SQL: ", sql1)
        #print("Featureset SQL: ", sql2)

        """
        testdf = pd.read_sql(sql1,db)
        testdf2 = pd.read_sql(sql2, db)
        result = pd.concat([testdf,testdf2]).drop_duplicates(keep=False)
        print("diff: ")
        print(result)
        print("---")"""


        print("Getting the SQL query")
        targetDataDF = pd.read_sql(sql1,db)
        featureDF = pd.read_sql(sql2,db)
        print("Crimes for target year: ", targetDataDF.shape)
        print("Crimes in last year: ", featureDF.shape)

        #print(featureDF)

        featureDF.to_csv(rawsFeatureCSVpath,index=False,encoding='utf8')
        targetDataDF.to_csv(rawTargetCSVpath,index=False,encoding='utf8')

        print("Creating the target column")
        targetDF = targetCreationFunc.targetCreation_wDF("C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\Grid_with_neighbors.csv", targetDataDF,hotspotCSVpath,targMonth)
        #targetDF = pd.read_csv("C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\ShortDatasets\\hotspotTallys\\Jan2019.csv")
        print("Creating the featureset...")
        #Create and return the datafrrame
        featuresetDF = fc.createFeatureset_wDataframe_Short("C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\Grid_with_neighbors.csv",
            featureDF,crimeTallysPath,targDay,targMonth,targYear)


        #print(targetDF)

        #print(featuresetDF)

        featuresetDF['Hotspot'] = targetDF['Hotspot']
        #print("Updated:")
        #print(featuresetDF)

        print("Exporting completed file to CSV...")
        featuresetDF.to_csv(completedSetPath,index=False,encoding='utf8')

        end = time.time()*1000
        print("Time took: ", end-start)
    


"""

print("Training the dataset")
resultsDF = DST.trainData(featuresetDF,"./trained_models/DST_saved_model.sav")
print(resultsDF.shape)


#Call the machine learning algorithm and get the dataframe
#and use the following script below
#Then reload user to new page and display the map
#Convert the JSON file to the type needed

print("Exporting to geojson to upload on map")
with open('C:\\\\xampp\\htdocs\\HotspotPredictions\\CrimeWebsite\\geojsonTest.json') as json_file:
    json_decoded = json.load(json_file)

for i in range(len(json_decoded['data']['features'])):
#for i in range(len(100)):
    if i%1000 ==0:
        print("on row: ", i)
    json_decoded['data']['features'][i]['properties']['ActualHot'] = 0
    json_decoded['data']['features'][i]['properties']['PredictHot'] = int(resultsDF[i])

with open("KNN_GEO.json", 'w') as json_file:
    json.dump(json_decoded, json_file)


print("process complete")"""
