# i = 1
# j = not not i
# print(j)

# i = 15
# j = 22

# var = 17
# var_right = var >> 1
# var_left = var << 2
# print(var, var_left, var_right)

# x = 1
# y = 0
#
# z = ((x == y) and (x == y)) or not(x == y)
# print(not(z))


# x = 4 # 0100
# y = 1 # 0001
#
# a = x & y # 0000
# b = x | y # 0101 = 5
# c = ~x  # tricky! = 1011 = ?
# d = x ^ 5 # 1
# e = x >> 2 # 1
# f = x << 2 # 16
#
# print(a, b, c, d, e, f)

#listing
# numbers = [1, 2, 15, 17, 19, 3]
# print("here are the numbers: ", numbers)
# print("and here is a specific number: ", numbers[2])



# numbers = [10, 5, 7, 2, 1]
# print("Original list content:", numbers)  # Printing original list content.
#
# numbers[0] = 111
# print("\nPrevious list content:", numbers)  # Printing previous list content.

# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("Previous list content:", numbers)  # Printing previous list content.

# print("\nList length:", len(numbers))  # Printing the list's length.


# numbers = [1, 4, 11, 18, 91, 100, 0]
# print(len(numbers))
#
# numbers[1] = numbers[4]
#
# del numbers[1] # delete 1 element in list "4"
# print(len(numbers)) # output 6
# print(numbers) # skip "4"
#
# print(numbers[4])
# numbers[4] = 1
# print(numbers[1])



# numbers = [10, 5, 7, 2, 1]
# print("Original list content:", numbers)  # Printing original list content.
#
# numbers[0] = 111
# print("\nPrevious list content:", numbers)  # Printing previous list content.
#
# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("Previous list content:", numbers)  # Printing previous list content.
#
# print("\nList's length:", len(numbers))  # Printing previous list length.
#
# ###
#
# del numbers[1]  # Removing the second element from the list.
# print("New list's length:", len(numbers))  # Printing new list length.
# print("\nNew list content:", numbers)  # Printing current list content.
#
# print(numbers[3])
# numbers[3] = 1
# ###
#

# hat_list = [1, 2, 3, 4, 5]
# hat_list[2] = int(input("please input number: "))
# del hat_list[-1]
# print(len(hat_list))
# print(hat_list)

# #adding element to the list I
# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)
#
# ###
#
# numbers.append(4)
#
# print(len(numbers))
# print(numbers)
#
# ###
#
# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)
#
# numbers.insert(1, 333)
# print(len(numbers))
# print(numbers)


# my_list = [] # create an empty list.
# for i in range(5):
#     my_list.insert(0, i + 1)
# print(my_list)

# my_list = [] # create an empty list
#
# for i in range(5):
#     my_list.append(i+1)
# #my_list.sort(reverse=True)
# print(my_list)

# # count sum of elements in the list
# my_list = [10, 1, 8, 3, 5]
# total = 0
#
# for i in my_list:
#     total += i
#
# print(total)

