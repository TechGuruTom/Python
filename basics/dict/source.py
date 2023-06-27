# stores a mapping between a key and value

# till python3.6 dict is unordered
# from python3.7 dict is ordered
# keys are unique 
# mutable 


# creating dict
# using curly braces - {}
# using dict()
# using sequences each item as a pair


# empty dict
dict = {}

# accessing elements in dict
dict = {
	'name': 'tom',
	'age': 23
}


# using square brackets
print(dict['name'])

# using get method
# pass second params as a default value
# if key not found in dict then it returns the default value
print(dict.get('age', 'pass default value here'))


# get all keys, values, items
dict.keys()
dict.values()
dict.items()


#iterating a dict
for item in dict:
	print(dict[item])

for entry in dict.items():
	print(entry[0], entry[1])


# find length of dict
print(len(dict))


# adding item to dict
# using key
dict['contact_no'] = '234567876'

# using update method
# if key not exists in that dict then it will add that as a new item in the dict.
dict.update({'contact_no': 67898765678})


# set default value to a key
# set default value if key doesn't exists
# key doesn't exists and value not mentioned. default None
# key exists and value mentioned. doesn't  change value
dict.setdefault('key', 'value')

# Removing items from the dictionary
dict = {'name': 'tom', 'age':24, 'gender': 'male'}
# dict.popitem() - removes last pair and return as tuple - if not exist will raise key error
# dict.pop(key) - removes the item by using key - returns the value - if not exist will raise key error
# del dict['key'] - delete a particular item by key
# dict.clear() - removes all items from dict.
# del dict - delete the whole dictionary

# Checking if a key exists
# use keys() and in operator to check the key exists.
print('name' in dict.keys())

# Join two dictionary
# using update method
# using ** operator

dict1 = {
	'name': 'tom',
	'age': 36
}
dict2 = {
	'lang': 'en',
	'country': 'IN'
}
# using update method
dict1.update(dict2)

# using ** operator
new_dict = {**dict1, **dict2}


# copying dict
# using copy()
# using dict() constructor method
# using = operator

# using copy()
dict_1 = dict1.copy()

# using dict() 
dict_2 = dict(dict2)

# using = operator
dict3 = dict2 # both object refers same object will changes


# sorting dict
# sorted() function used to sort the dict
# by default it sort dict by keys
# if needed can sort it by values

a = {
    'name': 'tom',
    'age': 22
}

sorted(a) #sort by key by default
sorted(a.keys()) #sort by keys
sorted(a.values()) #sort by values


# sort ascending 
sorted_dict = {key : a[key] for key in sorted(a)}

# sort desending
sorted_dict = {key : a[key] for key in sorted(a)[::-1]}


# min and max
# used with keys only
dict = {1:'aaa',2:'bbb',3:'AAA'}
print('Maximum Key',max(dict)) # 3
print('Minimum Key',min(dict)) # 1

# all and any
# used with keys only

# all
# When the built-in function all() is used with the dictionary the return value will be true in the case of all – true keys and false in case one of the keys is false.

# Few things to note here are

# Only key values should be true
# The key values can be either True or 1 or ‘0’
# 0 and False in Key will return false
# An empty dictionary will return true.

#dictionary with both 'true' keys
dict1 = {1:'True',1:'False'}

#dictionary with one false key
dict2 = {0:'True',1:'False'}

#empty dictionary
dict3= {}

#'0' is true actually
dict4 = {'0':False}

print('All True Keys::',all(dict1))
print('One False Key',all(dict2))
print('Empty Dictionary',all(dict3))
print('With 0 in single quotes',all(dict4))

# o/p
# All True Keys:: True
# One False Key False
# Empty Dictionary True
# With 0 in single quotes True


# any
# any() function will return true if dictionary keys contain anyone false which could be 0 or false. Let us see what any() method will return for the above cases.

#dictionary with both 'true' keys
dict1 = {1:'True',1:'False'}

#dictionary with one false key
dict2 = {0:'True',1:'False'}

#empty dictionary
dict3= {}

#'0' is true actually
dict4 = {'0':False}

#all false
dict5 = {0:False}

print('All True Keys::',any(dict1))
print('One False Key ::',any(dict2))
print('Empty Dictionary ::',any(dict3))
print('With 0 in single quotes ::',any(dict4))
print('all false :: ',any(dict5))

# o/p
# All True Keys:: True
# One False Key :: True
# Empty Dictionary :: False
# With 0 in single quotes :: True
# all false ::  False