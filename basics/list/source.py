# creating a python list
# using list() constructor
a = list((1,2,3,4))
print(f"list using constructor method {a}")

# using square brackets
b = [6,7,8,9]
print(f"list creating using square bracket method {b}")


# lenth of list
print(f"length of the list a is {len(a)}")


# accessing items in list
# using index method can access only one item 
print(a[0]) #positive index
print(a[-1]) #negative index

# using slices - can access more that one item
# a[start:stop:step]
# forward
print(a[:])
print(a[1:])
print(a[:5])
# forward negative index
print(a[:-5])
# ...more


# reverse slicing
print(a[::-1]) #print all items in a list in reverse order
print(a[-1:-10:-1]) #print index -1 to till -10 in reverse order

# iterating a list
fruits = ['apple', 'banana', 'kiwi', 'orange']
for fruit in fruits:
	print(fruit)

# iterate with index number
for index, fruit in enumerate(fruits):
	print(f"{index} --> {fruit}")

# iterate using len()
# can get index also
for i in range(0, len(fruits)):
	print(f"with index: {i} --> {fruits[i]}")

# adding elements to list
# append()
# insert()
# extend()
b = [1,2]
print(b.append(3)) #add 3 as last item in list
print(b.insert(0, 10)) #add value 10 as first item in the list
print(b.extend([5,6])) #extend the origional list, add values at last

# using + and * operators
a = [1,2,3,4,5]
b = a + [6,7,8,9]
print(b) #[1,2,3,4,5,6,7,8,9]

# using * 
a = [None]
a = a*3 
print(a) #[None,None,None]




# modify items 
# individual
c = [1,2,3,4]
c[1] = 10
print(c)
# range of items
c[2:3] = [10,20,30]
print(c)
c[2:] = [2,3,4]
print(c)


# modify all items
# in origional list
a = [1,2,3,4]
for i in range(len(a)):
	a[i]=a[i]*a[i]

print(a)

# use map function
# but it will not modify origional list
def square(a):
	return a*a

b = [2,4,6,8]
print(list(map(square, b))) # map will return map object so convert it to list
print(b) #as same as [2,4,6,8]


# removing elements
# remove(item)
# pop(index)
# clear()
# del list_name (fully or partially)

a = [10,20,30,40]
a.remove(10) #will remove first match
a.pop() #by default remove last indexed item
a.pop(0) #will remove first item
a.clear() #delete all item from list and return empty list

# remove partially
b = [1,2,3]
del b[1:] 
del b[:2]
del b[1:3]


# finding a element in list
# return error if item not exists
a.index(1)

# concatination of list
# using + operator
a = [1,2]
b = [3,4]
c = a+b

# extend will add list of items to another list
a.extend(b)


# copying a list
# = operator
# changes in new list still affect old list
a = [1,2,3]
b=a
a.append(4)
# b is also [1,2,3,4]

# copy()
# returns a shallow copy of the list
a = [1,2,3,4]
c = a.copy()

# copy by array slicing
# it's also shallow copy
a = [1,2,3,4,5,6,7]
b = a[1:3]

# deepcopy()
from copy import deepcopy
a = [1,2,3,4,[1,2,3,4]]
d = deepcopy(a)

# list operations:

# sort
# modifies origional list
a = [2,3,4,5,3,5,6]
a.sort()

# reverse
# modifies origional list
a = [1,2,3,34,4,5,6,76,7,8]
a.reverse()


# python build-in functions with list
# min and max
a = [1,2,3,4,5,6,76,32]
print(max(a))
print(min(a))

# sum
print(sum(a))

# all and any
# returns true if all elements return true
print(all([1,1,1,1,1,23]))
# returns true if any one is true
print(any([1,1,1,1,1,23]))

# join
# join list of elements if list contains strings
a = ['join', 'rose', 'alex']
'-'.join(a)


# list comphrehension
a = [1,1,2,32,3,[1,2,3,4]]