fruits = ["banana","mango","orange","apple","grape"]
print (fruits[0])  # Accessing the first element of the list

#lists can be changed
fruits[3] = "mamwiwa" # Changing the fourth element of the list

# print(fruits)  # Printing the modified list
#lists can be added to the end of the list
fruits.append("masau") # Adding a new element to the end of the list

# lists can be inserted at a specific position using the insert() method + indexing for the position

fruits.insert(3, "matohwe")  # Inserting "matohwe" at index 3

# lists can be removed from the list using the remove() method + indexing for the position

fruits.remove("grape") # Removing "grape" from the list

# lists can be removed from the end of the list using the pop() method

#list can be sorted using the sort() method

fruits.sort(reverse=True) # Sorting the list in reverse order/
print(fruits)