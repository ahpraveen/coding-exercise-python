'''
Lets say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''

my_input = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
my_new_list = [x for x in my_input if x % 2 == 0]
print(my_new_list)
