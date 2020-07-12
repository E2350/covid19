# -*- coding: utf-8 -*-

fibo_num =[1]

sum =1

for i in range(1,55):
    fibo_num.append(sum)
    sum = fibo_num[i-1]+fibo_num[i]
    if sum >55:
        break
    
print(fibo_num)