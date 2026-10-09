#lets cover all set commands 
# set is the unordered collections of unique items 

set_1 = {1,2,3,4,5,6,7,8,9,9,10}
set_2 = {6,7,8,9,10,11,12,13,14,15}

print(set_1)
print(set_2)

# # set operations in python - union,intersection,difference,symmetric difference
print("Union of set_1 and set_2 is ",set_1.union(set_2))
print("Intersection of set_1 and set_2 is ",set_1.intersection(set_2))
print("Difference of set_1 and set_2 is ",set_1.difference(set_2))
print("Symmetric difference of set_1 and set_2 is ",set_1.symmetric_difference(set_2))

list=[1,1,2,2,3,3,4,4,5,5] # convert list to set to remove duplicates
print(set(list))