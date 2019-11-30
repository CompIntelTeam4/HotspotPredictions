import pandas as pd
import sys
from sodapy import Socrata
from datetime import datetime, timedelta
import subprocess
import json 

sys.path.insert(1, './GridDetection')
import appendGridNumToCrimeData as test
#d = datetime.today()
#d.month
#d.day


yesterday = (datetime.now()-timedelta(2)).strftime('%Y-%m-%d')


queryStart = yesterday + 'T00:00:00.000'
print(queryStart)
queryEnd = yesterday + 'T23:59:59.000'
print(queryEnd)

query = "incident_occurred between '" + queryStart + "' and '" + queryEnd + "' and (offense_nibrs='13A' or offense_nibrs='13B' or offense_nibrs='13C') and latitude IS NOT NULL and longitude IS NOT NULL"
print(query)    


#Connect to the socrata client with the proper URL and unique ID
client = Socrata("data.nashville.gov", "ILX2dDLI7jQunnJRUeEEcVEim")
#Nashville crime incident API 2019
client_id = "a88c-cc2y"

#Print out the columns titles in the dataset
#metadata = client.get_metadata(client_id)
#for x in metadata['columns']:
    #print(x['name'])


#November 20th 2019
#Query all the crimes within the last day and store in variable

print("Getting the API query for: " + yesterday)
results = client.get(client_id, where=query)
print("Length of query: " + str(len(results)))


#Convert the results into a pandas dataframe.
results_df = pd.DataFrame.from_records(results)
#print(results_df[['incident_occurred']])

print("Appending the grid number to each crime...")
#Run the dataframe through appendGrid function to add grid number to each crime
crime_wGrid = test.append_grid_wDataframe('Grid_with_neighbors.csv', results_df)


print("Exporting the crimes to temporary CSV...")
#Export the file to temporary CSV to be opened by PHP file and uploaded to database
tempCSV = "C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_prediction\\Data\\Crime_data\\tempData\\crime_wGrid_" + yesterday + ".csv"
crime_wGrid.to_csv(tempCSV,index=False,encoding='utf8')
results_df.to_csv("gridtest.csv",index=False,encoding='utf8')

#Call database upload script and upload all the crimes from yesterday's date
print("Starting database upload: ")
proc = subprocess.Popen("php C:\\\\xampp\\htdocs\\HotspotPredictions\\databaseUpload.php", shell=True, stdout=subprocess.PIPE)
script_response = str(proc.stdout.read())

print(script_response)
print("Response Received from PHP script")
#Columns I need to parse are primary_incident_num (0), incident_occured(7), offense_nibrs(13), latitude (25), longitude (26), grid (31)







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

"""
print("Feature set: ")
print(featuresetDF.shape)
print(featuresetDF)
testDF = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\crimeTallys\\crime_tallys_2016_withNear.csv")
print("working df: ")
print(testDF.shape)
print(testDF)
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


print("process complete")