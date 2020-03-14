# -*- coding: utf-8 -*-
"""
This program can calculate the hit and miss % using FIFO method.

Created on Wed Sep 4 16:42:16 2019

@author: tuhin Mitra
"""


# demo = """
# You Can Either enter string like this:
#     1,3,0,3,5,6
#         or,
#     You can Also Enter like this:
#         130356
# (for better readability the first method is recommended,
#
# However--> For quick and easy entry you can also use the 2nd method of input)
#         --- in both the cases you get the same output ---
# """
# print(f"{demo}\n")
# print('Enter the Given string (separated by commas):') # actually if you don't separate by commas,it'll still not give
# # and problem
# string = input()
# if ',' in string:
#     string_list = string.replace(' ', '').split(',')
# else:
#     string_list = [i for i in string]


def solve(string_list, frame_length):
    current_list = []
    hit_count = 0
    miss_count = 0
    count = 0
    display_line = "Steps Display for FIFO Method:\n"
    # frame_length = int(input('Enter Frame length:'))
    # print('Entered length of the string : {}\n{}'.format(len(string_list), 16 * '__'))
    for i in string_list:
        if i not in current_list:
            if len(current_list) == frame_length:
                current_list.pop(0)
            current_list.append(i)
            miss_count += 1
            flag = 'miss'
        else:
            hit_count += 1
            flag = 'hit'
        count += 1
        temp_list = current_list.copy()  # a copy list created to keep safe the actual content
        temp_list.reverse()
        # print('>>{0} {1} with:({2}){3}{4}{5}'.format('step', count, i, '.\n|', '|\n|'.join(temp_list), '|'))
        # print(2 * ' ', flag, '\n')
        display_line += "\n" + '>>{0} {1} with:({2}){3}{4}{5}'.format('step', count, i, '\n|', '|\n|'.join(temp_list),
                                                                      '|') + f"\n{2 * ' '} {flag} \n"

    miss_pecent = (miss_count / len(string_list)) * 100
    hit_percent = (hit_count / len(string_list)) * 100
    # print('\nMiss count:{}, Hit count:{}\n{}'.format(miss_count, hit_count, 16 * '__'))
    display_line += '\n\nMiss count:{}, Hit count:{}\n{}'.format(miss_count, hit_count, 16 * '__')
    # print('The miss percent is: {0:.2f} and\nthe hit percent is: {1:.2f}'.format(miss_pecent, hit_percent))
    display_line += '\nThe miss percent is: {0:.2f} and\nthe hit percent is: {1:.2f}\n'.format(miss_pecent, hit_percent)
    display_line += f'\n{14*" "}--by Tuhin Mitra'
    return display_line