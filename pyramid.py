# input number of blocks
blocks = int(input("Enter the number of blocks: "))
height = 0
while blocks > height:
# relation betwen amount of block and height
    height = height + 1
    blocks = blocks - height
print("The height of the pyramid:", height)

























