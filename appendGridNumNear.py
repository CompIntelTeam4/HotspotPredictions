import pandas as pd 
import math
import time


start = time.time()*1000

grid = pd.read_csv("Grid_ints_updated.csv")
crime= pd.read_csv("Grid_ints_updated.csv")
crime['grid'] = -1

#print(data[['id']])
crime['top ']=0
crime['bottom ']=0
crime['left ']=0
crime['right ']=0
crime['topleft']=0
crime['topright']=0
crime['bottomleft']=0
crime['bottomright']=0

for crime_index, crime_row in crime.iterrows():

    if crime_index%100==0:
        print("On index: ", crime_index)
    #get lat and long for row
    '''latitude = crime_row['Latitude']
    longitude = crime_row['Longitude']
    #call cord_conversion and get x_cord and y_cord
    x_cord, y_cord = lat_to_cord(longitude ,latitude)'''
    x_cordl= crime_row['left']
    x_cordr=crime_row['right']
    y_cordt=crime_row['top']
    y_cordb=crime_row['bottom']
    check1=1
    check2=1
    check3=1
    check4=1
    check5=1
    check6=1
    check7=1
    check8=1
    check9=1
    #print("P",x_cord,y_cord)
    for grid_index, grid_row in grid.iterrows():
        #print(grid_row['left'],grid_row['right'],grid_row['bottom'],grid_row['top'])
        if x_cordl == grid_row['left'] and x_cordr == grid_row['right'] and y_cordb == grid_row['bottom'] and y_cordt <= grid_row['top']:
            #print("found")
            crime.at[crime_index,'grid'] = grid_row['id']
            check1-=1
            #crime_row['grid'] = 5#grid_row['id']
        elif  x_cordl == grid_row['left'] and x_cordr == grid_row['right'] and y_cordb+800 == grid_row['bottom'] and y_cordt+800 == grid_row['top']:
            #print("found")
            crime.at[crime_index,'top '] = grid_row['id']
            #print(grid_row['left'],grid_row['right'],grid_row['bottom'],grid_row['top'])
            #break
            check2-=1
        elif  x_cordl == grid_row['left'] and x_cordr == grid_row['right'] and y_cordb-800 == grid_row['bottom'] and y_cordt-800 == grid_row['top']:
            #crime_row['grid'] = 5#grid_row['id']
            crime.at[crime_index,'bottom '] = grid_row['id']
            check3-=1
        elif  x_cordl+800 == grid_row['left'] and x_cordr+800 == grid_row['right'] and y_cordb == grid_row['bottom'] and y_cordt == grid_row['top']:
            crime.at[crime_index,'right '] = grid_row['id']
            check4-=1
        elif  x_cordl-800 == grid_row['left'] and x_cordr-800 == grid_row['right'] and y_cordb == grid_row['bottom'] and y_cordt == grid_row['top']:
            crime.at[crime_index,'left '] = grid_row['id']
            check5-=1
        elif  x_cordl-800 == grid_row['left'] and x_cordr-800 == grid_row['right'] and y_cordb-800 == grid_row['bottom'] and y_cordt-800 == grid_row['top']:
            crime.at[crime_index,'bottomleft'] = grid_row['id']
            check6-=1
        elif  x_cordl+800 == grid_row['left'] and x_cordr+800 == grid_row['right'] and y_cordb-800 == grid_row['bottom'] and y_cordt-800 == grid_row['top']:
            crime.at[crime_index,'bottomright'] = grid_row['id']
            check7-=1
        elif  x_cordl-800 == grid_row['left'] and x_cordr-800 == grid_row['right'] and y_cordb+800 == grid_row['bottom'] and y_cordt+800 == grid_row['top']:
            crime.at[crime_index,'topleft'] = grid_row['id']
            check8-=1
        elif  x_cordl+800 == grid_row['left'] and x_cordr+800 == grid_row['right'] and y_cordb+800 == grid_row['bottom'] and y_cordt+800 == grid_row['top']:
            crime.at[crime_index,'topright'] = grid_row['id']
            check9-=1
        elif check1<=0 and check2<=0 and check3<=0 and check4<=0 and check5<=0 and check6<=0 and check7<=0 and check8<=0 and check9<=0:
            break
        else:
            "GRID NOT FOUND"
    #get_cord(): 
        #loop through each grid and see if cord is inside
            #if inside then return grid number

    #set the grid column for that specific row

"""
for final_index, final_row in crime.head().iterrows():
    x_cord,y_cord = lat_to_cord(final_row['Longitude'], final_row['Latitude'])
    print("Index is: " + str(final_index) + ", ID is: " + str(final_row['Primary Key']) + 
        ", Lat is: " + str(final_row['Latitude']) + ", Long is: " + str(final_row['Longitude']) + 
        ", Grid is: " + str(final_row['grid']) + ", X_Cord: " + str(x_cord) + ", Y_cord: " + str(y_cord))"""

crime.to_csv("Grid_with_neighbors.csv",index=False,encoding='utf8')

end = time.time()*1000

print("Total computation time: ", end-start)



    
