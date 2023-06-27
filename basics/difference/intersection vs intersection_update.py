# intersection() will not update the original set but intersection_update() will update the original set with only the common elements.
# intersection() will have a return value which is the new set with common elements between two or more sets whereas intersection_update() will not have any return value.

color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

# intersection of two sets
common_colors = color_set.intersection(remaining_colors)
print(common_colors)  # output {'indigo'}
# original set after intersection
print(color_set)
# Output {'indigo', 'violet', 'green', 'yellow', 'blue'}

# intersection of two sets using intersection_update()
color_set.intersection_update(remaining_colors)
# original set after intersection
print(color_set)
# output {'indigo'}