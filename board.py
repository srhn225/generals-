from generals import General,Grid,Plain, Swamp, Mountain, Farmer, Lieutenant, Commander,Player
import random
import constant
grid = [[Grid() for _ in range(constant.col)] for _ in range(constant.row)]
def generate_numbers():
    number1 = random.randint(0, 9)
    number2 = random.randint(number1 + 10, 19)
    return number1, number2
def generate_numbers_for_test():
    number1 = random.randint(0, 3)
    number2 = random.randint(0,3)
    return number1, number2
def generate_generals(grid):
    gen1row,gen2row=generate_numbers()
    gen1col,gen2col=generate_numbers()
    #gen1row,gen2row=generate_numbers_for_test()
    #gen1col,gen2col=generate_numbers_for_test()
    grid[gen1row][gen1col]=Commander(0)
    grid[gen2row][gen2col]=Commander(1)
def generate_swamp(grid):
    swamp_num=random.randint(0, 100)
    now_num=0
    while now_num<=swamp_num:
        row=random.randint(0, 19)
        col=random.randint(0, 19)
        if type(grid[row][col]).__name__=="Grid":
            grid[row][col]=Swamp()
            now_num+=1
def generate_mountain(grid):
    mountain_num=random.randint(15, 50)
    now_num=0
    while now_num<=mountain_num:
        row=random.randint(0, 19)
        col=random.randint(0, 19)
        if type(grid[row][col]).__name__=="Grid":
            grid[row][col]=Mountain()
            now_num+=1
def generate_lieutenant(grid):
    lieutebant_num=random.randint(5,15)
    now_num=0
    while now_num<=lieutebant_num:
        row=random.randint(0, 19)
        col=random.randint(0, 19)
        if type(grid[row][col]).__name__=="Grid":
            grid[row][col]=Lieutenant(random.randint(30, 40))
            now_num+=1
def generate_farmer(grid):
    farmer_num=random.randint(5,15)
    now_num=0
    while now_num<=farmer_num:
        row=random.randint(0, 19)
        col=random.randint(0, 19)
        if type(grid[row][col]).__name__=="Grid":
            grid[row][col]=Farmer(random.randint(5, 15))
            now_num+=1
def generate_plain(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if type(grid[i][j]).__name__=="Grid":
                grid[i][j] = Plain()
