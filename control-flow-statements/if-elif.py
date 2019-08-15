get_age = int(input("Enter your age")) 

if get_age <= 13:
    print("Kids are allowed from Gate No. 3")
elif get_age <= 40:
    print("Adults are allowed from Gate No. 4")
else:
    print("Old Citizen are allowed from Gate No. 5")