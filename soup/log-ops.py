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

# my_list = [10, 1, 8, 3, 5]
# total = 0
#
# for i in range(len(my_list)):
#     total += my_list[i]
#
# print(total)

# # practice swapping variables
#
# a = 1
# b = 2
#
# a, b = b, a
# print("a = ", a, "b = ", b, end="")

# # example
# my_list = [10, 1, 8, 3, 5]
#
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
#
# print(my_list)

# # not clear
# my_list = [10, 1, 8, 3, 5]
# length = len(my_list)
#
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i -1], my_list[i]
# # output is [5, 3, 8, 1, 10]
#
#
# print(my_list)

######################################lab######################################
#
# # step 1
# beatles = []
# print("Step 1:", beatles)
#
# # step 2
# beatles.append("John lennon")
# beatles.append('Paul McCartney')
# beatles.append('George Harrison')
#
# print("Step 2:", beatles)
#
# # step 3
# for i in 'Stu Sutcliffe', 'Pete Best':
#     beatles.append(i)
# print("Step 3:", beatles)
#
# beatles.index('Pete Best', 1)
#
# # step 4
# # del beatles[3]
# # del beatles[3]
# ## or
# del beatles[-2]
# del beatles[-1]
# print("Step 4:", beatles)
#
# # step 5
# beatles.insert(0, 'Ringo Starr')
# print("Step 5:", beatles)
#
# # testing list legth
# print("The Fab", len(beatles))


# my_list = [1, None, True, 'I am a string', 256, 0]
# print(my_list)
#
# my_list[1] = '?'
# print(my_list)

## nested list
# my_list = [1, 'a', ["list", 64, [0, 1], False]]
# print(my_list)

# my_list = [1, 3, 4, 6]
# del my_list[2]
# print(my_list)
# del my_list[2]
# print(my_list)


# my_list = ['white', 'purple', 'blue', 'yellow', 'green']

# for color in my_list:
#     print(color)

# my_list = ['white', 'purple', 'blue', 'yellow', 'green']
# print(len(my_list))
#
# del my_list[0]
# print(len(my_list))

# 6, 2, 3, 4, 5, 1

# 1, 2, 3, 4, 5

# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0

# for number in lst:
#     # add += number
#     add = add + number
#     print(add)
# ##     lst_2.append(add)
# ## print(lst)
# ## print(lst_2)
# print(add)
#

# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0
#
# for number in lst:
#     add += number
#     lst_2.append(add)
#
# print(lst)
# print(lst_2)

# lst = []
# del lst # deletes list
# print(lst)

## nested list as a single object in the list
# lst = [1, [2, 3], 4]
# print(lst[1])
# print(len(lst))

###############################################come back later !!!!!!!!!!!!!!!!!!!
########### my_list = [10, 1, 8, 3, 5]
########### length = len(my_list)
###########
########### for i in range(length // 2):
###########     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
###########
########### print(my_list)
###########
########### we've assigned the length variable with the current list's length (this makes our code a bit clearer and shorter)
########### we've launched the for loop to run through its body length // 2 times (this works well for lists with both even and odd lengths, because when the list contains an odd number of elements, the middle one remains untouched)
########### we've swapped the ith element (from the beginning of the list) with the one with an index equal to (length - i - 1) (from the end of the list); in our example, for i equal to 0 the (lenght - i - 1) gives 4; for i equal to 1, it gives 3 - this is exactly what we needed.