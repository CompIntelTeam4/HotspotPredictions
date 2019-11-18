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


    x_cordl= crime_row['left']
    x_cordr=crime_row['right']
    y_cordt=crime_row['top']
    y_cordb=crime_row['bottom']

    check1, check2, check3, check4, check5, check6, check7, check8, check9 = 1

    for grid_index, grid_row in grid.iterrows():

        if x_cordl == grid_row['left'] and x_cordr == grid_row['right'] and y_cordb == grid_row['bottom'] and y_cordt <= grid_row['top']:
            crime.at[crime_index,'grid'] = grid_row['id']
            check1-=1
        elif  x_cordl == grid_row['left'] and x_cordr == grid_row['right'] and y_cordb+800 == grid_row['bottom'] and y_cordt+800 == grid_row['top']:
            crime.at[crime_index,'top '] = grid_row['id']
            check2-=1
        elif  x_cordl == grid_row['left'] and x_cordr == grid_row['right'] and y_cordb-800 == grid_row['bottom'] and y_cordt-800 == grid_row['top']:
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



crime.to_csv("Grid_with_neighbors.csv",index=False,encoding='utf8')

end = time.time()*1000

print("Total computation time: ", end-start)



    
