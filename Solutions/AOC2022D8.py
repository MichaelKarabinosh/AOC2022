
with open('../InputFiles/InputFile8', 'r') as file:
    lines = file.readlines()
newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

grid = []

for line in newlines:
    elements = list(line)
    grid.append(elements)

total = 0

def count_trees(grid,x,y):
    val = int(grid[y][x])
    top = 1
    bottom = 1
    left = 1
    right = 1
    for t in range (0,y): # top
        if int(grid[t][x]) >= val:
            top = 0
    for b in range (y+1,len(grid)): # bottom
        if int(grid[b][x]) >= val:
            bottom = 0
    for l in range (0,x): # left
        if int(grid[y][l]) >= val:
            left = 0
    for r in range (x+1,len(grid)): # right
        if int(grid[y][r]) >= val:
            right = 0
    # print(top,bottom,left,right,int(grid[y][x]))
    return top or bottom or left or right

def part_one():
    total = 0
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[y])-1):
                 if count_trees(grid, x, y):
                    # print(y,x)
                    total += 1
    total += 2*len(grid) + 2*(len(grid) - 2)
    return total

def count_scenic_score(grid,x,y):
    val = int(grid[y][x])
    total_top = 0
    total_bottom = 0
    total_left = 0
    total_right = 0
    for t in range (y-1,-1,-1): # top
        if int(grid[t][x]) < val:
            total_top += 1
        else:
            total_top += 1
            break
    for b in range (y+1,len(grid)): # bottom
        if int(grid[b][x]) < val:
            total_bottom += 1
        else:
            total_bottom += 1
            break
    for l in range (x-1,-1,-1): # left
        if int(grid[y][l]) < val:
            total_left += 1
        else:
            total_left += 1
            break
    for r in range (x+1,len(grid)): # right
        if int(grid[y][r]) < val:
            total_right += 1
        else:
            total_right += 1
            break
    print(total_top, total_bottom, total_left, total_right,y,x)
    return total_top * total_bottom * total_left * total_right

def part_two():
    max = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            num = count_scenic_score(grid, x, y)
            if num > max:
                max = num
    return max

print('Part One:', part_one())
print('Part Two:', part_two())