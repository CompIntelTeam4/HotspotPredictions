import pandas as pd 

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta #for calculating time a year ago


def createFeatureset_wFile(grid_path, crime_path, output_path):

    grid = pd.read_csv(grid_path)
    #grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\Grid_with_neighbors.csv")

    #Enter the file name you want to use to create the feature set
    crime = pd.read_csv(crime_path)

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


    #Gonna need to pass in the month day and year

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
    output.to_csv(output_path)


def createFeatureset_wDataframe_wDate(grid_path, crimeDataframe, output_path, targetStartDay, targetStartMonth, targetStartYear):
   
   
    grid = pd.read_csv(grid_path)
    #grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\Grid_with_neighbors.csv")

    #Enter the file name you want to use to create the feature set
    crime = crimeDataframe

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

    targetStart = datetime(targetStartYear,targetStartMonth,targetStartDay)
 
    lastMonth = (targetStart-relativedelta(months=1))
    print(type(lastMonth))
    print("Last Month: ",end='')
    print(lastMonth)
    """
    lastMonth = str(lastMonth).split(' ')[0] #Convert datetime object to string and just take the date without time
    lastMonth = lastMonth.split('-')
    lastMonthMonth = int(lastMonth[1])
    lastMonthDay = int(lastMonth[2])
    lastMonthYear = int(lastMonth[0])
    print("last month time is: " + str(lastMonthMonth) + "-" + str(lastMonthDay) + "-" + str(lastMonthYear))
    """


    lastWeek = (targetStart-relativedelta(weeks=1))
    print("Last week: ",end='')
    print(lastWeek)
    """
    lastWeek = str(lastWeek).split(' ')[0]
    lastWeek = lastWeek.split('-')
    lastWeekMonth = int(lastWeek[1])
    lastWeekDay = int(lastWeek[2])
    lastWeekYear = int(lastWeek[0])
    print("last week time is: " + str(lastWeekMonth) + "-" + str(lastWeekDay) + "-" + str(lastWeekYear))
    """

    lastYear = (targetStart-relativedelta(years=1))
    print("Last Year: ",end='')
    print(lastYear)
    """
    lastYear = str(lastYear).split(' ')[0]
    lastYear = lastYear.split('-')
    lastYearMonth = int(lastYear[1])
    lastYearDay = int(lastYear[2])
    lastYearYear = int(lastYear[0])
    print("last year time is: " + str(lastYearMonth) + "-" + str(lastYearDay) + "-" + str(lastYearYear))
    """

    #print(str(yesterday).split(' ')[0])

    #Gonna need to pass in the month day and year

    #Loop through each grid in the dataset
    for grid_index, grid_row in grid.iterrows():
        #print("On grid number: ", grid_row['id'])
        if(grid_index%5 ==0):
            print("On grid: " + str(grid_index))
        
        near=0
        countMonth = 0
        countYear = 0
        countWeek = 0
        #Loop through all of the crimes 
        for crime_index, crime_row in crime.iterrows():
            
            #Parse out the month, day, and year
            date = crime_row['incident_occured']
            
            #With using the database datetime object, first date has to be converted to a string and split by '-'
            #this is different when using a reguarely downloaded file from data.nashville.gov...difference can be seen in createFeatureset_wFile
            date_pars = str(date).split('-')
            #print("date is: ", date_pars)
            year=int(date_pars[0])
            month = int(date_pars[1])
            day=int(date_pars[2].split(' ')[0])

            crime_date = date.to_pydatetime()
            """
            if crime_index == 0:
                print("..")
                date = date.to_pydatetime()
                print(date)
                
                print("date pars is: ", date_pars)
                print(type(date))
                print(date)
                print("Year is : ", year)
                print("Month is: ", month)
                print("day is: ", day)"""

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
            
            if crime_date >= lastMonth and grid_row['id'] == crime_row['grid']:
                countMonth = countMonth+1
            if crime_date >= lastWeek and grid_row['id'] == crime_row['grid']:
                countWeek = countWeek+1
            if  crime_date >= lastYear and grid_row['id'] == crime_row['grid']:
                countYear=countYear+1

        #Update the output for the specific grid
        output = output.append({'Grid': grid_row['id'], 'Hotspot': 0, 'week': countWeek, 'month': countMonth, 'year': countYear,'near': near}, ignore_index=True)


    #Output the file to the CSV
    output.to_csv(output_path)    
    return output


def createFeatureset_wDataframe(grid_path, crimeDataframe, output_path):

    grid = pd.read_csv(grid_path)
    #grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\Grid_with_neighbors.csv")

    #Enter the file name you want to use to create the feature set
    crime = crimeDataframe

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

    lastMonth = (datetime.now()-relativedelta(months=1))
    print(type(lastMonth))
    print(lastMonth)
    """
    lastMonth = str(lastMonth).split(' ')[0] #Convert datetime object to string and just take the date without time
    lastMonth = lastMonth.split('-')
    lastMonthMonth = int(lastMonth[1])
    lastMonthDay = int(lastMonth[2])
    lastMonthYear = int(lastMonth[0])
    print("last month time is: " + str(lastMonthMonth) + "-" + str(lastMonthDay) + "-" + str(lastMonthYear))
    """


    lastWeek = (datetime.now()-relativedelta(weeks=1))
    """
    lastWeek = str(lastWeek).split(' ')[0]
    lastWeek = lastWeek.split('-')
    lastWeekMonth = int(lastWeek[1])
    lastWeekDay = int(lastWeek[2])
    lastWeekYear = int(lastWeek[0])
    print("last week time is: " + str(lastWeekMonth) + "-" + str(lastWeekDay) + "-" + str(lastWeekYear))
    """

    lastYear = (datetime.now()-relativedelta(years=1))
    """
    lastYear = str(lastYear).split(' ')[0]
    lastYear = lastYear.split('-')
    lastYearMonth = int(lastYear[1])
    lastYearDay = int(lastYear[2])
    lastYearYear = int(lastYear[0])
    print("last year time is: " + str(lastYearMonth) + "-" + str(lastYearDay) + "-" + str(lastYearYear))
    """

    #print(str(yesterday).split(' ')[0])

    #Gonna need to pass in the month day and year

    #Loop through each grid in the dataset
    for grid_index, grid_row in grid.iterrows():
        #print("On grid number: ", grid_row['id'])
        if(grid_index%5 ==0):
            print("On grid: " + str(grid_index))
        
        near=0
        countMonth = 0
        countYear = 0
        countWeek = 0
        #Loop through all of the crimes 
        for crime_index, crime_row in crime.iterrows():
            
            #Parse out the month, day, and year
            date = crime_row['incident_occured']
            
            #With using the database datetime object, first date has to be converted to a string and split by '-'
            #this is different when using a reguarely downloaded file from data.nashville.gov...difference can be seen in createFeatureset_wFile
            date_pars = str(date).split('-')
            #print("date is: ", date_pars)
            year=int(date_pars[0])
            month = int(date_pars[1])
            day=int(date_pars[2].split(' ')[0])

            crime_date = date.to_pydatetime()
            """
            if crime_index == 0:
                print("..")
                date = date.to_pydatetime()
                print(date)
                
                print("date pars is: ", date_pars)
                print(type(date))
                print(date)
                print("Year is : ", year)
                print("Month is: ", month)
                print("day is: ", day)"""

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
            
            if crime_date >= lastMonth and grid_row['id'] == crime_row['grid']:
                countMonth = countMonth+1
            if crime_date >= lastWeek and grid_row['id'] == crime_row['grid']:
                countWeek = countWeek+1
            if  crime_date >= lastYear and grid_row['id'] == crime_row['grid']:
                countYear=countYear+1

        #Update the output for the specific grid
        output = output.append({'Grid': grid_row['id'], 'Hotspot': 0, 'week': countWeek, 'month': countMonth, 'year': countYear,'near': near}, ignore_index=True)


    #Output the file to the CSV
    output.to_csv(output_path)    
    return output


def createFeatureset_wDataframe_wDateV2(grid_path, crimeDataframe, output_path, targetStartDay, targetStartMonth, targetStartYear):
   
   
    grid = pd.read_csv(grid_path)
    #grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\Grid_with_neighbors.csv")
    print(grid.columns)
    #Enter the file name you want to use to create the feature set
    crime = crimeDataframe

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

    targetStart = datetime(targetStartYear,targetStartMonth,targetStartDay)
 
    lastMonth = (targetStart-relativedelta(months=1))
    print(type(lastMonth))
    print("Last Month: ",end='')
    print(lastMonth)
   
    lastWeek = (targetStart-relativedelta(weeks=1))
    print("Last week: ",end='')
    print(lastWeek)

    lastYear = (targetStart-relativedelta(years=1))
    print("Last Year: ",end='')
    print(lastYear)


    gridToCrimeMap = {}

    for i in range(1,3446):
        gridToCrimeMap[i] = {'lastWeek':0,'lastMonth':0,'lastYear':0,'near':0}

    for crime_index, crime_row in crime.iterrows():

            #if crime_row['grid'] not in gridToCrimeMap:
                #gridToCrimeMap[crime_row['grid']] = {'lastWeek':0,'lastMonth':0,'lastYear':0,'near':0}

            #Parse out the month, day, and year
            date = crime_row['incident_occured']
            #With using the database datetime object, first date has to be converted to a string and split by '-'
            #this is different when using a reguarely downloaded file from data.nashville.gov...difference can be seen in createFeatureset_wFile
            date_pars = str(date).split('-')
            #print("date is: ", date_pars)
            year=int(date_pars[0])
            month = int(date_pars[1])
            day=int(date_pars[2].split(' ')[0])
            crime_date = date.to_pydatetime()

            if crime_date >= lastMonth:#and grid_row['id'] == crime_row['grid']:
                gridToCrimeMap[crime_row['grid']]['lastMonth'] += 1
            if crime_date >= lastWeek: # and grid_row['id'] == crime_row['grid']:
                gridToCrimeMap[crime_row['grid']]['lastWeek'] += 1
            if  crime_date >= lastYear: # and grid_row['id'] == crime_row['grid']:
                gridToCrimeMap[crime_row['grid']]['lastYear'] += 1
    


    for grid_index, grid_row in grid.iterrows():

        if grid_row['id'] in gridToCrimeMap:

            total_near = 0 
            near_grids = ['top ','bottom ','left ','right ','topleft','topright','bottomleft','bottomright']

            
            if grid_row['id'] == 2071:
                print('top: ', grid_row['top '])
                if grid_row['top '] in gridToCrimeMap:
                   print("Top grid # is: " + str(grid_row['top ']) + ", and crimes within last year are: " + str(gridToCrimeMap[grid_row['top ']]['lastYear']))
                print('bottom: ', grid_row['bottom '])
                if grid_row['bottom '] in gridToCrimeMap:
                    print("bottom grid # is: " + str(grid_row['bottom ']) + ", and crimes within last year are: " + str(gridToCrimeMap[grid_row['bottom ']]['lastYear']))
                print('left: ', grid_row['left '])
                if grid_row['left '] in gridToCrimeMap:
                    print("left grid # is: " + str(grid_row['left ']) + ", and crimes within last year are: " + str(gridToCrimeMap[grid_row['left ']]['lastYear']))
                print('right: ', grid_row['right '])
                if grid_row['right '] in gridToCrimeMap:
                    print("right grid # is: " + str(grid_row['right ']) + ", and crimes within last year are: " + str(gridToCrimeMap[grid_row['right ']]['lastYear']))
                print('topright: ', grid_row['top'])
                if grid_row['topright'] in gridToCrimeMap:
                    print("topright grid # is: " + str(grid_row['topright']) + ", and crimes within last year are: " + str(gridToCrimeMap[grid_row['topright']]['lastYear']))
                print('topleft: ', grid_row['topleft'])
                if grid_row['topleft'] in gridToCrimeMap:
                    print("topleft grid # is: " + str(grid_row['topleft']) + ", and crimes within last year are: " + str(gridToCrimeMap[grid_row['topleft']]['lastYear']))
                print('bottomleft: ', grid_row['bottomleft'])
                if grid_row['bottomleft'] in gridToCrimeMap:
                    print("bottomleft grid # is: " + str(grid_row['bottomleft']) + ", and crimes within last year are: " + str(gridToCrimeMap[grid_row['bottomleft']]['lastYear']))
                print('bottomright: ', grid_row['bottomright'])
                if grid_row['bottomright'] in gridToCrimeMap:
                    print("bottomright grid # is: " + str(grid_row['bottomright']) + ", and crimes within last year are: " + str(gridToCrimeMap[grid_row['bottomright']]['lastYear']))
            
            for i in range(len(near_grids)):

                if grid_row[near_grids[i]] in gridToCrimeMap:
                    total_near += gridToCrimeMap[grid_row[near_grids[i]]]['lastYear']


            gridToCrimeMap[grid_row['id']]['near'] = total_near
            output = output.append({'Grid': grid_row['id'], 'Hotspot': 0, 'week': gridToCrimeMap[grid_row['id']]['lastWeek'], 'month': gridToCrimeMap[grid_row['id']]['lastMonth'], 'year': gridToCrimeMap[grid_row['id']]['lastYear'],'near': gridToCrimeMap[grid_row['id']]['near']}, ignore_index=True)
        else:
            output = output.append({'Grid': grid_row['id'], 'Hotspot': 0, 'week': 0, 'month': 0, 'year': 0,'near': 0}, ignore_index=True)
    #Output the file to the CSV
    output.to_csv(output_path)    
    return output