#!/usr/bin/env python
# coding: utf-8

# # Automate Boring Stuff with Python

# ## I. Basics

# ### Lesson 1 : Getting Help
# * Explain what you are trying to do, not just what you did.
# * If you get an error message, specify the point at which the error happens. (Including the line number.)
# * Explain what you’ve already tried to do to solve your problem.
# * List the version of Python you’re using.

# ### Lesson 2: Getting Started
# 
# * An instruction that evaluates to a single value is an expression. An instruction that doesn't is a statement.
# * IDE is an editor. Jupyter is specifically for Data science and scientific computing while VS code is for software development. 
# * The interactive shell window has the >>> prompt.
# * Data types: 
#     * Numeric: int, float, complex
#     * Character: String
#     * Bool
# * Strings hold text and begin and end with quotes: ‘Hello world!'
# * Values can be stored in variables: spam = 42
# * Variables can be used anywhere values can be used in expressions: spam + 1

# In[13]:


2 + 2 #This is an Expression


# In[16]:


X = 2 + 2 # This a Statement (usually to create variables)


# In[8]:


# Operator Predence Concept

(2 + 2) * 5 # BODMAS


# In[19]:


# Variable always keeps on Updating

x = 2  #Old value
x = 3  #New value
x


# ### Lesson 3: Writing First Program
# 
# * The execution starts at the top and moves down.
# * Comments begin with a # character and are ignored by Python; they are notes & reminders for the programmer.
# * Functions are like mini-programs in your program.
# * The print() function displays the value passed to it.
# * The input() function lets users type in a value. (String by Default)
# * The len() function takes a string value and returns an integer value of the string's length.
# * The int(), str(), and float() functions can be used to convert values' data type.

# In[36]:


print('Hey Buddy, What is your name?')
myname = input()
print('What is your age?')
myage = int(input())
lenname = len(myname)
print('Nice to meet you', myname)
print('Your name has', lenname, 'letters')
print('You will be', myage + 1, 'on your next birthday, Cheers!')


# ## II. Flow Control

# *Flow Control controls the order of execution of statements based on Conditions*
# 
# Three Types:
#   * If Else, Elif
#   * While Loops
#   * For Loop
#   
#  Flow Control involves three things
#  
#   * Boolean Value
#   * Comparison Operators
#   * Boolean or Logical Operators: *are used to evaluate boolean values or expressions.*

# ### Lesson 4: How Flow Control Works
# 
# * The Boolean data type has only two values: True and False (both beginning with capital letters).
# * Comparison operators compare two values and evaluate to a Boolean value: ==, !=, <, >, <=, >=
# * == is a comparison operator, while = is the assignment operator for variables.
# * Logical or Boolean operators (and, or, not) also evaluate to Boolean values.

# In[41]:


True and True # Only True Condition for and


# In[50]:


print(True or True) # True Condition for or
print(False or True)
print(True or False)


# In[54]:


x = 1   # Here = is assignment operator
print(x)
2 == 1 # Here == is comparison operation


# In[61]:


# not is opposite 

not 5 == 5


# ### Lesson 5 : If Else, Elif Else, Truthy Concept
# 
# * An if statement can be used to conditionally execute code, depending on whether the "if" statement's condition is True or False.
# * An elif (that is, "else if") statement can follow an if statement. Its block executes if its condition is True and all the previous conditions have been False.
# * An else statement comes at the end. Its block is executed if all of the previous conditions have been False.
# * The values 0 (integer), 0.0 (float), and ‘‘ (the empty string) are considered to be "falsey" values. When used in conditions they are considered False. You can always see for yourself which values are truthy or falsey by passing them to the bool() function.

# In[96]:


#if else Program - True or False

password = 'ucan'

'Hi, please enter password'

yourpassword = input()

if yourpassword == password:
    print('Access Granted')
else:
    print('Blocked')


# In[83]:


#if elif else Program - Provides the first True Result (Order Matters)

password = 'ucan'

'Hi, please enter password'

yourpassword = input()

if yourpassword == password:
    print('Access Granted')
elif yourpassword == 'uca':
    print('Almost there')
else:
    print('Blocked') 


# The concepts of truthy and falsy are fundamental for control flow and decision-making within programs
# 
# **Truthy Values**
# 
# * Any non-zero numeric value (e.g., 1, 2.5, -3.14).
# * Non-empty sequences or collections (e.g., lists, tuples, sets, dictionaries).
# * Non-empty strings (e.g., 'hello').
# * Any object that is not explicitly defined as falsey.
# 
# **Falsy Values**
# 
# * The numerical value 0 (integer or float).
# * Empty sequences or collections (e.g., [], (), {}, '').
# * The special value None.
# * Boolean value False itself.

# In[100]:


# Truthy and Falsy Concept

print(bool(0))  # Falsy
print(bool(101))   # Truthy   

print(bool(""))  # Falsy
print(bool("abc"))  # Truthy


# ### Lesson 6 : While Loops
# 
# *while loop is a control flow statement which excutes the code in loop till the condition is True*
# 
# * While loop is usually condition based
# * You can press ctrl-c to interrupt an infinite loop. This hotkey stops Python programs.
# * A "break" statement causes the execution to immediately leave the loop, without re-check the condition.
# * A "continue" statement causes the execution to immediate jump back to the start of the loop and re-check the condition.

# In[2]:


#Simple While Loop
x = 0
while x<=10:
    print(x)
    x+=1


# In[23]:


# Break

x = 0
while True:
    x += 1
    print(x)
    if x == 10:
        break


# In[28]:


# Continue
x = 0
while x <= 5:
    x+=1
    if x == 3: # 3 is skipped out of loop
        continue
    print(x)


# ### Lesson 7 : For Loop
# 
# *For loop is a control flow statement which excutes the code in loop for fixed number of times*
# 
# * A for loop will loop a specific number of times.
# * The range() function can be called with one, two, or three arguments.
# * The break and continue statements can be used in for loops just like they're used in while loops.

# In[34]:


# for loop 

for i in range(1,10,2):
    print(i)


# ## III. Functions

# ### Lesson 8 : Python Built in Functions
# 
# * You can import modules and get access to new functions.
# * The modules that come with Python are called the standard library, but you can also install third-party modules using the pip tool.
# * The sys.exit() function will immediately quit your program.

# In[56]:


# Importing modules

# ! pip install pandas -- for installing modules

import math
import pandas
import sys
import os
import warnings
warnings.filterwarnings("ignore")


# In[53]:


# sys.exit()

print(5)
sys.exit() # Execution stops
print(7)


# ### Lesson 9 : Writing your own Functions
# 
# * Functions are like a mini-program inside your program.
# * The main point of functions is to get rid of duplicate code.
# * The def statement defines a function.
# * The input to functions are called arguments. The output is called the return value.
# * The parameters are the variables in between the function's parentheses in the def statement.
# * The return value is specified using the return statement.
# * Every function has a return value. If your function doesn't have a return statement, the default return value is None. (Like True and False, None is written with a capital first letter.)
# * Keyword arguments to functions are usually for optional arguments. The print() function has keyword arguments "end" and "sep".

# In[76]:


# Self Defined Function

def salary_increment(x):  #Here x is a parameter not an argument
    return 'your revised salary is', x * 1.15
    
salary_increment(2000)


# In[83]:


# Type Conversion 

'hi ' + str(5)


# In[86]:


# args and kwargs i.e., arguments and keyword arguments

print(10, end= ', ')  #Kwargs are optional
print(20)


# ### Lesson 10 : Global and Local Scopes
# 
# * A scope can be thought of as a container of variables.
# * The global scope is code outside of all functions. Variables assigned here are global variables.
# * Each function's code is in its own local scope. Variables assigned here are local variables.
# * Code in the global scope cannot use any local variables.
# * Code in a function's local scope cannot use variables in any another function's local scope. While global can be used.
# * If there's an assignment statement for a variable in a function, that is a local variable. The exception is if there's a global statement for that variable; then it's a global variable.

# In[109]:


# Global Variable
x = 10 

# Local Variable
def tajamul():
    x = 5
    print(x)


# In[106]:


# using global variable inside function 

x = 100

def ik(): # Here no Assignment operator, so global variable
    print(x)

ik() 


# In[102]:


# Local variable is created by Assignment Operation

def ik():
    egg = 10 # Here Assignment operator changes x to Local
    print(egg)

ik() 


# In[107]:


# Changing local variable to global inside function

x = 10
def ty():
    global tj  #changed to global scope
    tj = 100
    print(tj)


# ## IV. Exception Handling

# ### Lesson 11 : Try and Except Statements
# 
# * A divide-by-zero error happens when Python divides a number by zero.
# * Errors cause the program to crash. (This doesn't damage your computer at all. It's just that the computer doesn't know how to carry out this instruction, so it immediately stops the program by "crashing" rather than continue.)
# * An error that happens inside a try block will cause code in the except block to execute. That code can handle the error or display a message to the user so that the program can keep going.
# * The try and except blocks should handle the exception when calling the function, not when defining it.

# In[115]:


# Dividing number by zero gives error

def divider(x):
    return 42/x

divider(0)


# In[142]:


# Try and Except Method -- ZeroDivisionError

def divider(x):
    try:
        return 42/x
    except ZeroDivisionError:
        print('Dont divide by zero')
            
print(divider(2))
print(divider(0))


# In[141]:


# Cat Counter -- ValueError

try:
    x = int(input('How many cats do you have? '))
    if x <= 4:
        print('less cats')
    else:
        print('more cats')
except ValueError:
    print('Enter Numbers only')


# ## V. Guess the Number Game

# In[ ]:


import random

x = input('Hello, what is your name? ')
print('so, ' +  x + ', I am thinking of a number between 1 and 10')

secret_number = random.randint(1,10)

for i in range(1,7):
    print('take a guess')
    
    guess = int(input())
    if guess < secret_number:
        print('Too Low')
    elif guess > secret_number:
        print('Too High')
    else:
        break
        
if guess == secret_number:
    print('good job, It took you ' + str(i) + ' guesses to guess my number')
else:
    print('Exceeded guess limits, My guess number was ' + str(secret_number))


# ## VI. List
# 
# *a list is a built-in data structure that represents an ordered collection of elements i.e., [1,2,3] != [3,2,1]
# and is mutable.*

# ### Lesson 13: List Basics
# 
# * A list is a value that contains multiple values: [42, 3.14, ‘hello']
# * The values in a list are called items.
# * You can access items in a list with its integer index.
# * The indexes start at 0, not 1.
# * You can also use negative indexes: -1 refers to the last item, -2 refers to the second to last item, and so on.
# * You can get multiple items from the list using a slice.
# * The slice has two indexes. 
# * The new list's items start at the first index and go up to, but doesn't include, the second index.
# * The len() function, concatenation, and replication work the same way on lists that they do with strings.
# * You can convert a value into a list by passing it to the list() function.

# **Indexing**

# In[14]:


# Basic Indexing

x = ['a','b','c']
x[0]


# In[15]:


# Nested List Indexing

y = [['n','c'], 'a', 'b']


# In[17]:


y[0][1]


# In[18]:


# Negative Indexing

x = ['a','b','c']
x[-1]


# **Slicing**

# In[30]:


# Basic Slicing

x = ['a','b','c']

x[0:2] #(n,n-1) concept


# In[29]:


#Negative Slicing

x = ['a','b','c']

x[-3::]


# **Mutability of Lists**

# In[35]:


x = ['a','b','c']
x[2:] = [1,2]
x


# **List Functions**

# In[60]:


fruits = ['apple','banana','grapes']


# In[61]:


len(fruits)  #len


# In[64]:


del fruits[2]   #del
fruits


# In[71]:


bind = [1,2,3,4] + [5,6,7,8]  #concatenate
bind


# In[75]:


x = ['a', 'b', 'c', 'd', 'e']  #Membership

print('a' in x)
print('a' not in x)


# In[82]:


x = (1,2,3)  #List conversion
list(x)


# ### Lesson 14: For Loops with Lists, Multiple Assignment and Augmented Operators
# 
# * A for loop technically iterates over the values in a list.
# * The range() function returns a list-like value, which can be passed to the list() function if you need an actual list value.
# * Variables can swap their values using multiple assignment: a, b = b, a
# * Augmented assignment operators like += are used as shortcuts.

# In[83]:


# The range() function returns a list-like value, which can be passed to the list() function.
for i in [0,1,2,3]:
    print(i)


# In[91]:


# Conversion of Range to List
list(range(0,10,2))


# **For loop for List with strings**

# In[100]:


# How to use for loop for list containing String elements?
animals = ["Bat", "cat", "Rat", "Dog"]

for i in range(len(animals)):
    print(i, animals[i]) #index and value


# **Multiple Assignment**

# In[103]:


Dog = ['Slim', 'Black', 'Loud']


# In[106]:


Size, Color, Bark = Dog  # Multiple Assignment


# In[105]:


Size


# In[107]:


Color


# In[108]:


Bark


# **Swapping Values in Variables**

# In[117]:


a = 'cat'
b = 'rat'


# In[118]:


a, b = b, a #Swapping Values


# In[119]:


a


# In[120]:


b


# **Augmented Assignment Operator**

# In[122]:


x = 2 + 1
x


# In[126]:


y = 1
y += 3  # Assignment Operator
y


# ### Lesson 15: List Methods
# *Methods are functions that are "called on" values.*
# 
# Return values are not used for methods like x = x.append('z')
# 
# * The index() list method returns the index of an item in the list.
# * The append() list method adds a value to the end of a list.
# * The insert() list method adds a value anywhere inside a list.
# * The remove() list method removes an item, specified by the value, from a list.
# * The sort() list method sorts the items in a list.
# * The sort() method's reverse=True keyword argument can make the sort() method sort in reverse order.
# * The sort() cant be used on list with multiple data types - important
# * These list methods operate on the list "in place", rather than returning a new list value.

# **Functions vs Methods**

# In[156]:


print(len('Hello'))  #Function

x = ['Hello', 'Hey', 'Hi']

x.index('Hello')  #Method because it is called on Value


# In[157]:


fruits = ['apple','banana','grapes']

fruits.append('orange')  #append
fruits


# In[158]:


fruits.pop()   #pop
fruits


# In[159]:


fruits.insert(1, 'Mango')  #insert (Index, New Value)
fruits


# In[160]:


fruits.remove('apple')  #remove
fruits


# In[165]:


number = [5, 2.5, 7.15, 7, 9, 8.15] #Sorting Numbers in Asc
number.sort()
number


# In[169]:


animals = ['monkeys', 'dogs', 'zebra', 'cat'] #Sorting Strings alphabetically
animals.sort()
animals


# In[170]:


number = [5, 2.5, 7.15, 7, 9, 8.15] #Sorting Numbers in Desc
number.sort(reverse = True)
number


# In[171]:


#The sort() cant be used on list with multiple data types - important

x = ['monkeys', 'dogs', 1 , 0]
x.sort()


# **Alphabetical vs ASCII - betical Order (AKA askey)** 
# 
# *This mean elements with capital letter will be given preference*

# In[187]:


x = ['andy', 'Andrew', 'Bob', 'bob']  #Capital will be given preference
x.sort()
x


# In[179]:


# In order to solve above problem

x = ['andy', 'Andrew', 'Bob', 'bob']  
x.sort(key = str.lower)  #Get Elements in True Form
x


# ### Lesson 16: Similarities between List and String
# *Lists are Mutable while strings are not*
# 
# * Strings can do a lot of the same things lists can do, but strings are immutable.
# * Immutable values like strings and tuples cannot be modified "in place".
# * Mutable values like lists can be modified in place.
# * Variables don't contain lists, they contain references to lists.
# * When passing a list argument to a function, you are actually passing a list reference.
# * Changes made to a list in a function will affect the list outside the function.
# * The \ line continuation character can be used to stretch Python instruction across multiple lines.

# In[193]:


# String does not support Mutability

x = 'I am a Data Analyst'
x[0] = 'U'


# In[198]:


# List Supports Mutability

x = list(range(0,10,2))
print(x)
x[0] = 10
x


# **References**

# In[202]:


A = 20
B = A
A += 2

print(A)
print(B) #B is not updated because it is not referenced


# In[224]:


# Variables contain references to lists because lists are saved as Reference IDs to save space, 
# lets say we have thousands of value in list, then it will only be referenced by ID hence saving space

spam = [1,2,3,4,5]
cheese = spam

spam[0] = 22

print(xmas)
print(bat)  #both getting updated


# ![image.png](attachment:image.png)
# 

# **Line Continuation Character**

# In[222]:


print('Automate Boring Stuff with Python \
you can literally enjoy and relax')


# ## VII. Dictionaries
# 
# *A dictionary in Python is an unordered, mutable, and indexed collection of key-value pairs. Each key is unique and is used to access the corresponding value in the dictionary. Dictionaries are highly efficient for lookups, insertion, and deletion of key-value pairs.*

# ### Lesson 17: The Dictionary Data Type
# 
# **Keys:** *Must be immutable and unique. Examples include integers, strings, and tuples.*
# 
# **Values:** *Can be mutable or immutable. Examples include integers, strings, lists, and dictionaries.*
# 
# 
# * Dictionaries contain key-value pairs. Keys are like a list's indexes.
# * Dictionaries are mutable. 
# * Variables hold references to dictionary values, not the dictionary value itself.
# * Dictionaries are unordered. There is no "first" key-value pair in a dictionary.
# * The keys(), values(), and items() methods will return list-like values of a dictionary's keys, vaues, and both keys and values, respectively.
# * The get() method can return a default value if a key doesn't exist.
# * The setdefault() method can set a value if a key doesn't exist.
# * The pprint module's pprint() "pretty print" function can display a dictionary value cleanly. 
# * The pformat() function returns a string value of this output.

# In[234]:


#Key value pair
mycat = {'size' : 'fat', 'color' : 'orange' , 'age': [3,4]}


# In[231]:


mycat['size']


# In[233]:


mycat['age'][1]


# In[240]:


#Dictionaries are unordered unlike lists

print([1,2,3] == [3,2,1]) #False, because list is ordered

print({'size' : 'fat', 'color' : 'orange'} == {'color' : 'orange', 'size' : 'fat'}) #True (Unordered)


# In[245]:


#check if key exists or not in Dict (in and not in)

dict = {'size' : 'fat', 'color' : 'orange'}

print('size' in dict) #only for keys
print('fat' in dict)   #not for values


# In[247]:


# Conversion of Dict into list

#Keys
print(list(dict.keys()))

#Values
print(list(dict.values()))

#Items
print(list(dict.items()))


# In[265]:


# Unpacking with for loop

dict = {'size' : 'fat', 'color' : 'orange'}

for i in dict.keys():
    print(i)

for i in dict.values():
    print(i)
    
for i in dict.items():  #Returns tuples
    print(i)
    
for a,b in dict.items():
    print(a, b)


# In[269]:


# Checking Membership

dict = {'size' : 'fat', 'color' : 'orange'}

'fat' in dict.values()

'size' in dict.keys()

if 'size' in dict.keys():
    print(dict.values())


# **get Method**

# In[272]:


category = {'size' : 'fat', 'color' : 'orange', 'age' : 8}


# In[276]:


category.get('speed', 0) #returns 0 if not found


# **setdefault**

# In[278]:


category.setdefault('size', 'thin') #if value for size is missing then 'thin' will be default


# **Count Repitition of Letters in String**

# In[289]:


m = 'a big fat hen'

count = {}

for character in m.upper():
    count.setdefault(character, 0)
    count[character] += 1

count


# **pprint function**
# 
# *Pretty print function*
# The pprint module's pprint() "pretty print" function can display a dictionary value cleanly

# In[294]:


import pprint

m = 'a big fat hen'

count = {}

for character in m.upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)


# **pprint format**
# 
# *The pformat() function returns a string value of this output.*

# In[302]:


m = 'a big fat hen'

count = {}

for character in m.upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pformat(count)


# ### Lesson 18: Data Structures

# In[349]:


#Tic Tac Toe Game

theboard = {
'top-L' : 'O',
'top-M' : 'X',
'top-R' : 'O',
'mid-L' : 'O',
'mid-M' : 'X',
'mid-R' : 'X',
'low-L' : 'X',
'low-M' : 'O',
'low-R' : 'O'
}


# In[350]:


def printboard(x):
    print(x['top-L'] + '|' + x['top-M'] + '|' + x['top-R'])
    print('-----')
    print(x['mid-L'] + '|' + x['mid-M'] + '|' + x['mid-R'])
    print('-----')
    print(x['low-L'] + '|' + x['low-M'] + '|' + x['low-R'])


# In[351]:


printboard(theboard)


# **type Function**

# In[348]:


print(type(6))
print(type('ab'))
print(type(1.2))
print(type(2j))
print(type(True))


# ## VIII. More about Strings

# ### Lesson 19: Advanced String Syntax
# 
# * Strings are enclosed by a pair of single quotes or double quotes (as long as the same kind are used).
# * Escape characters let you put quotes and other characters that are hard to type inside strings.
# * Raw strings (which have the r prefix before the first quote) will literally print any backslashes in the string and ignore escape characters.
# * Multiline strings begin and end with three quotes, and can span multiple lines.
# * Indexes, slices, and the "in" and "not in" operators all work with strings.

# In[355]:


#escape character

'that is alice\'s cat'


# ![image.png](attachment:image.png)

# In[360]:


# new line

print('Hey\nHow are you\nHow is everything going')


# **raw string**

# In[363]:


# raw string helps us literally print even escape characters

print(r'Hey\nHow are you\nHow is everything going') #raw character


# **multiple line string**

# In[367]:


print("""This is useful for really 
really
large string""")


# **Similarities between lists and strings**

# In[381]:


spam = 'Hello world'

spam[0] #same indexing
spam[0:6] #same slicing
'Hello' in spam #Membership also works


# ### Lesson 20: String Methods
# 
# * upper() and lower() return an uppercase or lowercase string.
# * isupper(), islower(), isalpha(), isalnum(), isdecimal(), isspace(), istitle() returns True or False if the string is that uppercase, lowercase, alphabetical letters, and so on.
# * startswith() and endswith() also return bools.
# * ‘,'.join([‘cat', ‘dog']) returns a string that combines the strings in the given list.
# * ‘Hello world'.split() returns a list of strings split from the string it's called on.
# * rjust() ,ljust(), center() returns a string padded with spaces.
# * strip(), rstrip(), lstrip() returns a string with whitespace stripped off the sides.
# * replace() will replace all occurrences of the first string argument with the second string argument.

# In[388]:


x = 'Hello world'

print(x.upper())
print(x.lower())


# In[399]:


# Solving Case of input

x = input('do you wana code? ')

if x.lower() == 'yes':
    print('Thanks for help!')


# In[402]:


# isupper

x = 'Hello world'
x.isupper()


# In[406]:


# isalpha means is alphabetical : to check if any integers are in string

x = 'Helloworld'
x.isalpha()


# In[408]:


# isalnum means is alphanumerical

x = 'Helloworld12'
x.isalnum()


# In[418]:


# isspace : To find space in strings

x = ' '
x.isspace()


# In[423]:


# Start with , End with

print('Helloword'.startswith('H'))
print('Helloword'.endswith('d'))


# In[440]:


# Join String

print('ing '.join(['sleep', 'eat', 'beat']))

print('\n\n'.join(['sleep', 'eat', 'beat']))


# In[443]:


# Split String

'There is a data, trick'.split(',')


# In[ ]:


# Strip String

x = ' There '
print(x.strip())

# lstrip = left strip

y = ' There '
print(y.lstrip())

# rstrip = right strip

z = ' There '
print(z.rstrip())


# In[454]:


# Replace String

x = 'Hello There'

x.replace('Hello', 'Hey')


# ### Lesson 21: String Formatting

# In[460]:


name = 'Tajamul'
address = 'Main colony'

f' I think I know u, Are u {name} from {address}'

