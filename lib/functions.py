#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

greet("Alberto")

def greet_with_default(name="programmer"):
    print(name)

greet_with_default("Alberto")

def add(num1, num2):
    return(num1 + num2)
add(2,2)

def halve(number):
    return(number / 2)
halve(10)