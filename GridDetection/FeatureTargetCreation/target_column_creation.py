

import pandas as pd 


def targetCreation_wFile():
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

def targetCreation_wDF(gridFilePath, crimeDF,outputPath, targetMonth):

    grid = pd.read_csv(gridFilePath)
    crime = crimeDF
    output = pd.DataFrame(columns=['Grid','Hotspot'])

    ####################################################################
    #Create new CSV file with two columns...the grid number and if that grid number is a hotspot or not for the specified month
    #Right now this program is set to determine if a hotspot or not for the first month (January)
    ######################################################################

    #Loop through and determine if a hot spot for each grid
    for grid_index, grid_row in grid.sample(30).iterrows():
        if grid_index%500 == 0:
            print("On grid number: ", grid_row['id'])

        #Loop through each crime until a crime for that month is either found or not found
        #If found then set hotspot to one
        for crime_index, crime_row in crime.iterrows():

            #Parse the date out of each crime
            date = crime_row['incident_occured']
            
            #With using the database datetime object, first date has to be converted to a string and split by '-'
            #this is different when using a reguarely downloaded file from data.nashville.gov...difference can be seen in createFeatureset_wFile
            date_pars = str(date).split('-')
            #print("date is: ", date_pars)
            year=int(date_pars[0])
            month = int(date_pars[1])
            day=int(date_pars[2].split(' ')[0])

            crime_date = date.to_pydatetime()

            found = False
            if month == targetMonth and grid_row['id'] == crime_row['grid']:
                #If a crime found then add row to output with hotspot set to 1
                found = True
                output = output.append({'Grid': grid_row['id'], 'Hotspot': 1}, ignore_index=True)
                break

        if not found:
            #If crime not found then add row to output with hotspot set to 0
            output = output.append({'Grid': grid_row['id'], 'Hotspot': 0}, ignore_index=True)

    #Output the resulting dataframe 
    output.to_csv(outputPath,index=False,encoding='utf8')
    return output








