import pandas as pd 

grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\Grid_with_neighbors.csv")

#Enter the file name you want to use to create the feature set
crime = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\assult_crime_data_2017_wGrid.csv")

#Initialize the output dataframe
output = pd.DataFrame(columns=['Grid','Hotspot', 'week', 'month','year','near'])

########################################################################
#
#This file loops through and creates the feature column's for our dataset
#It adds up the amount of crimes that happen in the week, month, year and
#how many crimes happen in the near grid's.
#The hotspot column will be all 0's and will be replaced with the output
#From the target creation file
#######################################################################

#******************
#Must set the proper year to check below based on what file you are using
#****************

countMonth=0
countYear=0
countWeek=0

#Loop through each grid in the dataset
for grid_index, grid_row in grid.iterrows():
    print("On grid number: ", grid_row['id'])
    near=0
    #Loop through all of the crimes 
    for crime_index, crime_row in crime.iterrows():
        
        #Parse out the month, day, and year
        date = crime_row['Incident Occurred']
        date_pars = date.split('/')
        month = int(date_pars[0])
        day= int(date_pars[1])
        year =int(date_pars[2].split(' ')[0])

        if grid_row['top '] == crime_row['grid']:
            near +=1
        if grid_row['bottom '] == crime_row['grid']:
            near +=1
        if grid_row['left '] == crime_row['grid']:
            near +=1
        if grid_row['right '] == crime_row['grid']:
            near +=1
        if grid_row['topleft'] == crime_row['grid']:
            near +=1
        if grid_row['topright'] == crime_row['grid']:
            near +=1
        if grid_row['bottomright'] == crime_row['grid']:
            near +=1
        if grid_row['bottomleft'] == crime_row['grid']:
            near +=1
        
        if month == 12 and grid_row['id'] == crime_row['grid']:
            countMonth = countMonth+1
        if day >= 25 and month == 12 and grid_row['id'] == crime_row['grid']:
            countWeek = countWeek + 1

        if  year == 2017 and grid_row['id'] == crime_row['grid']:
            countYear=countYear+1

    #Update the output for the specific grid
    output = output.append({'Grid': grid_row['id'], 'Hotspot': 0, 'week': countWeek, 'month': countMonth, 'year': countYear,'near': near}, ignore_index=True)
    countMonth = 0
    countYear = 0
    countWeek = 0

#Output the file to the CSV
output.to_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\crime_tallys_2016_withNear.csv",index=False,encoding='utf8')
