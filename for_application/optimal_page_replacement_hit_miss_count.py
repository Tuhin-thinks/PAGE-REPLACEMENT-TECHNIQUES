# -*- coding: utf-8 -*-
"""
This program can calculate the hit and miss % using FIFO method.

Created on Wed Sep  4 16:42:16 2019

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
def solve(string_list, frame_length):
    # print('Enter the Given string (separated by commas):')  # actually if you don't separate by commas,it'll still
    # not give any problem

    current_list = []
    hit_count = 0
    miss_count = 0
    # count = 0
    # frame_length = int(input('Enter Frame length:'))
    display_line = 'Steps Display for OPT Method:\n'

    # print()
    for pos, i in enumerate(string_list):
        if i not in current_list:
            if len(current_list) == frame_length:
                replace_index = 0  # set some arbitrary value
                for j in range(len(current_list)):
                    if current_list[j] not in string_list[pos:]:
                        repl_index = j
                        break
                    else:  # if future use of the page is found
                        use_index = string_list[pos:].index(current_list[j])
                        if use_index > replace_index:
                            replace_index = use_index
                            repl_index = j

                current_list.pop(repl_index)
                current_list.insert(repl_index, i)
            else:
                # current_list.insert(0, i)
                current_list.append(i)
            miss_count += 1
            flag = "miss"
        else:  # page is found in current frame
            hit_count += 1
            flag = "hit"

        temp_list = current_list.copy()
        temp_list.reverse()
        print_string = '|\n|'.join(temp_list)
        # print(f">>step: {pos + 1} with({i}).\n|{print_string}|")
        # print(2 * ' ', flag, '\n')
        display_line += f"\n>>step: {pos + 1} with({i}).\n|{print_string}|"+'\n'+f"{2*' '}{flag}\n"

    miss_pecent = (miss_count / len(string_list)) * 100
    hit_percent = (hit_count / len(string_list)) * 100
    # print('\nBy Optimal Page replacement –\nMiss count:{}, Hit count:{}\n{}'.format(miss_count, hit_count, 16 * '__'))
    display_line += '\n' + '\nBy Optimal Page replacement –\nMiss count:{}, Hit count:{}\n{}'.format(miss_count,
                                                                                                     hit_count,
                                                                                                     16 * '__')
    # print('The miss percent is: {0:.2f} and\nthe hit percent is: {1:.2f}'.format(miss_pecent, hit_percent))
    display_line += '\n' + 'The miss percent is: {0:.2f} and\nthe hit percent is: {1:.2f}'.format(miss_pecent,
                                                                                                  hit_percent)
    display_line += f"\n{14*'  '}--by Tuhin Mitra"
    # print(display_line)
    return display_line


# string = "1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6"
# frame_length = 4
# if ',' in string:
#     string_list = string.replace(' ', '').split(',')
# else:
#     string_list = [i for i in string]
# print(solve(string_list, frame_length))

# ans should be miss:8 and hit:12
# for input_string = 1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6
