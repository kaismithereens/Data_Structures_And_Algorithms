"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()
my_new_stack = stack.Stack()

s.push(string)
print(s)

for char in string:
    my_new_stack.push(char)

while not my_new_stack.is_empty():
    reversed_string += my_new_stack.pop()

print(reversed_string)
