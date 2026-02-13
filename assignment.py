#ADDITON
A=2
B=3
c=A+B
print("ADDITION", c)

#SUBTRACTION
A=5
B=1
C=A-B
print("SUBTRACTION", C)

#MULTIPLICATION
A=2
B=1
C=A*B
print("MULTIPLICATION", C)

#DIVISION
A=4
B=2
C=A/B
print("DIVISION", C)

#FLOOR DIVISION
A=17
B=3
C=A//B
print("FLOOR_DIVISION", C)

#AESTHERIC
A=4
B=4
C=A**B
print("AESTHERIC", C)

#modulo
a=3
b=3
c=a%b
print(c)



#print ()
print("hello")

#variables assignment(=)
x=1

#comment(#)
#This is a comment

# data types (int boolean)
pelumi=10 #int
is_me=True #boolean

#Arithmetic operators (+ -)
x=5+3
x=5-3

#input (input())
name=input("Enter your name:")

#if statement
if x>10:
    print("big number")

#Else statement
else:
    print("small number")

#Elif
    elif x==10:
print("Equal")

#for loop
for i in range (5):
    print(i)

#while loop
 while x<10:
    x+=1

#Break is used to stops loop
break

#continue used to skips loop iteration
continue

#functions(def)
def greet():
    print("Hello")

#Return statement
    return x+y

#List({})
numbers={1,2,3}

#Tuples cannot be change in a code we use it mainly when we are using constant they are immotable
point=(3,4)

#Dictionaries([])
person=["name:" "pelumi", "age:12"]

#Sets(set())
items={1,2,3}

#Indexing is used for accessing an item by position
numbers[0]

#slicing is use for extracting a portion of a sequence
numbers[1:3]

#Len is use to return the number of items
len(numbers)

#Import loads a module or library
import math

#Class used to create objects in OOP
class car:
    pass

#Try/except used to handle errors
try:
    x=5/0
except:
    print("Error!")

#with used for safe resource handling (e.g, files)
with open("file.text") as f:
    data =f.read()

#Pass used for a placeholder statement (does nothing)
pass

#In operator used for checking membersship
if 3 in numbers:
    print("found")

#Not, and, or logical operators
if x>5 and x<10:
    print("between")

#F-strings used for formatting strings
name="john"
print(f"Hello, {name}")




