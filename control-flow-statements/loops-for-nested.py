first_name = ["John","Jason","Gerry","Mark"]
last_name = ["Snow", "White","Henry","Waugh"]
name_generated = []
for first in first_name:
    for last in last_name:
        name = first + " " + last
        name_generated.append(name)
        print(name)

print(name_generated)