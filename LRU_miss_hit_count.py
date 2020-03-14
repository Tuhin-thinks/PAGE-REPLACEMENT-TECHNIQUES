# -*- coding: utf-8 -*-
"""
This program can calculate the hit and miss % using FIFO method.

Created on Wed Sep  4 16:42:16 2019

@author: tuhin Mitra
"""
demo = """
You Can Either enter string like this:
    1,3,0,3,5,6
        or,
    You can Also Enter like this:
        130356
(for better readability the first method is recommended,

However--> For quick and easy entry you can also use the 2nd method of input)
        --- in both the cases you get the same output ---
"""
print(f"{demo}\n")
print('Enter the Given string (separated by commas):')  # actually if you don't separate by commas,it'll still not give
# any problem
string = input()
if ',' in string:
    string_list = string.replace(' ', '').split(',')
else:
    string_list = [i for i in string]

current_list = []
hit_count = 0
miss_count = 0
count = 0
input_used = []
frame_length = int(input('Enter Frame length:'))
print('Entered length of the string : {}\n{}'.format(len(string_list), 16 * '__'))
for pos,i in enumerate(string_list):
    if i not in current_list:
        if len(current_list) == frame_length:
            repl_ind = len(input_used)
            elem = 'x'
            for j in current_list:
                for k in range(len(input_used)-1,-1,-1):
                    if input_used[k] == j:
                        if  k < repl_ind:
                            repl_ind = k
                            elem = input_used[k]  # getting the L.R.U element
                            break
                        else:
                            break
            ind = current_list.index(elem)
            current_list.pop(ind)
            current_list.insert(ind,i)
        else:
            # input_used.append(i)
            current_list.append(i)
        miss_count+=1
        flag = "miss"
    else:
        hit_count+=1

        flag="hit"
    input_used.append(i)
    temp_list = current_list.copy()
    temp_list.reverse()
    print_string = '|\n|'.join(temp_list)
    print(f">>step: {pos + 1} with({i}).\n|{print_string}|")
    print(2 * ' ', flag, '\n')




miss_pecent = (miss_count / len(string_list)) * 100
hit_percent = (hit_count / len(string_list)) * 100
print('\nBy L.R.U Page replacement technique–\nMiss count:{}, Hit count:{}\n{}'.format(miss_count, hit_count, 16 * '__'))
print('The miss percent is: {0:.2f} and\nthe hit percent is: {1:.2f}'.format(miss_pecent, hit_percent))
