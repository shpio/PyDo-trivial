# my_list = [8, 10, 6, 2, 4] # list to sort
#
# # for i in range(len(my_list)) - 1): # we need (5 - 1) comparisons
# #     if my_list[i] > my_list[i + 1]: # compare adjacent elements
# #         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # if we end up here, we have to swap
# #

# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
#
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print(my_list)

##
# my_list = [8, 10, 6, 2, 4]
#
# swapped = True
#
# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i +1], my_list[i]
#
# print(my_list)

# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)
#



#
# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
#
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)
#
# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print("\nSorted and reversed:")
# my_list.reverse()
# print(my_list)



# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
#
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)
#
# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print("\nSorted:")
# print(my_list)

#######################slices



# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)

#
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:]
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[3:]
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:]
# print(new_list)


# my_list = [10, 8, 6, 4, 2]
# del my_list[:]
# print(my_list)

# my_list = [0, 3, 12, 8, 2]
#
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)


# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
#
# for i in my_list:
#     if i > largest:
#         largest = i
# print(largest)

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
#
# for i in my_list[1:]:
#     if i > largest:
#         largest = i
# print(largest)

#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
#
# if to_find in my_list:
#     print(to_find)

# my_list = [3, 11, 5, 1, 9, 7, 15, 13, 17]
# largest = my_list[0]
#
# for i in range(len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]
# print(largest)

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
#
# for i in my_list:
#     if i > largest:
#         largest = i
# print(largest)


#slice to save comp power
# my_list = [3, 11, 5, 1, 9, 7, 15, 13, 17]
# largest = my_list[0]
#
# for i in my_list[1:]:
#     if i > largest:
#         largest = i
#
# print(largest)

# works
# my_list = [3, 11, 5, 1, 9, 7, 15, 13, 17]
# largest = my_list[0]
#
# for i in my_list:
#     if i > largest:
#         largest = i
#
# print(largest)

# fixed
# my_list = [3, 11, 5, 1, 9, 7, 15, 13, 17]
# largest = my_list[0]
#
# # for i in range(1, len(my_list)):
# for i in my_list:
#     if i > largest:
#         largest = i
#
# print(largest)

# ---------------repeat---slices------------------
# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)

#
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1] # 2 is the end. prints till the end
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# del my_list[1:3]
# print(my_list)

#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
#
# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
# if found:
#     print("Element found at index", i)
# else:
#     print("absent")




# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0

# for i in bets:
#     if i in drawn:
#         hits += 1
#         var = print(i)
#         continue
# print("You guess righ 4 numbers", hits)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
#
# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
#
# if found:
#     print("Element found at index", i)
# else:
#     print("absent")

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# new_list = my_list[:]
# print(new_list)

# for i in my_list:
#     if my_list[i] == my_list[i]:
#         del my_list[i]


# print("The list with unique elements only:")
# print(my_list)

#################################################################################################################33
## Advanced list - CHESS

EMPTY = "-"
ROOK = "ROOK"
KNIGHT = "KNIGHT"
BISHOP = "BISHOP"
QUEEN = "QUEEN"
KING = "KING"
PAWN = "PAWN"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[0][1] = KNIGHT
board[0][6] = KNIGHT
board[7][1] = KNIGHT
board[7][6] = KNIGHT
board[0][2] = BISHOP
board[0][5] = BISHOP
board[7][2] = BISHOP
board[7][5] = BISHOP
board[0][3] = QUEEN
board[7][3] = QUEEN
board[0][4] = KING
board[7][4] = KING
board[1][0] = PAWN
board[1][1] = PAWN
board[1][2] = PAWN
board[1][3] = PAWN
board[1][4] = PAWN
board[1][5] = PAWN
board[1][6] = PAWN
board[1][7] = PAWN
board[6][0] = PAWN
board[6][1] = PAWN
board[6][2] = PAWN
board[6][3] = PAWN
board[6][4] = PAWN
board[6][5] = PAWN
board[6][6] = PAWN
board[6][7] = PAWN

print(board)





















