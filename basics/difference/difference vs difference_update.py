# The difference() method will not update the original set while difference_update() will update the original set.
# The difference() method will return a new set with only the unique elements from the set on which this method was called. difference_update() will not return anything.

color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

# difference of two sets
new_set = color_set.difference(remaining_colors)
print(new_set)
# output {'violet', 'yellow', 'green', 'blue'}
# original set after difference
print(color_set)
# {'green', 'indigo', 'yellow', 'blue', 'violet'}

# difference of two sets
color_set.difference_update(remaining_colors)
# original set after difference_update
print(color_set)
# Output {'green', 'yellow', 'blue', 'violet'}