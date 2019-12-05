
import pandas as pd 




def targetCreationNear_wFile():

    grid = pd.read_csv("Grid_with_neighbors.csv")
    #Specify the file you want to use for the target prediction month
    crime = pd.read_csv("assult_crime_data_2018_wGrid.csv")

    #Create the output format for the pandas DataFrame
    output = pd.DataFrame(columns=['Grid','Hotspot','near'])

    ########################################################################################
    # This file creates the hotspot predictions as well as the feature column of near
    # near is based off how many of the surrounding grids are also hotspots for that month
    # each near hotspot adds .125 to near's value...near's max value is one if all 8
    # surrounding grids are a hotspot for that month
    #########################################################################################

    #Loop through and calculate for each grid
    for grid_index, grid_row in grid.iterrows():

        print("On grid number: ", grid_row['id'])

        hot, near, top, bottom, left, right, tl, tr, bl, br = 0

        #Loop through each crime
        for crime_index, crime_row in crime.iterrows():
            date = crime_row['Incident Occurred']
            date_pars = date.split('/')
            month = int(date_pars[0])
            #print("Month is: ", month)
            found = False
            if month == 1:

                if grid_row['id'] == crime_row['grid']:
                    hot=1
                if grid_row['top '] == crime_row['grid']:
                    top=.125
                if grid_row['bottom '] == crime_row['grid']:
                    bottom=.125
                if grid_row['left '] == crime_row['grid']:
                    left=.125
                if grid_row['right '] == crime_row['grid']:
                    right=.125
                if grid_row['topleft'] == crime_row['grid']:
                    tl=.125
                if grid_row['topright'] == crime_row['grid']:
                    tr=.125
                if grid_row['bottomright'] == crime_row['grid']:
                    br=.125
                if grid_row['bottomleft'] == crime_row['grid']:
                    bl=.125

            if hot==1 and top+bottom+left+right+tr+tl+br+bl==1:
                break

        #Append each grid's results to the dataframe
        output = output.append({'Grid': grid_row['id'], 'Hotspot': hot,'near': top+bottom+left+right+tr+tl+br+bl}, ignore_index=True)

    #Output the dataframe to the CSV
    output.to_csv("hotspot_predictions_with_near_2018.csv",index=False,encoding='utf8')

    



def targetCreationNear_wDF(gridFilePath, crimeDF):

    grid = pd.read_csv("Grid_with_neighbors.csv")
    #Specify the file you want to use for the target prediction month
    crime = pd.read_csv("assult_crime_data_2018_wGrid.csv")

    #Create the output format for the pandas DataFrame
    output = pd.DataFrame(columns=['Grid','Hotspot','near'])

    ########################################################################################
    # This file creates the hotspot predictions as well as the feature column of near
    # near is based off how many of the surrounding grids are also hotspots for that month
    # each near hotspot adds .125 to near's value...near's max value is one if all 8
    # surrounding grids are a hotspot for that month
    #########################################################################################

    #Loop through and calculate for each grid
    for grid_index, grid_row in grid.iterrows():

        print("On grid number: ", grid_row['id'])

        hot, near, top, bottom, left, right, tl, tr, bl, br = 0

        #Loop through each crime
        for crime_index, crime_row in crime.iterrows():
            date = crime_row['Incident Occurred']
            date_pars = date.split('/')
            month = int(date_pars[0])
            #print("Month is: ", month)
            found = False
            if month == 1:

                if grid_row['id'] == crime_row['grid']:
                    hot=1
                if grid_row['top '] == crime_row['grid']:
                    top=.125
                if grid_row['bottom '] == crime_row['grid']:
                    bottom=.125
                if grid_row['left '] == crime_row['grid']:
                    left=.125
                if grid_row['right '] == crime_row['grid']:
                    right=.125
                if grid_row['topleft'] == crime_row['grid']:
                    tl=.125
                if grid_row['topright'] == crime_row['grid']:
                    tr=.125
                if grid_row['bottomright'] == crime_row['grid']:
                    br=.125
                if grid_row['bottomleft'] == crime_row['grid']:
                    bl=.125

            if hot==1 and top+bottom+left+right+tr+tl+br+bl==1:
                break

        #Append each grid's results to the dataframe
        output = output.append({'Grid': grid_row['id'], 'Hotspot': hot,'near': top+bottom+left+right+tr+tl+br+bl}, ignore_index=True)

    #Output the dataframe to the CSV
    output.to_csv("hotspot_predictions_with_near_2018.csv",index=False,encoding='utf8')

