"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    a = ask_score()
    if 0 < a < 50:
        print("Bad")
    elif  a > 100:
        print("Invalid score")
    elif 50> a > 90:
        print("Passable")
    elif a > 90:
        print("Excellent")
    else:
        print("Invalid score")

def ask_score():
    score = eval(input("enter your score:"))
    return score


def new_part():
    output = random.randint(101)
    return output