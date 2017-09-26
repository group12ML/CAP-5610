###### INSTRUCTIONS FOR USE ######################################
# Copy and paste this line into your shell to use the function   #
# and make sure your shell is running in the same directory      #
#                                                                #
# from excelToArray import excelToArray                          #
#                                                                #
# Example for how to use the function                            #
# x = excelToArray()                                             #
# OR                                                             #
# x = excelToArray("spreadsheet_name.xls")                       #
##################################################################

def excelToArray(filename = "dataset.xlsx"):

    import numpy as np
    import pandas as pd

    # Inputs data from spreadsheet
    df = pd.read_excel(filename)

    # Uncomment this line to print the spreadsheet's dimensions
    #print "df.shape: ", df.shape

    # Store dimensions of the datafile
    noRow = df.shape[0]
    noCol = df.shape[1]

    # Creates a blank array with the opposite dimensions as the spreadsheet
    # because reading the transpose was easier, we change it back at the end
    finalDat = np.empty((df.shape[1],df.shape[0]))

    # Uncomment to show finalDat dimensions
    #print "finalDat.shape: ", finalDat.shape
    
    # Copies the excel array into finalDat column by column
    j = 0
    for i in df.columns:
        tempCol = df[i]
        finalDat[j] = tempCol
        j += 1

    # Returns the matrix to it's original form
    finalDat = finalDat.transpose() 

    # Uncomment to show finalDat dimensions after transpose
    #print "finalDat.shape AFTER transpose: ", finalDat.shape

    return finalDat
