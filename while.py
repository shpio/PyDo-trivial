print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""
)

number = int(input("Enter a number: "))
secret_number = 111

while number != secret_number:
    if number != secret_number:
        print("Ha ha! You're stuck in my loop!")
        number = int(input("Enter a number: "))
print("Well done, muggle! You are free now.")


# # Store the current largest number here.
# largest_number = -999999999
#
# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))
#
# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))
#
# # Print the largest number.
# print("The largest number is:", largest_number)

# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# odd_numbers = 0
# even_numbers = 0
#
# number = int(input("Enter a number or type 0 to stop: "))

# while number:
#     if number %2:
#         even_numbers +=1
#     else:
#         odd_numbers +=1
#     number = int(input("Enter a number or type 0 to stop: "))
#
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count: ", even_numbers)

