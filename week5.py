
def student_result(*marks):
    total = 0
    for score in marks:       # Loop through each mark
        total += score        # Add it to total

    average = total / len(marks)  # Calculate average
    print("Average marks:", average)

    # Determine pass/fail
    if average >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")
student_result(70, 80, 65, 90)

def fruit_price(**kwargs):
    sum = 0
    for i in kwargs.values():  # Loop through all values (prices)
        sum = sum + i          # Add prices together
    return sum


k = fruit_price(mango=10, Apple=5, Orange=15)

# Print the total price
print(k)


print("Fruits available:", list({'mango':10, 'Apple':5, 'Orange':15}.keys()))

def subject_average(**kwargs):
    total = 0
    for mark in kwargs.values():  # Loop through all scores
        total += mark

    average = total / len(kwargs)
    print("Subject Average Score:", average)

# Passing subject codes and marks
subject_average(IT5014=60, IT7809=80, IT6798=50, IT5048=70)

# Import the random module
import random

# Generate one random number between 1 and 20
num = random.randint(1, 20)
print("Random number:", num)

import random

def unique_random_numbers():
    numbers = random.sample(range(1, 21), 20)  # Picks 20 unique numbers from 1 to 20
    print("Unique Random Numbers:", numbers)

unique_random_numbers()
