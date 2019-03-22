"""
Python Collections (Arrays)
"""
#list is same as array
mylist = ["apple", "ball", "cherry"]
print(mylist[1])

#looping
for x in mylist:
    print(x)

#checking item in array
if "ball" in mylist:
    print ("Yes, ball exists in list")

#length
print(len(mylist))

#adding items to list
mylist.append("orange")
mylist.insert(1, "banana")
print(mylist)

#remove
mylist.remove("orange")
print(mylist)
mylist.pop() #or use pop(2) any number to remove that item
print(mylist)
del mylist[0]

#delete list completely
# del mylist
# mylist.clear()



"""
Tuples
like list but unchangeable, small brackets are used ()
"""
my_tuple = ("apple", "ball", "cherry")

"""
Set
like list and is unordered and unindexed, curly brackets {}
"""
my_set = {"apple", "banana", "cherry"}

"""
Dictionary
"""
my_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(my_dict)
print(my_dict["model"])
print(my_dict.get("model"))

#printing keys
for x in my_dict:
    print(x)
for x in my_dict:
    print(my_dict[x])
for x in my_dict.values():
    print(x)
for x,y in my_dict.items():
    print(x,y)

if "model" in my_dict:
  print("Yes, 'model' is one of the keys in the my_dict dictionary")


#removing item from dictionary
my_dict.popitem()
print(my_dict)

my_dict.clear()
