'''
Sorting the list as per ascending order and remove duplicates if any
'''
my_input = [2, 3, 10, 1, 2, 5, 9, 17, 29, 31, 4]

my_count = 0
while my_count < len(list(my_input)):
    x = 0
    for i in range(len(my_input) - 1):
        if my_input[i] == my_input[i + 1]:
            del my_input[i]
            x = 1
            break
        if my_input[i] > my_input[i + 1]:
            temp = my_input[i]
            my_input[i] = my_input[i + 1]
            my_input[i + 1] = temp
    if x == 1:
        continue
    my_count += 1
print(my_input)