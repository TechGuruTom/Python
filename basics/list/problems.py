# Check if a list contains an element - using in operator
# How to iterate over 2+ lists at the same time
# When would you use a list vs dictionary?
# While both lists and dictionaries are ordered as of python 3.7, a list allows duplicate values while a dictionary doesn’t allow duplicate keys.
# Is a list mutable?
# What is the difference between append and extend?

# Do python lists store values or pointers?
# Python lists don’t store values themselves. They store pointers to values stored elsewhere in memory. This allows lists to be mutable.

# What does “del” do?
# del removes an item from a list given its index.

# What is the difference between “remove” and “pop”?
# Remove duplicates from a list
# Find the index of the 1st matching element
# Remove all elements from a list
# Iterate over both the values in a list and their indices
# How to concatenate two lists
# How to manipulate every element in a list with list comprehension
# Count the occurrence of a specific object in a list
# How to shallow copy a list?
# Why create a shallow copy of a list?
# How to deep copy a list?
# What is the difference between a deep copy and a shallow copy?

# What is the difference between a list and a tuple.
# Return the length of a list
# What is the difference between a list and a set?
# How to check if an element is not in a list?
# Multiply every element in a list by 5 with the map function
# Combine 2 lists into a list of tuples with the zip function - o/p list of tuples
# Insert a value at a specific index in an existing list
# Subtract values in a list from the first element with the reduce function
# Remove negative values from a list with the filter function - filter return element if its true
# Convert a list into a dictionary where list elements are keys


# Modify an existing list with a lambda function
# Remove elements in a list after a specific index - use slicing
# Remove elements in a list before a specific index
# Remove elements in a list between 2 indices
# Return every 2nd element in a list between 2 indices
# Sort a list of integers in ascending order
# Sort a list of integers in descending order
# Filter even values out of a list with list comprehension
# Count occurrences of each value in a list - use collections module
# Get the first element from each nested list in a 


# What is the time complexity of insert, find and delete for a list?
# Insert is O(n). If an element is inserted at the beginning, all other elements must be shifted right.
# Find by index is O(1). But find by value is O(n) because elements need to be iterated over until the value is found.
# Delete is O(n). If an element is deleted at the beginning, all other elements must to be shifted left.

# What kind of copy would the list constructor create from an existing list?
# The list constructor creates a shallow copy of a passed in list. That said, this is less pythonic than using .copy()

# Combine elements in a list into a single string.
# What’s the affect of multiplying a list by an integer? just like n times loop 
# Can you sort a list with “None” in it? - no, bcoz it uses comparision operator
# Reverse the order of a list
# What is the difference between reverse and reversed?
# What is the difference between sort and sorted?
#  Return the minimum value in a list
# Return the maximum value in a list
# Return the sum of values in a list
# Use a list as a stack - append/pop ==> LIFO 

# Find the intersection of 2 lists
# Find the difference between a set and another set
# Flatten a list of lists with a list comprehensions
# Generate a list of every integer between 2 values
# Combine 2 lists into a dictionary - dict(zip(a,b))
# Reverse the order of a list using the slice syntax