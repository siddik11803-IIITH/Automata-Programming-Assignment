from colorama import Fore, Back, Style
import os
import time

class config():
    def __init__(self, m, n, k, marked_cells, rule):
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
        self.new_line = ''
        self.grid_list = self.grid()
        self.output_file = open('./output.txt', 'w')
        self.rule = rule
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
    def new_gen(self, title):
        grid = self.grid_list[:]
        for i in range(len(grid)):
            grid[i] = [0] + grid[i] + [0]
        grid = [[0]*len(grid[0])] + grid + [[0]*len(grid[0])]
        # Now the grid is padded and the new generation can be used as the reference, since it is padded. 
        neigbours = [
            [1, 1], [1, 0], [1, -1],
            [0, 1],         [0, -1],
            [-1, 1], [-1, 0], [-1, -1],
        ]
        next_gen = []
        for i in range(1, len(grid)-1):
            temp = []
            for j in range(1, len(grid[0])-1):
                temp_n = [grid[i+x[0]][j + x[1]] for x in neigbours]
                # temp-n has the neighbour values for i, j th positions in the grid
                temp += [self.rule(grid[i][j], temp_n)] # this is the place we are going to have to add the rule
            next_gen += [temp]
        self.render(next_gen)
        self.grid_list = next_gen
        self.output_file.write(self.output_string(self.grid_list, title))
    def test_rule(self, state, neighbours):
        if(state):
            return 1
        else:
            if(neighbours[4]):
                return 1
            else:
                return 0
    def output_string(self, grid, title):
        str_out = title+"\n"
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]):
                    str_out += '1'
                else:
                    str_out += '0'
            str_out += '\n'
        return str_out + '\n'



question = 1


iterations = int(input("Enter number of iterations: "))
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



def rule_q1(state, neighbours):
    if(state):
        return 1
    else:
        if(neighbours[4]):
            return 1
        else:
            return 0

def rule_q2(state, neighbours):
    print()
    if(neighbours[1] == 1 and neighbours[6] == 1 and state == 1):
        return 1
    if(neighbours[3] == 1 and neighbours[4] == 1 and state == 1):
        return 1
    elif(neighbours[2] and neighbours[4] and neighbours[7]):
        return 1
    elif(neighbours[0] and neighbours[3] and neighbours[5]):
        return 1
    elif(neighbours[0] and neighbours[1] and neighbours[2]):
        return 1
    elif(neighbours[5] and neighbours[6] and neighbours[7]):
        return 1
    return 0

def rule_q3(state, neighbours):
    if(neighbours[1] or neighbours[6] or state):
        return 1
    return 0


rule_dict = {1: rule_q1, 2: rule_q2, 3: rule_q3}

conf = config(m, n, k, marked_cells, rule_dict[question])



# Actually rendering the answer. 
os.system('clear')
print('Initial State')
conf.render(conf.grid_list)
time.sleep(0.7)
for i in range(iterations):
    os.system('clear')
    conf.new_gen('Iteration - '+ str(i+1))
    print('Iteration - '+ str(i+1))
    time.sleep(0.7)
