# -*- coding: utf-8 -*-

n = int(input("Enter a limit number: "))
my_list = []


for i in range(2,n+1):
    counter = 0
    for j in range(1,i+1):
        if i % j  == 0:
            counter+=1
    if counter==2:
        my_list.append(i)                
print(my_list)
   




            

       