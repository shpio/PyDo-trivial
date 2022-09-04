block_num = int(input("input number of blocks: ")) # 6

a = 1
b = 1
c = a + b
c = b
while block_num != 0:
    c = a + b
    b = c
    print(a, b, c)
# i = 3
# for i in range(5):
#     print(i)
# else:
#     print("else:", i)



#
# i = 111
# for i in range(2, 1):
#     print(i)
# else:
#     print("else:", i)





# i = 5
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)



# word_without_vowels = ""
# user_word = input("Enter a word: ")
# user_word = user_word.upper()
#
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#
#     word_without_vowels = print(letter, end="")
# pass



# for i in user_word:
#     if i == "A":  # or "E" or "I" or "O" or "U":
#         continue
#     print(i)
#
# pass

# #for loop and continue
# user_word = input("Enter a word: ")
# user_word = user_word.upper()
#
# for i in user_word:
#     if i == "A" :
#         continue
#     elif i == "E":
#         continue
#     elif i == "I":
#         continue
#     elif i == "O":
#          continue
#     elif i == "U":
#         continue
#     print(i)
#
# pass


# word_ = input("enter a word: ")
# while word_ != "chupacabra":
#     word_ = input("enter a word: ")
#     break
# print("You've successfully left the loop.")

# word_ = input("enter a word: ")
# while word_ != "chupacabra":
#     word_ = input("enter a word: ")
# #    break
#     print("You are at the end of loop")
# print("You've successfully left the loop.")


# largest_number = -99999999
# counter = 0
#
# number = int(input("Enter a number or type -1 to end program: "))
#
# while number != -1:
#     if number == -1:
#         continue
#     counter += 1
#
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end program: "))
#
# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")



# for i in range(10):
#     print("The value of i is currently", i)
#
# for i in range(2, 8):
#     print("The value of i is currently", i)
#
# for i in range(-10, -1, 5):
#     print(i)

# power = 1
# for expo in range(16):
#     print("2 to the power of ", expo, "is", power)
#     power *=2



#import time
# Write a for loop that counts to five.
# Body of the loop - print the loop iteration number and the word "Mississippi".
# Body of the loop - use: time.sleep(1)



# for i in range(1, 6):
#     print(i, "Mississippi")
#     time.sleep(1)
# # Write a print function with the final message.
#
# print("Ready or not, here I come!")




# break - example
# print("The break instruction:")
# for i in range(-3, 3):
#     if i == 2:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")
#
#
# # continue - example
#
# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 4:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.",i)

