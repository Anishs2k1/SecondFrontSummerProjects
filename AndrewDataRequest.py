#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import pandas as pd
import numpy as np
import xlrd
import sys
import os

def convertingnan(data1, data2):
    #Writing a script in order to take values from Justifications feature from 1 data set and populate the same column in another dataset 
    #where the CVE ID justifications are empty


    #excluding the data except for the 4 main features neccessary 
    excel_cus = pd.read_excel(data1)
    excel1 = excel_cus[['cve', 'package', 'package_version', 'Justifications']]
    excel_raw = pd.read_excel(data2)
    excel2 = excel_raw[['cve', 'package', 'package_version', 'Justifications']]
    
    
    #filling all NA values with 1 to make it easily identifiable
    excel2['Justifications'] = excel2['Justifications'].fillna(1)


    #merging the 3 features together to make it easier to match similar features
    excel1['newcve'] = excel1[['cve', 'package_version', 'package']].apply(lambda x: '-'.join(x[x.notnull()]), axis = 1)
    excel2['newcve'] = excel2[['cve', 'package_version', 'package']].apply(lambda x: '-'.join(x[x.notnull()]), axis = 1)
    excel1 = excel1[['newcve', 'Justifications']]  
    excel2 = excel2[['newcve', 'Justifications']]
    
    #creating a dictionary allowing us to use it as a key for searching for Justifications and CVEs
    justifications_dict = dict(zip(excel1["newcve"], excel1["Justifications"]))

    #iterating through the Justification columns on the raw dataset
    #if the Justification is not nan it adds to a seperate list
    #if it is nan then it alters the Justification to the correct one and then adds it to the list
    tmplist = []
    count = 0
    for values in excel2['Justifications']:
        if values != 1:
            tmplist.append(values)
            count +=1
        elif values == 1:
            z1 = excel2.loc[count, 'newcve']
            if z1 in justifications_dict:
                tmplist.append(justifications_dict.get(z1))
                count +=1
                
    #declares the new list in place of the original justifications                
    excel_raw['Justifications'] = tmplist
    return excel_raw
    #excel_raw.to_excel("updated_raw.xlsx")

x = input("Enter the path of your file: ")
assert os.path.exists(x) , "I did not find the file at, "+str(x)
#newx = open(x,'r+')
y = input("Enter the path of the second file: ")
assert os.path.exists(y) , "I did not find the file at, "+str(y)
#newy = open(y, 'r+')
#x = "customer_anchore.xlsx"
#y = "raw_anchore.xlsx"
finaldataset = convertingnan(x, y)
finaldataset.to_excel("finaldataset.xlsx")
print("all done!")


#/Users/zaha/Downloads/customer_anchore.xlsx
#/Users/zaha/Downloads/raw_anchore.xlsx

