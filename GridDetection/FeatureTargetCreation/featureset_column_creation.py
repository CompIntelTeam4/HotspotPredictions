import pandas as pd 

grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Grid_ints_updated.csv")
crime = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\assault_crime_data_2016_wGrid.csv")

output = pd.DataFrame(columns=['Grid','Hotspot', 'week', 'month','year'])

#Create new CSV file with two columns...grid numbers hotspot column

countMonth=0
countYear=0
countWeek=0

for grid_index, grid_row in grid.iterrows():
    #print("Grid ID is: ", grid_row['id'])
    print("On grid number: ", grid_row['id'])
    for crime_index, crime_row in crime.iterrows():

        date = crime_row['Incident Occurred']
        date_pars = date.split('/')
        month = int(date_pars[0])
        day= int(date_pars[1])
        year =int(date_pars[2].split(' ')[0])
        #print("Year is: ", year)
        #print("Month is: ", month)
        if month == 12 and grid_row['id'] == crime_row['grid']:
            countMonth = countMonth+1
        if day >= 25 and month == 12 and grid_row['id'] == crime_row['grid']:
            countWeek = countWeek + 1
        #it should be 17 but we are looking at 18 to get the count
        if  year == 2017 and grid_row['id'] == crime_row['grid']:
            countYear=countYear+1
            
    output = output.append({'Grid': grid_row['id'], 'Hotspot': 0, 'week': countWeek, 'month': countMonth, 'year': countYear}, ignore_index=True)
    countMonth = 0
    countYear = 0
    countWeek = 0
    #print(month)

output.to_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_prediction\\Data\\Crime_data\\crime_tallys_2016.csv",index=False,encoding='utf8')


#print(output)
