import re

custom_variables = {}


def create_variable(x):
    x = x.replace(" ", "")
    new_var = x.split("=")

    if new_var[0].isalpha() == False:
        print("Invalid identifier")
        calc()

    elif new_var[1].isalpha() == True and new_var[1] not in custom_variables:
        print("Unknown variable")
        calc()

    elif new_var[1].isalpha() == False and new_var[1].isdigit() == False or len(new_var) > 2:
        print("Invalid assignment")
        calc()

    if new_var[1] in custom_variables:
        custom_variables[new_var[0]] = custom_variables[new_var[1]]
    else:
        custom_variables[new_var[0]] = new_var[1]


def add_variable(x):
    new_var = x.split()

    if new_var[0].isalpha() == False:
        print("Invalid identifier")
        calc()
    try:
        print(custom_variables[new_var[0]])
        calc()  # Watch this for potential errors
    except KeyError:
        print("Unknown variable")
        calc()


def change_variable(x):
    for var in x:
        if var.isalpha():
            try:
                x = x.replace(var, custom_variables[var])
            except KeyError:
                print("Unknown variable")

    print(eval(x))
    calc()


def calc():
        inp = input()
        answer = []
        for char in inp:
            answer.append(char)

        if len(answer) == 1:
            new_answer = ""
            for i in answer:
                new_answer += i
            if new_answer.isalpha():
                add_variable(inp)
            else:
                try:
                    print(int(new_answer))
                    calc()
                except ValueError:
                    print("Invalid expression")
                    calc()

        elif len(answer) == 0:
            calc()

        elif "=" in inp:
            create_variable(inp)
            calc()

        elif "+" in inp or "-" in inp or "/" in inp or "*" in inp or "(" in inp or ")" in inp:
            if inp == "/help":
                print("The program calculates the sum of numbers")
                calc()
            elif inp == "/exit":
                print("Bye")
                exit()
            else:
                try:
                    print(eval(inp))
                    calc()
                except SyntaxError:
                    if inp[0] == "/":
                        print("Unknown command")
                        calc()
                    else:
                        print("Invalid expression")
                        calc()
                except NameError:
                    change_variable(inp)

        else:
            add_variable(inp)


calc()
