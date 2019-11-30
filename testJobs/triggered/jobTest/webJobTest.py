f = open("D:/home/site/wwwroot/webSuccess.txt", "w+")


for i in range(10):
    f.write("This is line %d\r\n" % (i+1))

f.close()