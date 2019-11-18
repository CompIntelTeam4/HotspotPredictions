import pandas as pd 
import math
import time


start = time.time()*1000

grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Grid_ints_updated.csv")
crime = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\2017_assault.csv")

crime['grid'] = -1

#Map coord to lat long
def cord_conversion(x_cord,y_cord):

    b=20037508.34

    longitude = x_cord*(180/20037508.34)
    latitude = math.atan(math.exp(y_cord*(math.pi/b)))*(360/math.pi)-90

    return longitude, latitude

def lat_to_cord(long, lat):

    b=20037508.34
    x_cord = (b*long)/180
    y_cord = math.log(math.tan((lat+90)/(360/math.pi)))*(b/math.pi)

    return x_cord, y_cord


for crime_index, crime_row in crime.iterrows():

    if crime_index%1000==0:
        print("On index: ", crime_index)
    #get lat and long for row
    latitude = crime_row['Latitude']
    longitude = crime_row['Longitude']
    #call cord_conversion and get x_cord and y_cord
    x_cord, y_cord = lat_to_cord(longitude ,latitude)
    for grid_index, grid_row in grid.iterrows():
        if x_cord > grid_row['left'] and x_cord < grid_row['right'] and y_cord > grid_row['bottom'] and y_cord < grid_row['top']:
            #print("found")
            crime.at[crime_index,'grid'] = grid_row['id']
            #crime_row['grid'] = 5#grid_row['id']
            break
        else:
            "GRID NOT FOUND"


crime.to_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_prediction\\Data\\Crime_data\\assault_crime_data_2016_wGrid.csv",index=False,encoding='utf8')

end = time.time()*1000

print("Total computation time: ", end-start)



    