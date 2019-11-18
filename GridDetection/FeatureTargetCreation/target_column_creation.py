

import pandas as pd 

grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Grid_ints_updated.csv")
crime = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\assult_crime_data_2017_wGrid.csv")
output = pd.DataFrame(columns=['Grid','Hotspot'])

####################################################################
#Create new CSV file with two columns...the grid number and if that grid number is a hotspot or not for the specified month
#Right now this program is set to determine if a hotspot or not for the first month (January)
######################################################################

#Loop through and determine if a hot spot for each grid
for grid_index, grid_row in grid.iterrows():
    print("On grid number: ", grid_row['id'])

    #Loop through each crime until a crime for that month is either found or not found
    #If found then set hotspot to one
    for crime_index, crime_row in crime.iterrows():

        #Parse the date out of each crime
        date = crime_row['Incident Occurred']
        date_pars = date.split('/')
        month = int(date_pars[0])

        found = False
        if month == 1 and grid_row['id'] == crime_row['grid']:
            #If a crime found then add row to output with hotspot set to 1
            found = True
            output = output.append({'Grid': grid_row['id'], 'Hotspot': 1}, ignore_index=True)
            break

    if not found:
        #If crime not found then add row to output with hotspot set to 0
        output = output.append({'Grid': grid_row['id'], 'Hotspot': 0}, ignore_index=True)

#Output the resulting dataframe 
output.to_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_prediction\\Data\\Crime_data\\hotspot_predictions_2017.csv",index=False,encoding='utf8')






