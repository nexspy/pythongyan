"""
Just a beginning of python world
Very easy language
"""
msg = "hello world"
print(msg)


"""
Numbers
"""
x = 5
x = int(3.4) #converts to 3
y = 2

#11 must be bigger than 2 to print this :D
if (x>y):
    print ("x is bigger than y")


"""
Strings
"""
fname = "Nirmal"
lname = "Limbu"
print(fname + " " + lname)
#convert number to string
num = str(2) #gives '2'
print(type(num))
#getting substring 
a = "Hello, World!"
print(a[1])
print(a[0:5])
#remove whitespace from start
a = " Hello World"
print(a.strip())
#getting length
print(len(a))
"""
Other functions
.lower()
.upper()
.replace("H", "J")
.split(",") -> this is like explode
"""

#getting input from command line
# x = input()
# print("hello", x)


"""
Operators
some new operators are using
and for &&
also similary we have
and, or, not
.............. not is used as :  not(x and y)
x is y
y is not y
x in y
x not in y
"""
x = 1
y = 1
if (x and y):
    print("ok man")


