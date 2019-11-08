

import pandas as pd 

grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Grid_ints_updated.csv")
crime = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\assult_crime_data_2018_wGrid.csv")

output = pd.DataFrame(columns=['Grid','Hotspot'])

#Create new CSV file with two columns...grid numbers hotspot column

print(crime.head()[['Latitude']])

for grid_index, grid_row in grid.head().iterrows():
    #print("Grid ID is: ", grid_row['id'])
    print("On grid number: ", grid_row['id'])
    for crime_index, crime_row in crime.iterrows():

        date = crime_row['Incident Occurred']
        date_pars = date.split('/')
        month = int(date_pars[0])
        #print("Month is: ", month)
        found = False
        if month == 1 and grid_row['id'] == crime_row['grid']:
            found = True
            output = output.append({'Grid': grid_row['id'], 'Hotspot': 1}, ignore_index=True)
            break

    if not found:
        output = output.append({'Grid': grid_row['id'], 'Hotspot': 0}, ignore_index=True)

        #print(month)

output.to_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_prediction\\Data\\Crime_data\\hotspot_predictions.csv",index=False,encoding='utf8')


print(output.head())
    





