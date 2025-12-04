with open('../InputFiles/InputFile10', 'r') as file:
    lines = file.readlines()
newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)


def part_one():
    masterdict = {}
    regValue = 1
    cycle = 1
    for line in newlines:
        if 'addx' in line:
            items = line.split(' ')
            cycle += 1
            masterdict[cycle] = regValue
            cycle += 1
            regValue += int(items[1])
            masterdict[cycle] = regValue
        if 'noop' in line:
            cycle += 1
            masterdict[cycle] = regValue
    return (20*masterdict[20]) + (60*masterdict[60]) + (100*masterdict[100]) + (140*masterdict[140]) + (180*masterdict[180]) + (220*masterdict[220])
def part_one_test():
    masterdict = {}
    regValue = 1
    cycle = 1
    masterdict[cycle] = regValue
    for line in newlines:
        if 'addx' in line:
            items = line.split(' ')
            cycle += 1
            masterdict[cycle] = regValue
            cycle += 1
            regValue += int(items[1])
            masterdict[cycle] = regValue
        if 'noop' in line:
            cycle += 1
            masterdict[cycle] = regValue
    return masterdict


rows = 6
cols = 40
grid = [['.' for _ in range(cols)] for _ in range(rows)]
num_cycle = 1
sprite_pos = 1
ypos = 0
masterdict2 = part_one_test()
print(masterdict2)
while num_cycle < 220:
    for i in range(0,40):
        sprite_pos = masterdict2[num_cycle]
        if sprite_pos- 1 < num_cycle < sprite_pos + 1:
            grid[ypos][num_cycle - 1] = '#'
        num_cycle += 1
    ypos = ypos + 1
print(grid)


# masterdict = {}
# regValue = 1
# cycle = 1
# for line in newlines:
#     if 'addx' in line:
#         items = line.split(' ')
#         cycle += 1
#         masterdict[cycle] = regValue
#         cycle += 1
#         regValue += int(items[1])
#         masterdict[cycle] = regValue
#     if 'noop' in line:
#         cycle += 1
#         masterdict[cycle] = regValue

print('Part One:', part_one())
