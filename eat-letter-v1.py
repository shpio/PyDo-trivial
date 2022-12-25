# Prompt the user to enter a word and assign it to the user_word variable.
user_word = str(input("Enter a word: ")).upper()    # upper method added to input from user.

for letter in user_word:
    if letter in "A,U,E,O,I":   # if statement in a single line
        continue
    print(letter)

# test
# input -> Gregory
# output <-
# G
# R
# G
# R
# Y
# input -> abstemious
# output <-
# B
# S
# T
# M
# S
# input -> IOUEA
# output <-
