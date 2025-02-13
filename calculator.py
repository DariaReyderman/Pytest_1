import math
import sqlite3


def add(a, b):
    return a + b  # + 0.1 # 0.99999999999


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def make_error():
    raise IndexError()


def create_table(query):
    # check if table exists
    raise sqlite3.IntegrityError


def say_hello():
    name = input("Enter name? ")
    return f"hello {name}"


# ------- HOMEWORK -------
# a
def power(a, b):
    return a ** b


# b
def sqrt(b):
    return math.sqrt(b)


# c
def factorial(c):
    return math.factorial(c)
