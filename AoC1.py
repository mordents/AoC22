# The Elves document snack calories# 
# For example, suppose the Elves finish writing their items' Calories and end up with the following list:
# Separated by blank lines - add 
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying? 
import re 
with open('input.txt', 'r') as input:
    lines= input.readlines()                        #read in all lines#
    calories = [line.strip() for line in lines]    #remove trailing input 

total=[]
sum = 0
for x in calories:
    if x!="":
        sum+=int(x)
    elif x=="":
        total.append(sum)
        sum=0
totalsort=sorted(total,reverse=True)        
sum2=totalsort[0]+totalsort[1]+totalsort[2]
print(sum2)
# add things in between  /n blank /n #