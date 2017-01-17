

#Import regexp module
import re

print ("Hello World!\tkTest")

# Print the output of a calculation
print (1+1)

# Assign value of calcuation to a variable
NUM1 = 1+1

# print a string and variable
print "NUM1 =", NUM1, NUM1


# split a string, specifying a delimiter, and then which element
print ("Hello World").split(" ")[0]

# Boolean examples
print 5 == 5

print "this" is "This"
print "this" is not "This"

# Lists
print ["This", "is", "a", "list"][0]

# Dictionaries
print {"Name": "Kevin", "Surname": "Pillay"}["Name"]

# Function example One
def function_one():
    print ("Function One")

function_one()

# Function example Two
def function_two(str1, str2):
    print (str1)
    print (str2)

function_two("String 1", "String 2")

# Function example Three - settings defaults and keyword arguments
def function_three(name = "Someone", age = "Unknown"):
    print "My name is", name, "and my age is ", age

function_three(age=3000, name="Narg")

# Function example Four - infinite arguments
def function_four(*array):
    for item in array:
        print"Item Value:",item

function_four("Item1", "Item2", "Item3")

# Function example Five - returning values
def function_five(num1, num2):
    return num1+num2

print"Adding:",function_five(1,2)

# Conditional statements

VAR1 = 1

if VAR1 == 2:
    print"VAR1 = 2"
elif VAR1 == 3:
    print"VAR1 = 3"
else:
    print"VAR1 not equal to 2 OR 3"

# Loop - "for" loop example
mylist = [1,2,3,4,5]

for element in mylist:
    print element


# Loop - "while" loop example

state = True
myval = 1

while state:
    if myval == 20:
        print "All done!"
        state = False
    else:
        print "myval =", myval
        myval += 1


# RegEx
mystr = "THIS IS a string, with upper, lower case chars. It also has 1 2 3 4 numbers"

newstr = re.sub('[A-Z]', '', mystr)
print newstr

newstr = re.sub('[a-z]', '', mystr)
print newstr

newstr = re.sub('[,]', '!!', mystr)
print newstr

newstr = re.sub('[,.]', '!!', mystr)
print newstr

newstr = re.sub('[0-9A-Za-z]', '!!', mystr)
print newstr

newstr = re.sub('[0-9+" "]', '~', mystr)
print newstr

newstr = re.sub('[^0-9]', '~', mystr)
print newstr