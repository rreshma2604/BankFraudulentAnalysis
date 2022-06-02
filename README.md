# BankFraudulentAnalysis
In order to design a fault detection system, three sample datasets are provided. We must  extract data from the given datasets: transaction.txt, fraud-description.txt, and description.txt. The first dataset (description.txt) comprises genuine transaction descriptions. The description  of fraudulent transactions can be found in the second dataset (fraud-description.txt) and the  actual transactions (10,000) data are contained in the last dataset (transaction.txt). The transaction dataset contains information about the transactions, such as their descriptions,  amounts, and locations. The location is just Euclidean coordinates in x and y points. The attributes of transaction dataset (transaction.txt) are: userID, transactionID, transaction description, transaction amount, each transaction's x coordinate, each transaction's y  coordinate and a Boolean label indicating whether the transaction is fraudulent.

Furthermore, we must create a user interface that allows the user to query and interact with a variety of statistical functions, such as the user's maximum and minimum transactions,standard deviation, variance etc. The user can opt out of this interface at any moment, and the features can be accessed several times.

IMPLEMENTATION OF SOLUTION
In order to implement a system that analyses bank customers' purchase transaction data to 
detect fraudulent behaviour, we are asked to design and construct three modules: 
load_dataset_module, user_statistics_module and test_module.
* Load_dataset_module
In this module, the specified dataset (transaction.txt) is loaded and saved into a 
dictionary with line-by-line data. 
* User_statistics_module 
In this module we must develop and implement eight functions that take data from 
the load_dataset_module to compute basic statistical functions.
a) Maximum and Minimum transaction.
b) Location centroid of user’s transaction.
c) Distance between any transaction location and centroid of a user.
d) Standard Deviation of transactions of any user.
e) Variance of transactions of any user.
f) Check if the transaction is fraudulent or not.
g) Distance between any two-transaction location of any user.
h) Distance between transaction location of two different users.
* Test_module:
Thisis the system's core module, providing the user interface routines that allow users 
to query and interact with all the system's functions

#python_programing #jupyter #dataset
