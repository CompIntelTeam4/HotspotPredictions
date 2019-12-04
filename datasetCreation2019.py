import pandas as pd
import sys
from datetime import datetime, timedelta
import subprocess
import json 
import mysql.connector
from mysql.connector.constants import ClientFlag
import MySQLdb
from dateutil.relativedelta import relativedelta #for calculating time a year ago
sys.path.insert(1, './GridDetection/FeatureTargetCreation')
sys.path.insert(1, "./MachineLearningAlgos")
import DecisionTreeTestAutomated as DST
import feature_creation_with_near as fc
import target_column_creation as targetCreationFunc
sys.path.insert(1, './GridDetection')
import appendGridNumToCrimeData as test


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



rawTargetCSVpath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\rawCrimes\\Feb2019Crimes.csv"
rawsFeatureCSVpath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\rawCrimes\\Feb2018-Jan2018Crimes.csv"

hotspotCSVpath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\hotspotTallys\\Feb2019.csv"
crimeTallysPath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\crimeTallys\\Feb2018-Jan2019tally.csv"
completedSetPath = "C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\PastDatasets\\readyDatasets\\predictFeb2019_wCrimeTallysFeb2018-Jan2019.csv"
targMonth = 2
targYear = 2019
targDay = 1

startDate = str(targYear-1) + "-" + str(targMonth) + "-" + str(targDay) + " 00:00:00"
endDate = str(targYear) + "-" + str(targMonth) + "-" + str(targDay) + " 00:00:00"
print(startDate)
print(endDate)


sql1 = "SELECT * FROM incidents WHERE MONTH(incident_occured) = " + str(targMonth) + " and YEAR(incident_occured) = " + str(targYear)  
sql2 = "SELECT * FROM incidents WHERE incident_occured >= '" + startDate + "' and incident_occured < '" + endDate + "'"



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
#print(featureDF)

print("Creating the target column")
targetDF = targetCreationFunc.targetCreation_wDF("C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\Grid_with_neighbors.csv", targetDataDF,hotspotCSVpath,targMonth)

print("Creating the featureset...")
#Create and return the datafrrame
featuresetDF = fc.createFeatureset_wDataframe_wDate("C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\Grid_with_neighbors.csv",
       featureDF,crimeTallysPath,targDay,targMonth,targYear)


print(targetDF)

print(featuresetDF)

featuresetDF['Hotspot'] = targetDF['Hotspot']
print("Updated:")
print(featuresetDF)


featuresetDF.to_csv(completedSetPath,index=False,encoding='utf8')

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
