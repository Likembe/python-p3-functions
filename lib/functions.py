#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()
    

def greet(name = "Naureen"):
    print(f"Hello, {name}!")

greet()

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()

def add(num1, num2):
    return num1 + num2

result = add(1,2)

print(result)

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    
    return number / 2

result = halve(4)
print(result)
