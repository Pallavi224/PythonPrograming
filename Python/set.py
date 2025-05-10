#set is unoredered
# set is mutable
# set is iterable   
# set is unindexed
# set is unordered collection of items
# set is mutable, so we can change the value of a set after it is created   
# set is iterable, so we can iterate over the elements of a set
# set is unindexed, so we cannot access the elements of a set using index   
    #there is no duplicate elements in set
my_set={1,2,3,4,4,5,6,'pallavi','Rajnish','pallavi','Rajnish',True,False}
print(my_set)

my_set.add(10) # adds 10 to the set
print(my_set)
my_set.add(20) # adds 20 to the set
print(my_set)

my_set.remove(20) # removes 20 from the set
print(my_set)
print("------------------pop------------------")
my_set.pop() # removes the first element from the set
print(my_set)

print("------------------clear------------------")
my_set.clear() # removes all the elements from the set      
print(my_set)
print("------------------discard------------------")
my_set.discard(1) # removes 1 from the set      
print(my_set)

# Example of set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union of sets
union_set = set_a.union(set_b)
print("Union:", union_set)

# Intersection of sets
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)

# Difference of sets
difference_set = set_a.difference(set_b)
print("Difference:", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", symmetric_difference_set)