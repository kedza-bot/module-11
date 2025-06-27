#sets are unordered collections of unique elements
# They are mutable, meaning you can add or remove elements after creation.but they do not allow duplicate elements.
# Sets are defined using curly braces {} or the set() constructor.
# Sets are useful for membership testing, removing duplicates from a collection, and performing mathematical set operations like union, intersection, and difference.
# Example of a set
'''
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Printing the set

# Adding an element to the set
my_set.add(6)
print(my_set)  # Printing the set after adding an element

# Removing an element from the set
my_set.remove(3)
print(my_set)  # Printing the set after removing an element
'''

#union is the operation of combining two sets to create a new set that contains all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

mubatanidzwa = set1.union(set2)  # Union of set1 and set2 and creating a new set removing duplicates
print(mubatanidzwa)  # Printing the union of the sets

# Intersection is the operation of finding common elements between two sets.
zvinownikwa_mose = set1.intersection(set2)  # Intersection of set1 and set2
print(zvinownikwa_mose)  # Printing the intersection of the sets

#difference is the operation of finding elements that are in one set but not in another.
kusiyana = set1.difference(set2)  # Difference of set1 and set2

print(kusiyana)  # Printing the difference of the sets is what is in set1 but not in set2
#when to use sets:
# 1. When you need to store unique elements and want to avoid duplicates.
# 2. When you need to perform mathematical set operations like union, intersection, and difference.
# 3. When you need to check for membership efficiently, as sets provide average O(1) time complexity for membership tests.
# 4. When you need to perform operations that require unordered collections of elements.
# 5. When you need to remove duplicates from a list or other iterable.