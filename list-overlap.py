'''
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] and write a program that
  returns a list that contains only the elements that are common between the lists (without duplicates). Make sure
  your program works on two lists of different sizes
'''


def list_overlap(list_a, list_b):
    output_c = []
    for x in list_a:
        for y in list_b:
            if x == y:
                if x not in output_c:
                    output_c.append(x)
                break
    return output_c


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

my_output_c = list_overlap(a, b)

print(my_output_c)

# one line code
print(set(a).intersection(set(b)))
