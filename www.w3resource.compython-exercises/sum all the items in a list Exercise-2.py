#sum all the items in a list Exercise-2.py
#https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.php

def sum_list(items):
    sum=0
    for i in range(len(items)):
        sum+=items[i]
    return sum

print(sum_list([3,4,-9,4]))