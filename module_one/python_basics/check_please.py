import math


def split_check(total, number_of_people):
    cost_per_person = total / number_of_people
    return cost_per_person

total_due = float(input("What is the total bill? "))
number_of_people = int(input("How many people are splitting the bill? "))   

amount_due = split_check(total_due, number_of_people)
print(f"Each person owes ${(math.ceil(amount_due))}")


def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("What is the total bill? "))
    number_of_people = int(input("How many people are splitting the bill? "))
    amount_due = split_check(total_due, number_of_people)
    print(f"Each person owes ${(amount_due)}")
except ValueError:
    print("Please enter a valid number for the total bill and number of people.")