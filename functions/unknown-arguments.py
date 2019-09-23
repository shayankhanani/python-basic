def highlights(goals,won, **other):
    print("The goals were: " + goals)
    print("The winner was: " + won)
    for key,val in other.items():
        print(key + ": "+ val)

highlights("3-4","ARG", teams = "BRA vs ARG")
#optional arguments come with after regular parameters
#handle optional positional arguments