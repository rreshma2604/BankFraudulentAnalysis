################################################################################################
#fuction name: minAndMax
# Discription: Function to find the maximum and minimum amount of transactions of any user
# Parameter(s): dic - it is dictionary containing transition id, disc, amnt, xaxis, yaxis, fraud
# Return: this function returns a tuple with minimum, maximum amount
################################################################################################
def minAndMax(dic):
    maxVal = 0
    minVal = maxVal
    
    #loop to get minimum and maximum from all the transactions
    for y in dic:
        
        #if condition to check if the transaction amount is greater than maxval
        if dic[y]['amount'] > maxVal:
            maxVal = dic[y]['amount']
            temp = dic[y]['amount']
        elif dic[y]['amount'] < minVal: # if above condition fails to check if the transaction amount is less than maxval
            minVal = dic[y]['amount']
        else:
            if (minVal == 0):
                minVal = temp
            continue;
    return (minVal,maxVal)  

################################################################################################
#fuction name: calcCentroid
# Discription: Function to find the location centroid of any user based on their transaction locations
# Parameter(s): dictxy - it is dictionary containing transition id, disc, amnt, xaxis, yaxis, fraud
# Return: this function returns the  location centroid
################################################################################################
def calcCentroid(dictxy):
    xsum =0
    ysum =0
    count = 0
    
    #loop through dictionary to sum all the transaction xaxis and yaxis
    for y in dictxy:
        xsum += dictxy[y]['xaxis'] #to get the xaxis
        ysum += dictxy[y]['yaxis'] #to get yaxis
        count += 1
    return (round((xsum/count),2), round((ysum/count),2))

################################################################################################
#fuction name: transLocation
# Discription: Function to find the distance of any transaction location from the centroid
# Parameter(s): dis - it is dictionary containing transition id, disc, amnt, xaxis, yaxis, fraud
#               centroid - transaction centroid of the user 
# Return: this function returns the  location 
################################################################################################
def transLocation(dis, centroid):
    xval =0
    yval = 0
    xval = difference(centroid[0] , dis["xaxis"])#used difference() for calculation difference
    yval = difference(centroid[1] , dis["yaxis"])#used difference() for calculation difference        
    return (round(xval,2),round(yval,2))

################################################################################################
#fuction name: StandardDeviation
# Discription: Function to find the variance and standard deviation
# Parameter(s): dis - it is dictionary containing transition id, disc, amnt, xaxis, yaxis, fraud
# Return: this function returns the variance and standard deviation
################################################################################################
def StandardDeviation(dic):
    amountSum =0
    count =0
    var = 0
    stdDev =0
    
    #loop to sum the amount and find the length
    for amnt in dic:
        amountSum += float(dic[amnt]["amount"])
        count +=1
    mean = amountSum/count;
    
    #loop to square the difference between amount and mean then sum it and divide by number
    var = sum(((dic[x]["amount"])-mean)**2 for x in dic)/count
    stdDev = var ** 0.5 # squareroot of variance
    return (round(var,2),round(stdDev,2))

################################################################################################
#fuction name: identifyFraud
# Discription: Function to find if the transaction is fraudulent or not
# Parameter(s): trasaction - it is dictionary containing transition id, disc, amnt, xaxis, yaxis, fraud
# Return: this function returns the message 
################################################################################################
def identifyFraud(transaction):
    
    #condition to check if the transaction fraud status
     if(transaction["fraud"] == 'true'):
        return (errorMsg("Sorry, but the transaction is a fraudulent\n \033[1m Transaction Details \033[0;0m \nDiscription: "+transaction["discription"]+"\ncordinates: ("+str(transaction["xaxis"])+","+str(transaction["yaxis"])+")"))
     else:
        return successMsg("The transaction is a valid one and not a fraudulent")

################################################################################################
#fuction name: distanceBtwTransaction
# Discription: Function to find the the distance of transactions of any two users
# Parameter(s): dic1 = tuple with details of 1st user and dic2 = tuple with details of 2nd user
# Return: this function returns the coordinates
################################################################################################    
def distanceBtwTransaction(dic1, dic2):
    xaxis = difference(dic1["xaxis"] , dic2["xaxis"])
    yaxis = difference(dic1["yaxis"] , dic2["yaxis"])         
    return (xaxis,yaxis) 

################################################################################################
#fuction name: distbtw2trans
# Discription: Function to find the distance between any two given transactions of any user
# Parameter(s): trans1= tuple with details of one transaction and trans2 = tuple with details of second transaction
# Return: this function returns the coordinates
################################################################################################
def distbtw2trans(trans1,trans2):
    xaxis = difference(trans1["xaxis"],trans2["xaxis"])
    yaxis = difference(trans1["yaxis"],trans2["yaxis"])
    return (xaxis,yaxis)

################################################################################################
#fuction name: getUserId
# Discription: Function to get the userid from the user and check if the user id is valid
# Parameter(s): dic - it is dictionary containing userid, transition id, disc, amnt, xaxis, yaxis, fraud
# Return: uid if it is valid userid else return 0
################################################################################################
def getUserId(dic):
    uid = input("\nPlease enter the Userid:  ")
    
    #condition to check if the user is exists
    if str(uid) in dic:
        return uid;
    else:
        print(errorMsg('User id  doesn\'t exist'))
        return 0
    
################################################################################################
#fuction name: getTrans
# Discription: Function to get the transaction id from the user and to verify if the id is valid or not
# Parameter(s): dictn - it is dictionary containing transition id, disc, amnt, xaxis, yaxis, frau
# Return: transaction id if exists else return 0
################################################################################################        
def getTrans(dictn):
    
    #loop to display the transaction id with discription for users reference
    for x in dictn:print("\x1b[35m"+x+":"+dictn[x]["discription"]+"\x1b[0m", end ="   |   ")      
    tid = input("\nPlease enter the transaction id:  ")
    
    #check if the transaction id exists
    if str(tid) in dictn:
        return tid;
    else:
        print(errorMsg('Transaction id  doesn\'t exist'))
        return 0
    
################################################################################################
#fuction name: difference
# Discription: Function to find the the difference between two numbers
# Parameter(s): val1, val2
# Return: Difference of two number
################################################################################################    
def difference(val1,val2):
    diff =0
    if val1 > val2:
        diff = val1 -val2
    else:
        diff = val2-val1
    return diff 

################################################################################################
#fuction name: errorMsg
# Discription: Function to print the error message in red color
# Parameter(s): string-error message
# Return: message in red colour
################################################################################################
def errorMsg(string):
    return "\x1b[31m"+ string +"\x1b[0m"

################################################################################################
#fuction name: successMsg
# Discription: Function to print the success message in green color
# Parameter(s): string-Success message
# Return: message in green colour
################################################################################################
def successMsg(string):
    return "\x1b[32m"+ string +"\x1b[0m"
    