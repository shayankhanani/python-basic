def operation(input1,input2):
    result = input1 + input2
    print(str(result))

operation(2,3)
#parameter by position

def printer(name, last):
    print(name + " " + last)
#parameter by keywords
printer(name="Shayan",last="Khanani")
printer(last="Khanani", name = "Shayan")

def salary_calc(salary, tax = 0.013):
    print(str(salary*tax))

salary_calc(30000,0.01)
#default parameter of tax = 0.013
salary_calc(40000)

#positional and keyword arguments
def greet(greeting, name):
    print(greeting + ", " + name)


#greet(greeting="Good Morning", "Shayan")
greet("Hello", name = "Shayan")


