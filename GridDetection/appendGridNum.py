import pandas as pd 
import math

grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Grid_ints_updated.csv")
crime = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\2017_assault.csv")

crime['grid'] = None
#print(data[['id']])

#Map coord to lat long
def cord_conversion(x_cord,y_cord):

    b=20037508.34

    longitude = x_cord*(180/20037508.34)
    latitude = math.atan(math.exp(y_cord*(math.pi/b)))*(360/math.pi)-90

    #print("Long: ", longitude)
    #print("Lat: ", latitude)

    return longitude, latitude

def lat_to_cord(long, lat):

    b=20037508.34
    x_cord = (b*long)/180
    print("x_cord is: ", x_cord)

    y_cord = math.log(math.tan((lat+90)/(360/math.pi)))*(b/math.pi)
    print("y_cord is:", y_cord)

    return x_cord, y_cord
    #math.log(math.tan((lat-90)/(360/math.pi)))*(b/math.pi)
    #180.0/math.pi*math.log(math.tan(math.pi/4.0+y_cord*(math.pi/180.0)/2.0)) 


for index, row in crime.head().iterrows():
    row['grid'] 

    #get lat and long for row
    latitude = row['Latitude']
    longitude = row['Longitude']
    #call cord_conversion and get x_cord and y_cord
    x_cord, y_cord = lat_to_cord(longitude ,latitude)
    print("x_cord is: ", x_cord)
    print("y_cord is: ", y_cord)
    for index, grid_row in grid.iterrows():
        if x_cord > grid_row['left'] and x_cord < grid_row['right'] and y_cord > grid_row['bottom'] and y_cord < grid_row['top']:
            crime['grid'] = grid['id']
            break
        
    #get_cord(): 
        #loop through each grid and see if cord is inside
            #if inside then return grid number

    #set the grid column for that specific row

    #print(str(row['id']) + " : " + str(row['grid']))

print(crime.head())




x = -9672391
y = 4321695
#longitude, latitude = cord_conversion(x,y)

#lat_to_cord(longitude,latitude)



    