with open('../InputFiles/InputFile5', 'r') as file:
    file = file.readlines()


box_order = {}
box_order2 = {}
newlines = []
for line in file:
    line = line.strip("\n")
    newlines.append(line)

num_lines = 9 # adjust by the largest number of boxes

for i in range(0,num_lines): # organizes the first part of the input into respective keys, by far the most annoying part
    line_horizontal = list(newlines[i]) # grab each horizontal line
    for j in range(1, len(line_horizontal)): # loop through each char in horiz line
        char_vertical = line_horizontal[j - len(line_horizontal)] #START AT BOTTOM VERY IMPORTANT
        if char_vertical.strip().isalpha(): #IF STRIP IS ONLY CHAR APPEND
            count = 1
            if j != 1:
                count = int((j - 1)/4) + 1 # this is b/c chars are placed every 4 indexes at max due to space brackets etc
            if box_order.get(count) is not None:
                box_order[count] += char_vertical
            else:
                box_order[count] = char_vertical
box_order2 = box_order.copy()

def instruction_parser(line): # splits a word instruction into an easier to understand x|y|z format instruction
    string = '|'
    for char in line.split(' '):
        if char.isdigit():
            string += char + "|"
    return string

def instruction_completer(instruction):
   insts = instruction.split('|')
   destination_num = int(insts[3])
   start_num = int(insts[2])
   bound_num = int(insts[1])
   start = box_order[start_num]
   end = box_order[destination_num]
   for i in range(bound_num):
       letter = start[:1]
       start = start[1:]
       end = letter + end
   box_order[start_num] = start
   box_order[destination_num] = end

def instruction_completer2(instruction): # same as p1 except instead of going from bottom to top its top to bottom: too lazy to write better lol
    insts = instruction.split('|')
    destination_num = int(insts[3])
    start_num = int(insts[2])
    bound_num = int(insts[1])
    start = box_order2[start_num]
    end = box_order2[destination_num]
    letter = start[:bound_num]
    start = start[bound_num:]
    end = letter + end
    box_order2[start_num] = start
    box_order2[destination_num] = end



for line in range(10, len(newlines)): # adjust based on the index where the first instruction starts - 1
    instruction = instruction_parser(newlines[line])
    instruction_completer(instruction)
    instruction_completer2(instruction)


stringp1 = ""
stringp2 = ""
for i in range(1,num_lines + 1):
    stringp1 += box_order[i][0]
    stringp2 += box_order2[i][0]

print("Part One:", stringp1)
print("Part Two:", stringp2)