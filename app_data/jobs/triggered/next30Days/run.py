import sys
site_packages = "D:\\home\\site\\wwwroot\\env\\Lib\\site-packages"
sys.path.append(site_packages)

from sodapy import Socrata
import pandas as pd
import sys
from datetime import datetime, timedelta
import subprocess
import json 
sys.path.insert(1, 'D:\\\\home\\site\\wwwroot\\GridDetection')
import appendGridNumToCrimeData as test
import logging

logging.basicConfig(filename='D:\\\\home\\LogFiles\\API_pull_Test.log', level=logging.INFO, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.info('Logging the next 30 days script')

#Get the previous date for yesterday.
yesterday = (datetime.now()-timedelta(1)).strftime('%Y-%m-%d')

#Set up the query time parameters
queryStart = yesterday + 'T00:00:00.000'
print(queryStart)
queryEnd = yesterday + 'T23:59:59.000'
print(queryEnd)

#Create the query
query = "incident_occurred between '" + queryStart + "' and '" + queryEnd + "' and (offense_nibrs='13A' or offense_nibrs='13B' or offense_nibrs='13C') and latitude IS NOT NULL and longitude IS NOT NULL"
print(query)
logging.info("Query: " + query)    


#Connect to the socrata client with the proper URL and unique ID
client = Socrata("data.nashville.gov", "ILX2dDLI7jQunnJRUeEEcVEim")
#Nashville crime incident API 2019
client_id = "a88c-cc2y"

#Query all the crimes within the last day and store in variable
print("Getting the API query for: " + yesterday)
logging.info("Getting the API query for: " + yesterday)
results = client.get(client_id, where=query)
print("Length of query: " + str(len(results)))
logging.info("Length of query: " + str(len(results)))


#Convert the results into a pandas dataframe.
results_df = pd.DataFrame.from_records(results)


print("Appending the grid number to each crime...")
logging.info("Appending the grid number to each crime...")

#Run the dataframe through appendGrid function to add grid number to each crime
crime_wGrid = test.append_grid_wDataframe('D:\\\\home\\site\\wwwroot\\Data\\Crime_data\\Grid_with_neighbors.csv', results_df)


print("Exporting the crimes to temporary CSV...")
logging.info("Exporting the crimes to temporary CSV...")
#Export the file to temporary CSV to be opened by PHP file and uploaded to database
#tempCSV = "C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_prediction\\Data\\Crime_data\\tempData\\crime_wGrid_" + yesterday + ".csv"
tempCSV = "D:\\\\home\\site\\wwwroot\\Data\\Crime_data\\tempData\\crime_wGrid_" + yesterday + ".csv"

logging.info("Storing API crime pulls with the grids attatched in file named: crime_wGrid_" + yesterday + ".csv")
crime_wGrid.to_csv(tempCSV,index=False,encoding='utf8')
tempAPIresultsString = "D:\\\\home\\site\\wwwroot\\Data\\Crime_data\\tempData\\apiPull- " + yesterday + ".csv"
logging.info("Storing API pull into tempfile..")
results_df.to_csv(tempAPIresultsString,index=False,encoding='utf8')


#Call database upload script and upload all the crimes from yesterday's date
print("Starting database upload: ")
logging.info("Starting database upload: ")
proc = subprocess.Popen("php databaseUpload.php", shell=True, stdout=subprocess.PIPE)
script_response = str(proc.stdout.read())

print(script_response)
print("Response Received from PHP script")
logging.info("Response Received from PHP script")
logging.info(script_response)

#Columns I need to parse are primary_incident_num (0), incident_occured(7), offense_nibrs(13), latitude (25), longitude (26), grid (31)
logging.info("First half complete.")



import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta #for calculating time a year ago
import sys
sys.path.insert(1, 'D:\\\\home\\site\\wwwroot\\GridDetection\\FeatureTargetCreation')
sys.path.insert(1, "D:\\\\home\\site\\wwwroot\\MachineLearningAlgos")
import DecisionTreeTestAutomated as DST
import feature_creation_with_near as test
import json



import mysql.connector
from mysql.connector.constants import ClientFlag


try:
    db = mysql.connector.connect(host="crimewebsitedatabase.mysql.database.azure.com",
                user="lmurdock12@crimewebsitedatabase",
                password="TheCloudtest2019",
                db="crimes",
                port=3306,
                ssl_ca="D:\\\\home\\ssl\\BaltimoreCyberTrustRoot.crt.pem")
except mysql.connector.Error as err:
    print(err)


"""
db = MySQLdb.connect(host="crimewebsitedatabase.mysql.database.azure.com",user="lmurdock12",
            passwd='TheCloudtest2019',db="crimes",ssl={"ssl":{"ssl-ca":"D:\\\\home\\ssl\\BaltimoreCyberTrustRoot.crt.pem"}})"""


yesterday = (datetime.now()-relativedelta(years=1))
yesterday = str(yesterday).split(' ')[0] #Convert datetime object to string and just take the date without time
print(str(yesterday).split(' ')[0])

sql = "SELECT * FROM incidents WHERE incident_occured >= '" + yesterday + "'" 


print("Creating and sending the sql query...")
logging.info("Creating and sending the sql query...")

df = pd.read_sql(sql,db)
print(df)


print("Creating the featureset...")
logging.info("Creating the featureset...")


tempTally = "D:\\\\home\\site\\wwwroot\\Data\\Crime_data\\tempTallys\\crimeTallys_" + yesterday + ".csv"
#Create and return the datafrrame
featuresetDF = test.createFeatureset_wDataframeV2("D:\\\\home\\site\\wwwroot\\Data\\Crime_data\\Grid_with_neighbors.csv",
       df,tempTally)



print("Training the dataset")
logging.info("Training the dataset")
resultsDF = DST.trainData(featuresetDF,"D:\\\\home\\site\\wwwroot\\trained_models\\DST_saved_model.sav")
print(resultsDF.shape)


#Call the machine learning algorithm and get the dataframe
#and use the following script below
#Then reload user to new page and display the map
#Convert the JSON file to the type needed

print("Exporting to geojson to upload on map")
logging.info("Exporting to geojson to upload on map")
with open('geojsonTemplate.json') as json_file:
    json_decoded = json.load(json_file)

for i in range(len(json_decoded['data']['features'])):
#for i in range(len(100)):
    if i%1000 ==0:
        print("on row: ", i)
    json_decoded['data']['features'][i]['properties']['ActualHot'] = 0
    json_decoded['data']['features'][i]['properties']['PredictHot'] = int(resultsDF[i])

with open("D:\\\\home\\site\\wwwroot\\KNN_GEO.json", 'w') as json_file:
    json.dump(json_decoded, json_file)


print("process complete")
logging.info("Process Complete!")

