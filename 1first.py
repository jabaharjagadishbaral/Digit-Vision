# lets do variables and data types in python

# str_var = "Hello, World"
# int_var = 45
# float_var = 3.14
# bool_var = True
# list_var = [1,2,3,"aryan", 4.5, False]
# tuple_var = (1,2,3,"aryan", 4.5, False)
# set_var = {1,2,2,2,3,4,5,5,6}
# dictionary_var = {"name": "Aryan", "age": 20, "is_student": True}

# print(str_var +" "+ str(int_var)) 

# print(f"{str_var}  {int_var}")


# lets do operators in python - +,-,*,/,%,//,**

# int_var1 = 10
# int_var2 = 3

# print(int_var1 + int_var2) # addition
# print(int_var1 - int_var2) # subtraction
# print(int_var1 * int_var2) # multiplication
# print(int_var1 / int_var2) # division
# print(int_var1 % int_var2) # modulus
# print(int_var1 // int_var2) # floor division
# print(int_var1 ** int_var2) # exponentiation

# logical and conditional operators in python - and, or, not, ==, !=, >, <, >=, <=  

# print(int_var1 > int_var2 and int_var1 != int_var2) # True
# print(int_var1 < int_var2 or int_var1 == int_var2) # False
# print(not(int_var1 == int_var2)) # True

# lets do concditional statements example - if, elif, else and switch condition

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# else:
#     print("Grade: D")

# lets do switch case statement in python using dictionary

# dict_1 = {
#     90: "Grade: A",
#     80: "Grade: B",
#     70: "Grade: C"
# }

# grade = dict_1.get(marks, "Grade: D")
# # lambda syntax is lambda arguments: expression
# switch_case = {
#     90: lambda: print("Grade: A"),
#     80: lambda: print("Grade: B"),
#     70: lambda: print("Grade: C"),
#     "default": lambda: print("Grade: D")
# }

# print(switch_case.get(marks, switch_case["default"])())

# lets do loop in python - for loop and while loop



# for i in list_1:

#     if i == 5:
#        continue
#     print(i)


# lets do list condition
# list_1 = [1,2,3,4,5,6,7,8]

# i = 0
# while i < len(list_1):
#     if list_1[i] == 5:
#         i += 1
#         continue
#     print(list_1[i])
#     i += 1


# lets count the number of times each letter ha sbeen reeeated

s = "messi"
l = []

for i in s:
    if i not in l:
        l.append(i)
        print(f"{i} has been repeated {s.count(i)} times")