#Sum all the items in a list Exercise-1
#https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.php
a=[10,12,20,22]
sum=0
for i in range(len(a)):
    sum+=a[i]
print("The sum is {}".format(sum))