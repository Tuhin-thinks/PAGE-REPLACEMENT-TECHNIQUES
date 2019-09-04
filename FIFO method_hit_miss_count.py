# -*- coding: utf-8 -*-
"""
This program can calculate the hit and miss % using FIFO method.

Created on Wed Sep  4 16:42:16 2019

@author: tuhin Mitra
"""
print('Enter the Given string(without commas):')
string=input()
string_list=[i for i in string]
current_list=[]
hit_count=0
miss_count=0
count=0
frame_length=int(input('Enter Frame length:'))
print('Entered length of the string : {}\n{}'.format(len(string_list),16*'__'))
for i in string_list:
    if i not in current_list:
        if len(current_list)==frame_length:
            current_list.pop(0)
        current_list.append(i)
        miss_count+=1
        flag='miss'
    else:
        hit_count+=1
        flag='hit'
    count+=1
    print('>>{0} {1}{2}{3}{4}'.format('step',count,'.\n|','|\n|'.join(current_list),'|'))
    print(2*' ',flag,'\n')

miss_pecent=(miss_count/len(string_list))*100
hit_percent=(hit_count/len(string_list))*100
print('\nMiss count:{}, Hit count:{}\n{}'.format(miss_count,hit_count,16*'__'))
print('The miss percent is: {0:.2f} and\nthe hit percent is: {1:.2f}'.format(miss_pecent,hit_percent))