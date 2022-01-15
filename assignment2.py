# Student_ID--> 20CE060
# Name--------> Yash Narodia
# GITHUB-LINK->
# --------------------------------------Dictionaries---------------------------------
# 1)

from itertools import count
from multiprocessing import cpu_count


Dict_1 = {
    'Yash': 19,
    'Yug': 20,
    'Shruti': 21,
    'Aneri': 23
}

Dict_2 = {
    'Devansh': 24,
    'Hinata': 25,
    'Kageyema': 26,
    'Suki': 27
}
print("(1) Write a Python script to check whether a given key already exists in a dictionary.")

# 'a' is the key to be found and dict is the dictionary from which it has to found
def Key_present(a, dict):
    if a in dict:
        print("Present")
    else:
        print("Not Present")

Key_present('Yash', Dict_1)
Key_present('Yash', Dict_2)
# 2)-------------------------------------------------------------------------------
print("(2) Write a Python script to merge two Python dictionaries.")

def Join_dict(dict1, dict2):
    return dict1.update(dict2)
print(Dict_1)
# 3)-------------------------------------------------------------------------------
print("(3) Write a Python program to sum all the items in a dictionary.")

def SumDict(dict):
    sum = 0
    values = list(dict.values())
    print(values)
    for i in values:
        sum +=i
    return sum

print(SumDict(Dict_1))

# 4)-------------------------------------------------------------------------------
print("(4) Write a Python script to add a key to a dictionary.")

def appendDict(dict,key, value):
    dict[key] = value
    return dict

print(appendDict(Dict_2,"Abhi",30))

# 5)-------------------------------------------------------------------------------
print("(5)  Write a Python script to concatenate following dictionaries to create a new one.")


def mergeDict(dict1,dict2):
    res = {**dict1, **dict2}
    return res

Dict_3 = mergeDict(Dict_1, Dict_2)
# --------------------------------------Tuples---------------------------------
# 1)-------------------------------------------------------------------------------
print("(1) Write a Python program to create a tuple with different data types.")
tuple1 = (1,'yash', 19.5,[1,2,3],('a','b'))

# 2)-------------------------------------------------------------------------------
print("(2) Write a Python program to create a tuple with numbers and print one item.")
tuple2 = (1,2,3,4,5,6,7,8,9,0)
print(tuple2[5])

# 3)-------------------------------------------------------------------------------
print("(3) Write a Python program to add an item in a tuple.")
l = list(tuple1)
l.append(10)
tuple3 = tuple(l)
print(tuple3)

# 4)-------------------------------------------------------------------------------
print("(4) Write a Python program to convert a tuple to a string.")
def TupleToString(tuple):
    str = ''
    for i in tuple:
        str+=i
    return str

tuple3 = ('y','a','s','h')
print(TupleToString(tuple3))

# 5)-------------------------------------------------------------------------------
print("(5) Write a Python program to find the length of a tuple.")

def tupleLength(tuple):
    l = list(tuple)
    length = len(l)
    return length

print(tupleLength(tuple2))


# --------------------------------------Set---------------------------------
# 1)-------------------------------------------------------------------------------
print("(1) Write a Python program to add member(s) in a set and clear a set")

set1 = {'red','blue'}
print('set1 ',set1)
set1.add('green')
print('after adding',set1)
set1.clear()

# 2)-------------------------------------------------------------------------------
print("(2) Write a Python program to remove an item from a set if it is present in the set.")

def removeFromSet(set, value):
    if value in set:
        set.remove(value)
    else:
        print('value not in set')
# 3)-------------------------------------------------------------------------------
print("(3) Write a Python program to create an intersection, Union, difference of sets.")

A = {0, 2, 4, 6, 8, 10}
B = {1, 2, 3, 4, 5, 6}
print("Intersection: ",A&B)
print("Union: ",A|B)
print("Difference: ",A-B)

# 4)-------------------------------------------------------------------------------
print('(4) Write a Python program to find maximum and the minimum value in a set.')
print('Max in set A',max(A))
print('Min in ser B',min(A))
# 5)-------------------------------------------------------------------------------
print('(5) Write a Python program to find the most common elements and their counts from list, tuple, dictionary.')

dict = {1:2,2:3,3:4,4:4,5:4}
tuple4 = (2,3,4,4,5,4)
list2 = [2,2,3,3,4,4,5,4,4]

def frequncyTuple(tuple1):
    l = list(tuple1)
    count = 0
    num = l[0]
    for i in l:
        cur_freq = l.count(i)
        if(cur_freq>count):
            count = cur_freq
            num = i     
    print('Number is : ',num, '\n frequncy is : ',count)

def frequncyList(list1):
    count = 0
    num = list1[0]
    for i in list1:
        cur_freq = list1.count(i)
        if(cur_freq>count):
            count =cur_freq
            num = i
    print('Number is : ',num, '\n frequncy is : ',count)

def frequncyDict(dict):
    count = 0
    values = list(dict.values())
    print(values)
    value  = values[0]  
    for i in values:
        cur_freq = values.count(i)
        if (cur_freq>count):
            count = cur_freq
            value = i

    print('Number is :',value ,'\nfrequncy is :',count)
    
frequncyDict(dict)
frequncyList(list2)
frequncyTuple(tuple4)