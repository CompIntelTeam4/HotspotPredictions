

import pandas as pd 

grid = pd.read_csv("Grid_with_neighbors.csv")
crime = pd.read_csv("assult_crime_data_2018_wGrid.csv")

output = pd.DataFrame(columns=['Grid','Hotspot','near'])

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
    #for grid_index, grid_row in grid.iterrows():
    for crime_index, crime_row in crime.iterrows():
        date = crime_row['Incident Occurred']
        date_pars = date.split('/')
        month = int(date_pars[0])
        #print("Month is: ", month)
        found = False
        if grid_row['id'] == crime_row['grid']:
            #found = True
            hot=1;
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
    output = output.append({'Grid': grid_row['id'], 'Hotspot': hot,'near': top+bottom+left+right+tr+tl+br+bl}, ignore_index=True)
        #print(month)

output.to_csv("hotspot_predictions_with_near_2018.csv",index=False,encoding='utf8')


print(output.head())
    





