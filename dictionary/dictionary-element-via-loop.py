todaysCustomer = {"name":"Mark", "email":"mark@zuckerberg.com", "city":"San Francisco", "telephone": 92321321321}
for items in todaysCustomer.values():
    print(items)
for items in todaysCustomer.keys():
    print(items)
for keys, items in todaysCustomer.items():
    print("Todays customer's "+ keys + " is "+ str(items))