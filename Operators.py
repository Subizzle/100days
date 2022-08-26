mylist = [1,2,3,4,5,6,7,8,9,10]
print (mylist)

# range

for num in range(10):
    print(num)

for steps in range(0,10,5):
    print(steps)

a = list(range(0,10,3))
print(a)

#enumerate

index_count = 0

for letter in 'abc':
    print('At index {} the letter is {}.'.format(index_count,letter))
    index_count += 1

#tuples

word = "hello"

for item in enumerate(word):
    print(item)
    index_count += 1

#tuple unpacking

word = "hello"

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

#zip

mylist1 = ['red', 'white', 'blue']
mylist2 = ['car', 'truck', 'bike']
mylist3 = [1,2,3]

for item in zip(mylist1,mylist2,mylist3):
    print(item)

b = list(zip(mylist1,mylist2,mylist3))
print(b)

#in

incheck = 'x' in mylist1
print(incheck)

incheck1 = 'car' in mylist2
print(incheck1)

password = 'ghity*&^'
incheck2 = '&' in password
print(incheck2)

incheck3 = 'key1' in {'key1':1}
print(incheck3)

c = {'key1':1}
incheck4 = 1 in c.values()
print(incheck4)

incheck5 = 2 in c.keys()
print(incheck5)

#min max

d = [100,345,678678678,423426778456456]
print(min(d))
print(max(d))

#random library shuffle

from random import shuffle
from unittest import result
e = ['a','b','c','d','e','f','g','h',]
shuffle(e)
print(e)

#random integer
from random import randint
print(randint(0,9999))

mynum = randint(0,100000)
print(mynum)

#input; always a string
z = input("What is favorite number?")
print(z)
print(type(z)) #class string

y = int(input("Number?"))
print(y)
print(type(y)) #class integer

x = float(input("Number?"))
print(x)
print(type(x)) #class float
