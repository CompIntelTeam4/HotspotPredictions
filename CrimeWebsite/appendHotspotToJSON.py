print("Hello world")


import json


with open(r'C:\xampp\htdocs\CrimePrediction\HTMLtest\geojsonTest.json') as json_file:
    json_decoded = json.load(json_file)

json_decoded['data']['features'][0]['hotspot'] = 1

print(json_decoded['data']['features'][0]['hotspot'])

#3445 grids total

for i in range(len(json_decoded['data']['features'])):
    print(i+1,end='')

#with open(json_file, 'w') as json_file:
    #json.dump(json_decoded, json_file)