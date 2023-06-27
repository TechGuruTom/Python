# unordered
# unchangable
# unique
# can be created with immutable data types
# a set contains int,float,boolean,str,tuple, frosen set,Bytes
# should not contain mutable data types
# should not have list,set, dict,array, bytearray


# creating a set
# using {}
a = {1,2,3,'tom'}
# using set() constructor
a = set((1,2,3,4))
# a set with mutable data gives error (TypeError)
# invalid_set = {1,2,3,[1,2,3,4]}

# when creating empty set use set() constructor, if we use {} then by default it considered as dict.



# accessing items in set
valid_set = {1,2,3,4,5,6}
for item in valid_set:
	print(item) 

# check an item in set
if 1 in valid_set:
	print('item exists')


# finding the length
print(len(valid_set))

# adding an item to set
# add() - use this to add single item
a.add(6)
# update()
a.update([8,9,10])

# removing items
# remove() - throw error if item not exists
a.remove(9)
# discard() - not throw error if item not exists
a.discard(9)
# pop() - returns removed item
popped_item = a.pop()
# clear() - will clear entire set
a.clear()
# del - deletes the entire set
del a


# set operations
# union --> | --> all items in the both set, all items exists only once/remove duplicates
a = {1,2,3,4}
b = {2,3,4,5,6,7,8}

print(f"after union in set {a|b}") #after union in set {1, 2, 3, 4, 5, 6, 7, 8}


# intersection --> & --> return common items from both sets
print(f"after intersection in set {a&b}") #after intersection in set {2, 3, 4}

# difference --> - --> a-b , remove a's item which exists in b
print(f"after difference in set {a-b}") #after difference in set {1}
print(f"after difference in set {b-a}") #after difference in set {8, 5, 6, 7}
# symmentric_difference --> ^ --> remove common items and return a,b values
print(f"after symmetric difference in set {a^b}") #after symmetric difference in set {1, 5, 6, 7, 8}


# intersection vs intersection update
# difference vs difference_update


# copying a set

# subset, superset, disjoint
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# all items of A are present in B
print(A.issubset(B))
print(B.issuperset(A))
print(A.isdisjoint(B))
