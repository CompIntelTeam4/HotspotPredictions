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



def createFeatureset_wDataframe_Short(grid_path, crimeDataframe, output_path, targetStartDay, targetStartMonth, targetStartYear):
   
   
    grid = pd.read_csv(grid_path)
    #grid = pd.read_csv("C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_Prediction\\Data\\Crime_Data\\Grid_with_neighbors.csv")
    #print(grid.columns)
    #Enter the file name you want to use to create the feature set
    crime = crimeDataframe

    #Initialize the output dataframe
    output = pd.DataFrame(columns=['Grid','Hotspot', '1day', '2day','3day','4day','5day','6day','7day','8day','9day','10day',
                                    '11day', '12day','13day','14day','15day','16day','17day','18day','19day','20day',
                                    '21day', '22day','23day','24day','25day','26day','27day','28day','29day','30day'])

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
 

    gridToCrimeMap = {}

    for i in range(1,3446):
        gridToCrimeMap[i] = {'1day':0,'2day':0,'3day':0,'4day':0,'5day':0,'6day':0,'7day':0,'8day':0,'9day':0,'10day':0,'11day':0,'12day':0,'13day':0,'14day':0,'15day':0,'16day':0,
                        '17day':0,'18day':0,'19day':0,'20day':0,'21day':0,'22day':0,'23day':0,'24day':0,'25day':0,'26day':0,'27day':0,'28day':0,'29day':0,'30day':0, 'total':0,'totalNear':0}

    totalAdded = 0
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
            #print("Crime Date: " + str(crime_date) + ", Relative: " + (str(targetStart-relativedelta(days=1))))
            if crime_date.day == (targetStart-relativedelta(days=1)).day:
                gridToCrimeMap[crime_row['grid']]['1day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=2)).day:
                gridToCrimeMap[crime_row['grid']]['2day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=3)).day:
                gridToCrimeMap[crime_row['grid']]['3day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=4)).day:
                gridToCrimeMap[crime_row['grid']]['4day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=5)).day:
                gridToCrimeMap[crime_row['grid']]['5day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=6)).day:
                gridToCrimeMap[crime_row['grid']]['6day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=7)).day:
                gridToCrimeMap[crime_row['grid']]['7day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=8)).day:
                gridToCrimeMap[crime_row['grid']]['8day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=9)).day:
                gridToCrimeMap[crime_row['grid']]['9day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=10)).day:
                gridToCrimeMap[crime_row['grid']]['10day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=11)).day:
                gridToCrimeMap[crime_row['grid']]['11day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=12)).day:
                gridToCrimeMap[crime_row['grid']]['12day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=13)).day:
                gridToCrimeMap[crime_row['grid']]['13day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=14)).day:
                gridToCrimeMap[crime_row['grid']]['14day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=15)).day:
                gridToCrimeMap[crime_row['grid']]['15day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=16)).day:
                gridToCrimeMap[crime_row['grid']]['16day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=17)).day:
                gridToCrimeMap[crime_row['grid']]['17day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=18)).day:
                gridToCrimeMap[crime_row['grid']]['18day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=19)).day:
                gridToCrimeMap[crime_row['grid']]['19day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=20)).day:
                gridToCrimeMap[crime_row['grid']]['20day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=21)).day:
                gridToCrimeMap[crime_row['grid']]['21day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=22)).day:
                gridToCrimeMap[crime_row['grid']]['22day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=23)).day:
                gridToCrimeMap[crime_row['grid']]['23day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=24)).day:
                gridToCrimeMap[crime_row['grid']]['24day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=25)).day:
                gridToCrimeMap[crime_row['grid']]['25day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=26)).day:
                gridToCrimeMap[crime_row['grid']]['26day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=27)).day:
                gridToCrimeMap[crime_row['grid']]['27day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=28)).day:
                gridToCrimeMap[crime_row['grid']]['28day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=29)).day:
                gridToCrimeMap[crime_row['grid']]['29day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1
            if crime_date.day == (targetStart-relativedelta(days=30)).day:
                gridToCrimeMap[crime_row['grid']]['30day'] += 1
                gridToCrimeMap[crime_row['grid']]['total'] += 1
                totalAdded +=1


    print("Added: " + str(totalAdded) + ", crimes to the features")
    for grid_index, grid_row in grid.iterrows():

        if grid_row['id'] in gridToCrimeMap:

            total_near = 0 
            near_grids = ['top ','bottom ','left ','right ','topleft','topright','bottomleft','bottomright']


            for i in range(len(near_grids)):

                if grid_row[near_grids[i]] in gridToCrimeMap:
                    total_near += gridToCrimeMap[grid_row[near_grids[i]]]['total']


            gridToCrimeMap[grid_row['id']]['totalNear'] = total_near
            output = output.append({'Grid': grid_row['id'],'Hotspot':0, '1day': gridToCrimeMap[grid_row['id']]['1day'], '2day': gridToCrimeMap[grid_row['id']]['2day'], '3day': gridToCrimeMap[grid_row['id']]['3day'], '4day': gridToCrimeMap[grid_row['id']]['4day'],
                        '5day': gridToCrimeMap[grid_row['id']]['5day'],'6day': gridToCrimeMap[grid_row['id']]['6day'],'7day': gridToCrimeMap[grid_row['id']]['7day'],'8day': gridToCrimeMap[grid_row['id']]['8day'],
                        '9day': gridToCrimeMap[grid_row['id']]['9day'],'10day': gridToCrimeMap[grid_row['id']]['10day'],'11day': gridToCrimeMap[grid_row['id']]['11day'],'12day': gridToCrimeMap[grid_row['id']]['12day'],
                        '13day': gridToCrimeMap[grid_row['id']]['13day'],'14day': gridToCrimeMap[grid_row['id']]['14day'],'15day': gridToCrimeMap[grid_row['id']]['15day'],
                        '16day': gridToCrimeMap[grid_row['id']]['16day'],'17day': gridToCrimeMap[grid_row['id']]['17day'],'18day': gridToCrimeMap[grid_row['id']]['18day'],'19day': gridToCrimeMap[grid_row['id']]['19day'],
                        '20day': gridToCrimeMap[grid_row['id']]['20day'],'21day': gridToCrimeMap[grid_row['id']]['21day'],'22day': gridToCrimeMap[grid_row['id']]['22day'],'23day': gridToCrimeMap[grid_row['id']]['23day'],
                        '24day': gridToCrimeMap[grid_row['id']]['24day'],'25day': gridToCrimeMap[grid_row['id']]['25day'],'26day': gridToCrimeMap[grid_row['id']]['26day'],'27day': gridToCrimeMap[grid_row['id']]['27day'],
                        '28day': gridToCrimeMap[grid_row['id']]['28day'],'29day': gridToCrimeMap[grid_row['id']]['29day'],'30day': gridToCrimeMap[grid_row['id']]['30day']}, ignore_index=True)
        else:
            output = output.append({'Grid': grid_row['id'],'Hotspot':0, '1day': 0, '2day': 0, '3day': 0, '4day': 0,'5day': 0,'6day': 0, '7day': 0, '8day': 0, '9day': 0,'10day': 0,
                            '11day': 0, '12day': 0, '13day': 0, '14day': 0,'15day': 0,'16day': 0, '17day': 0, '18day': 0, '19day': 0,'20day': 0,'21day': 0, '22day': 0, '23day': 0, '24day': 0,'25day': 0,
                            '26day': 0, '27day': 0, '28day': 0, '29day': 0,'30day': 0}, ignore_index=True)
    #Output the file to the CSV
    output.to_csv(output_path)    
    return output