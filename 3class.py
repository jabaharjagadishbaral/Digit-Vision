# #list vs tuple vs dictionary vs set
# #list is ordered collection of items and it is mutable
# #tuple is ordered collection of items and it is immutable
# #dictionary is unordered collection of key-value pairs and it is mutable
# #set is unordered collection of unique items and it is mutable

# #ordered means that the items have a defined order, and that order will not change.
# #unordered means that the items do not have a defined order, and that order may change.


# #list_commands.py
# #all list commands in python - append,extend,insert,remove,pop,clear,index,count,sort,reverse,copy

# list_1 = [1,2,3,4,5,5,6,7,8,9,10]
# list_2 = [11,12,13,14,15]

# list_1.append(11) #add an element to the list
# list_1.extend([11,12,13])
# print(list_1)

# list_1.insert(1,24)
# print(list_1)

# list_1.remove(5)
# print(list_1)

# list_1.pop()
# print(list_1)

# list_1.clear()
# print(list_1)

# list_1.pop(2)
# print(list_1)

# list_1.sort()
# list_1.sort(reverse=True) #or we can use that list.reverse()

# #slicing of list
# print(list_1[2:4])

# print(list_1[:5]) #get element from the start to index 4

# print(list_1[::-1]) #get elements in reverse order



#lets do tuple commands in python - count, index

tuple_1 = (1,2,3,4,5,5,5,6,7,8,9,10)

print(len(tuple_1))
print(tuple_1)

print(tuple_1.count(5))
print(tuple_1.index(4))

#dictionary

dict_1={'name':'kuna','age':25,'city':'kolkata'}
dict_2={'name':'kuna','age':25,'city':'kolkata'}

print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())

#acessing the dictionary usingn two methods - using key and using get method
#advantages of using get method is that it will not throw an error if the key is not found, it will return None instead
print(dict_1.get('colony', 'not found'))
print(dict_1['colony']) #this will throw an error if the key is not found

dict_1