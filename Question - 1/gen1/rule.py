import numpy as np
import pandas as pd
from colorama import Fore, Back, Style

iterations = int(input())
if(iterations == -1):
    print("Adios")
    quit()


# Getting the configuration
config_file_dir = "./config.txt"
config_file = open(config_file_dir, 'r')
config_file_content = config_file.read()
config_file_content = config_file_content.split('\n')
temp = config_file_content[0].split(' ')
config_file_content = config_file_content[1:]
m = int(temp[0])
n = int(temp[1])
k = int(temp[2])
marked_cells = []
for i in range(k):
    temp = config_file_content[i].split(' ')
    marked_cells += [[int(temp[0]) - 1, int(temp[1]) - 1]]


class config():
    def __init__(self, m, n, k, marked_cells):
        self.m = m
        self.n = n
        self.k = k
        self.marked_cells = marked_cells
        self.char = '   '
        self.x_char_out = Fore.BLACK + Back.BLACK + self.char + Style.RESET_ALL
        self.o_char_out = Fore.WHITE + Back.WHITE + self.char + Style.RESET_ALL
        self.x_char = 1
        self.o_char = 0
        self.space_char = ' '
        self.new_line = '\n'
        self.grid_list = self.grid()
    def grid(self):
        grid = []
        for i in range(m):
            temp = []
            for j in range(n):
                if([i, j] in marked_cells):
                    temp += [1]
                else:
                    temp += [0]
            grid += [temp]
        return grid
    def render(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]):
                    print(self.x_char_out, end = self.space_char)
                else:
                    print(self.o_char_out, end =self.space_char)
            print(self.new_line)
        # The print seems to be working.
    def new_gen(self):
        grid = self.grid_list[:]
        for i in range(len(grid)):
            grid[i] = [0] + grid[i] + [0]
        grid = [[0]*len(grid[0])] + grid + [[0]*len(grid[0])]
        # Now the grid is padded and the new generation can be used as the reference, since it is padded. 
                

conf = config(m, n, k, marked_cells)
print(m, n, k)
print(marked_cells)
conf.render(conf.grid_list)
print('\n\n')
conf.new_gen()