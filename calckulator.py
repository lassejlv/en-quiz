# simple little calckulator


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    print("Welcome to calculator")
    print("Type 'quit' to exit")
    while True:
        a = input("Enter first number: ")
        if a == 'quit':
            break
        a = float(a)
        b = input("Enter second number: ")
        if b == 'quit':
            break
        b = float(b)
        operation = input("Enter operation: ")
        if operation == 'quit':
            break
        if operation == '+':
            print(add(a, b))
        elif operation == '-':
            print(subtract(a, b))
        elif operation == '*':
            print(multiply(a, b))
        elif operation == '/':
            print(divide(a, b))
        else:
            print("Unsupported operation")
        

    
if __name__ == '__main__':
    main()


#!/usr/bin/env python3
