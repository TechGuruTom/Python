# join list of items except last element
a = [1,2,3,4,5]
print('\n'.join(map(str,a)))

# reverse a string
# slice method will not modify origional list
print(a[::-1])

# reverse method will modify origional list
a.reverse()
print(a)


# check two lists are exactly equal
import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

compare([1,2,3], [1,2,3,3])
compare([1,2,3], [1,2,3])
compare([1,2,3,3], [1,2,2,3])

# check a list have same elements
# ex [1,1,1,1,1]

# using set and len
a = [1,1,1,1,1,1,1]
print(len(set(a)) ==1)

# count method
a.count(a[0]) == len(a)

# using *
[a[0]]*len(a) == a

# find unique and difference in list