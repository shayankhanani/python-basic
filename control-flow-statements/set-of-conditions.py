pyth = input("Do you know Python")
js = input("Do you know JavaScript")
csharp = input("Do you know csharp")

if pyth == "Yes" and js == "No" or csharp == "Yes":
    print("JS is mandatory, Please try letter")
elif pyth == "Yes" and js == "Yes" or csharp == "No":
    print("Welcome to CodeScript")
else:
    print("Better luck next time!")