#f = open("D:/home/site/wwwroot/webSuccess.txt", "w+")


import logging

logging.basicConfig(filename='D:\\\\home\\webJobTest.log', level=logging.INFO, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.error('This will get logged to a file')


num = 0
for i in range(10):
    num += i
    #f.write("This is line %d\r\n" % (i+1))

#f.close()
print(num)
logging.info("testing log")
print("test")