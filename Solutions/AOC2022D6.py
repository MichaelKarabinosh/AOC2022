with open('../InputFiles/InputFile6', 'r') as file:
    line = file.readline().strip()


def check_str(str):
    dict = {}
    for char in str:
        if char in dict:
            return False
        dict[char] = 0
    return True

def check_line(step):
    for i in range(0, len(line)):
        str = line[i:i+step]
        if check_str(str):
            return i+step
    return None



print("Part One:", check_line(4))
print("Part Two:", check_line(14))