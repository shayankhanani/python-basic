#line starting with hash symbol are comments and will be ignored by python
#deifning variable in python
name = "Shayan"
print(name)

#case-sensitive nature of python as Name is treated different from name
#print(Name)

name = "Khanani"
#changing value in existing variable
print(name)

#variable containing numbers
lang = 2
print(lang)

#performing maths addition as python knows the variable is number
print(lang + 1)

#sting number with maths
original_num = "23"
#new_num = original_num + 7
#print(new_num) ---illegal: will generate type error string variable can not perform maths in python

original_num = 23
#now the variable value is changed to number
new_num = original_num + 7
print(new_num)

#rules for variable names
#does not contain spaces
# my name = "Shayan Khanani"  ---illegal---
# does not enclose in quotes
# "my name" = "Shayan Khanani" ---illegal---
# my_name = "Shayan Khanani" ---legal---
# 1st_name = Shayan ---illegal--- can not begin with a number but can contain number 