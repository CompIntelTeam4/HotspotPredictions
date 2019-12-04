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
    for grid_index, grid_row in grid.sample(5).iterrows():
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
