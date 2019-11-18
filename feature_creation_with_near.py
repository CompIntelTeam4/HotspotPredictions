import pandas as pd 

grid = pd.read_csv("Grid_with_neighbors.csv")
crime = pd.read_csv("assault_crime_data_2016_wGrid.csv")

output = pd.DataFrame(columns=['Grid','Hotspot', 'week', 'month','year'])

#Create new CSV file with two columns...grid numbers hotspot column

countMonth=0
countYear=0
countWeek=0

for grid_index, grid_row in grid.iterrows():
    #print("Grid ID is: ", grid_row['id'])
    print("On grid number: ", grid_row['id'])
    hot=0
    near=0
    top=0
    bottom=0
    left=0
    right=0
    tl=0
    tr=0
    bl=0
    br=0
    for crime_index, crime_row in crime.iterrows():
        
        date = crime_row['Incident Occurred']
        date_pars = date.split('/')
        month = int(date_pars[0])
        day= int(date_pars[1])
        year =int(date_pars[2].split(' ')[0])
        #print("Year is: ", year)
        #print("Month is: ", month)
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
        if month == 12 and grid_row['id'] == crime_row['grid']:
            countMonth = countMonth+1
        if day >= 25 and month == 12 and grid_row['id'] == crime_row['grid']:
            countWeek = countWeek + 1
        #it should be 17 but we are looking at 18 to get the count
        if  year == 2017 and grid_row['id'] == crime_row['grid']:
            countYear=countYear+1
    output = output.append({'Grid': grid_row['id'], 'Hotspot': hot, 'week': countWeek, 'month': countMonth, 'year': countYear,'near': top+bottom+left+right+tr+tl+br+bl}, ignore_index=True)
    countMonth = 0
    countYear = 0
    countWeek = 0
    #print(month)

output.to_csv("crime_tallys_2016.csv",index=False,encoding='utf8')


#print(output)
