def sum(num1, num2):
    print(num1 + num2)


def minus(num1, num2):
    print(num1 - num2)


def mult(num1, num2):
    print(num1 * num2)


def division(num1, num2):
    print(num1 / num2)


def convertToFahrenheit(num1):
    print((num1 * 1.8) + 32)


print("Welcome to the Calculator")
operator = input("What Operator would like to use? [-] [+] [/] [*] [f]")
num1 = float(input("Please Enter Number #1 or Temperature (If you have Choosen)"))
if operator.lower() == "f":
    convertToFahrenheit(num1)
else:
    num2 = float(input("Please Enter Number #2"))

    if "-" in operator:
        minus(num1, num2)
    elif "+" in operator:
        sum(num1, num2)
    elif "/" in operator:
        division(num1, num2)
    elif "*" in operator:
        mult(num1, num2)
    else:
        print("Input Error")
