# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:59:58 2019

@author: Bidhan
"""

import sys

data=[]
data_extract=[]
operate={}

fin = open ('friday.txt', 'r')
fout = open ('friday.out', 'w')
p=0

for line in fin:
    data.append(line.strip("\n"))
    #print(data[p])
    #p+=1
    
#x=0
N=int(data[0])

final_output=[]

for j in range(32):
    operate[j]="?"

def OR(i,j):
    if (i==1 or j==1):
        return 1
    if (i==0 and j==0):
        return 0
    if (i=="?" and j=="?"):
        return("?")
    if (i==0 and j=="?"):
        return("?")
    if (i=="?" and j==0):
        return("?")
    

def AND(i,j):
    if (i=="?" and j=="?"):
        return("?")
    if (i==0 or j==0):
        return 0
    if (i==1 and j=="?"):
        return("?")
    if (i=="?" and j==1):
        return("?")
    if (i==1 and j==1):
        return 1    
    
    
def CLEAR(i):
    return(0)
    
def SET(i):
    return(1)

int_entries=[]
for x in range(len(data)):
    if(len(data[x])<=2):
        int_entries.append(x)
    
final_print=""
    #N=int(data[x])
for i in range(len(int_entries)):
    N=int_entries[i]
    #if(type(int(data[N+1]))!=int):
    for j in range(int(data[N])):
        data_extract = data[N+j+1].split(" ")
        print(data_extract)
        if(data_extract[0]=="OR"):
            operate[int(data_extract[1])] = OR(operate[int(data_extract[1])],operate[int(data_extract[2])])
        if(data_extract[0]=="AND"):
            operate[int(data_extract[1])] = AND(operate[int(data_extract[1])],operate[int(data_extract[2])])
        if(data_extract[0]=="SET"):
            operate[int(data_extract[1])] = SET(operate[int(data_extract[1])])
        if(data_extract[0]=="CLEAR"):
            operate[int(data_extract[1])] = CLEAR(operate[int(data_extract[1])])
       
    for k in range(32):
        if int(data[N])!=0:
            #fout.write(str(operate[31-k]))
            final_print = final_print+str(operate[31-k])
            #print(k)
            #print(operate[31-k])
            if k==31:
                final_output.append(final_print)
                final_print=[]
                
        
                    

                
        
    




    

    
