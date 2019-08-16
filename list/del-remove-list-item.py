cities = ["Karachi","Lahore","Islamabad","Quetta","Pehawar","Hyderabad","Sialkot","Gawadar","Mardan"]
del cities[8]
# print(cities[8]) index out of range error because now the list size is of 7 index
cities.remove("Gawadar")
#print(cities[7]) index out of range error because now the list size is of 6 index