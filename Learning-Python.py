print("Hello World!")

# exit()

if 5 > 2:
  print("Five is greater than two!")

x=2
y="dog"
z=str(3)
w=int(3)
v=float(3)

"""
Multi-line comment
1
2
3
"""

print(x)
print(y)
print(z)
print(w)
print(v)

print(type(x))
print(type(z))
print(type(v))

a, b, c = 1, 2, 4
e = f = g = 10
print(a, b, c, e, f, g)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# globals:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# objects

x = dict(name="Seth", age=24)

# Python uses standard operators but also has a floor divion function using double forward slash //
x=101//25
print(x)
# x=4 in this case

# Python has "and", "or", and "not" operators
# Python also has identity operators "is" and "is not", which check if the two arguments are in the same memory
# Python also has membership operators "in" and "not in" which check if a sequence is presented in an object
# There are also bitwise operators, but those are not that necessary for now

# Onto lists now!
# Lists are ordered and changeable

myList = [1, 2, 3]
strList = ["a", "b", "c"]
# len(myList) = 3; len returns the length
newList = list((1, 2, "three"))
# the list(()) constructor is an alternative way to make a list

# Lists have a 0 based index and can also be accessed from the end with negatives
# Ranges also work
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# Leaving the value prior to the colon empty defaults to 0. Leaving the value after the colon empty defaults to (len-1)
# Accesing by range is non-inclusive for the second argument of the range

# We can use the "in" operator with lists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# We can change items in a list by accessing them by index. This can be done with ranges too
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Replacing a range with fewer parameters than elements will insert the values and shorten the list as needed

# Inserting can also be done with an insert method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
# watermelon is in between banana and cherry now

# append method can be used to add one item to the end of the list
# extend method can be used to concatenate lists

thislist = [1, 2]
thatlist = ["a", "b"]

bothlist = thislist.extend(thatlist)
# bothlist = [1, 2, "a", "b"]
# extend can also be used on a list and will overwrite the list with the extended

#extend also works with other data structures
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
# the tuple is added to the list as two new elements

# list.remove("element") removes elements by content. list.pop(#) removes elements by index
# list.pop() defaults to the final element
# del list[#] also removes elements by index
# del list deletes the entire list
# list.clear clears the list, but the list remains in memory, empty

# sorting lists

# Lists can be sorted with list.sort() which defaults to alphanumeric sorting. list.sort(reverse = true) is reversed sorting.
# list.reverse() reverses the list order
# you can also create custom sorting functions and use list.sort(key = func) to do this

# We can copy lists 2 ways
newlist = thislist.copy()
newlist = list(thislist)

# lists can be concatenated with + operators
list1 = [1, 2, 3]
list2 = [4, 5]
bothlist = list1 + list2

# we can count the number of items in an array of a certain value with count

thislist= ["a", "a", "b", "c"]
# thislist.count("a") returns 2


