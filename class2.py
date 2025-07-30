# # set - example
# s = {1,2,3,4}
# print(s)

# d = set()
# d.add(5)
# print(d)

# s1 = {1,2,3}
# s2 = {3,4,5}
# print(s1.union(s2))
# print(s1.intersection(s2))

# # frozenset - example
# fs = frozenset([1,2,3,3,2])
# print(fs)

# s = {frozenset([1,2]), frozenset([3,4])}
# print(s)

# #defaultdict - example
# from collections import defaultdict

# d2 = defaultdict(list)
# d2['x'].append(10)
# print(d2)

# try-except - example
# try:
#     num = int(input('Enter the number: '))
#     result = 10/num
#     print('Result is: ', result)
# except ZeroDivisionError:
#     print('Cannot divide by Zero')
# except ValueError:
#     print('Invalid input, please enter a number') 

import turtle
t = turtle.Turtle()
for i in range(50):
    t.forward(74)
    t.right(150)
turtle.done()    
