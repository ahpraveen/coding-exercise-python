'''
Sorting the list as per ascending order and remove duplicates if any
'''


def sorting_list(my_input_param):
    my_count = 0
    while my_count < len(list(my_input_param)):
        x = 0
        for i in range(len(my_input_param) - 1):
            if my_input_param[i] == my_input_param[i + 1]:
                del my_input_param[i]
                x = 1
                break
            if my_input_param[i] > my_input_param[i + 1]:
                temp = my_input_param[i]
                my_input_param[i] = my_input_param[i + 1]
                my_input_param[i + 1] = temp
        if x == 1:
            continue
        my_count += 1
    return my_input_param


my_input = [2, 3, 10, 1, 2, 5, 9, 17, 29, 31, 4, 1, 3, 5, 2]
print('Before sorting ', my_input)
print('After sorting', sorting_list(my_input))
