import mysql.connector
from mysql.connector.constants import ClientFlag
import MySQLdb
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta #for calculating time a year ago
import sys
sys.path.insert(1, './GridDetection/FeatureTargetCreation')
sys.path.insert(1, "./MachineLearningAlgos")
import DecisionTreeTestAutomated as DST
import feature_creation_with_near as test
import json

"""
try:
    mydbb = mysql.connector.connect(host="crimewebsitedatabase.mysql.database.azure.com",
                user="lmurdock12@crimewebsitedatabase",
                password="TheCloudtest2019",
                db="crimes",
                port=3306,
                ssl_ca="C:\\\\xampp\\phpMyAdmin\\ssl\\BaltimoreCyberTrustRoot.crt.pem")
except mysql.connector.Error as err:
    print(err)"""





db = MySQLdb.connect(host="crimewebsitedatabase.mysql.database.azure.com",user="lmurdock12",
            passwd='TheCloudtest2019',db="crimes",ssl={"ssl":{"ssl-ca":"C:\\\\xampp\\phpMyAdmin\\ssl\\BaltimoreCyberTrustRoot.crt.pem"}})



#yesterday = (datetime.now()-timedelta(1)).strftime('%Y-%m-%d')
#yesterday = (datetime.now()-timedelta(1))
yesterday = (datetime.now()-relativedelta(years=1))
yesterday = str(yesterday).split(' ')[0] #Convert datetime object to string and just take the date without time
print(str(yesterday).split(' ')[0])

sql = "SELECT * FROM incidents WHERE incident_occured >= '" + yesterday + "'" 

#sql = "SELECT * FROM incidents WHERE incident_occured >= '"


print("Creating and sending the sql query...")
df = pd.read_sql(sql,db)
print(df)
print("Creating the featureset...")
#Create and return the datafrrame
featuresetDF = test.createFeatureset_wDataframe("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\Grid_with_neighbors.csv",
       df,"C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\crimeTallys\\ALGOTEST.csv")


#featuresetDF = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\crimeTallys\\crime_tallys_2016_withNear.csv")
#print(featuresetDF.shape)
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
    if i%1000 ==0:
        print("on row: ", i)
    json_decoded['data']['features'][i]['properties']['ActualHot'] = 0
    json_decoded['data']['features'][i]['properties']['PredictHot'] = int(resultsDF[i])

with open("KNN_GEO.json", 'w') as json_file:
    json.dump(json_decoded, json_file)


print("process complete")