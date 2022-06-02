################################################################################################
#fuction name: fileRead
# Discription: Function to read the file
# Return: text after striping white space
################################################################################################
def fileRead():
    try:
        file = open("Transaction.txt","r", encoding ="ISO-8859-1")
        Text = file.read()     
        return Text.strip()
        file.close()
    except FileNotFoundError:
        print("File not found")
    except AttributeError:
        print("NoneType object has no attribute")
            
################################################################################################
#fuction name: makeDictionary
# Discription: Function to create a dictionary
# Return: dic = dictionary
################################################################################################
def makeDictionary():
    dic ={}
    i =0
    Text = fileRead()
    
    #if text exists
    if Text:
        trans = Text.split("\n")
        
        #loop through each line 
        for line in trans:     
            (userId, transId, disc, amnt, xaxis, yaxis, fraud) = line.split(':')
            dic.setdefault(userId,{})
            dic[userId][transId] = {"discription": disc, "amount":float(amnt), "xaxis": float(xaxis), "yaxis": float(yaxis), "fraud": fraud}        
    return dic 