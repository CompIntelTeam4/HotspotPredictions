print("Hello world")

import json
import pandas as pd

#3445 grids total
train = pd.read_csv('C:\\\\xampp\\htdocs\\HotspotPredictions\\Data\\Crime_data\\Results\\Jan2019_MLP_wPredictPrev6Mon.csv')
#print(train.head())
with open(r'C:\xampp\htdocs\HotspotPredictions\CrimeWebsite\geojsonTest.json') as json_file:
    json_decoded = json.load(json_file)

#json_decoded['data']['features'][0]['hotspot'] = 1
#print(json_decoded['data']['features'][0]['hotspot'])

#print(train['Grid'][0])
#print(json_decoded['data']['features'][0]['properties'])


for i in range(len(json_decoded['data']['features'])):
    if i%1000 ==0:
        print("on row: ", i)
    json_decoded['data']['features'][i]['properties']['ActualHot'] = int(train['Hotspot'][i])
    json_decoded['data']['features'][i]['properties']['PredictHot'] = int(train['predictions'][i])

with open("MLP_GEO_12M.json", 'w') as json_file:
    json.dump(json_decoded, json_file)
