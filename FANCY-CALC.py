def add(n1, n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1,n2):
    return n1/n2



maths_functions = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide}

# result = (maths_functions["*"](3,4))
#print(result)

print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""" ) 

blfag = False
total2 = 0
total = 0
num1 = int(input('Please enter your first number: '))
print("+\n-\n*\n/\n")
operator = input("Please enter your operator: ")
num2 = int(input("please enbter your next number: "))



if operator in maths_functions:
    total = maths_functions[operator](num1, num2)

print(f"your total is {num1} {operator} {num2} = {total}")

while blfag == False:
    continueG = (input("Type 'y' to continue calculating with 4.0, or type 'n' to start a new calculation:"))

    if continueG ==  "y":
        print("+\n-\n*\n/\n")
        operator = (input("Please enter your operator"))
        num2 = int(input("please enbter your next number: "))

        if operator in maths_functions:
            total2 =maths_functions[operator](total, num2)
            print(f"your total is {total} {operator} {num2} = {total2}")
        elif operator not in maths_functions:
            print("wrong calculator")
            exit()
    else:
        exit()
