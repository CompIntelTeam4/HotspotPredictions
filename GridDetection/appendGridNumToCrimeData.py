import pandas as pd 
import math
import time




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



def append_grid_wFile(grid_file, crime_file):

    start = time.time()*1000
    
    grid = "C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\" + grid_file
    crime = "C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\rawData\\" + crime_file
    print(grid)
    print(crime)
    grid = pd.read_csv(grid)
    crime = pd.read_csv(crime)

    crime['grid'] = -1
    
    for crime_index, crime_row in crime.iterrows():

        if crime_index%5==0:
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


    crime.to_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_prediction\\Data\\Crime_data\\assault_crime_data_2019_wGrid.csv",index=False,encoding='utf8')

    end = time.time()*1000

    print("Total computation time: ", end-start)


def append_grid_wDataframe(grid_file, crimeDataframe):

    start = time.time()*1000
    
    grid = grid_file
    grid = pd.read_csv(grid)

    crimeDataframe['grid'] = -1
    
    for crime_index, crime_row in crimeDataframe.iterrows():

        #Print out index every 50 rows to keep track of progress
        if crime_index%50==0:
            print("On index: ", crime_index)

        #Get lat and long for row
        #*****For some reason the 2019 dataset uses a lowercase l for lat in long column
        #*****The 2018 and earlier datasets seem to use uppercase l
        #*****Also the values stored in lat long columns seem to come in as strings...this isn't when I imported
        #*****the earlier versions like '2017_assault.csv'
        latitude = float(crime_row['latitude'])
        longitude = float(crime_row['longitude'])

        #call cord_conversion and get x_cord and y_cord
        x_cord, y_cord = lat_to_cord(longitude,latitude)
        for grid_index, grid_row in grid.iterrows():
            if x_cord > grid_row['left'] and x_cord < grid_row['right'] and y_cord > grid_row['bottom'] and y_cord < grid_row['top']:
                #print("found")
                crimeDataframe.at[crime_index,'grid'] = grid_row['id']
                #crime_row['grid'] = 5#grid_row['id']
                break
            else:
                "GRID NOT FOUND"

        #Possibly add in function to remove row if grid value is -1

    end = time.time()*1000
    print("Total computation time to append grids: ", end-start)

    return crimeDataframe


#if __name__ == "__main__":
    #append_grid_wFile('Grid_with_neighbors.csv','2019_assaults.csv')


    