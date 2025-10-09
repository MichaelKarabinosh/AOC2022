with open("../InputFiles/InputFile3", "r") as file:
    lines = file.readlines()
    num = 0
    for line in lines:
        half = int(len(line) / 2)
        firstComp = line[:half]
        secondComp = line[half:]
        for string in firstComp:
            if string in secondComp:
                if string.isupper():
                    num += ord(string.lower()) - 70
                else:
                    num += ord(string) - 96
                break

    print("Part One:", num)
    num = 0
    res = [] # split array
    n = 3 # how often to split

    for i in range(0,len(lines),n):
       res.append(lines[i:i + n])

    for entry in res:
        firstComp = entry[0]
        secondComp = entry[1]
        thirdComp = entry[2]
        for string in firstComp:
            if string in secondComp:
                if string in thirdComp:
                    if string != "\n":
                        if string.isupper():
                            num += ord(string.lower()) - 70
                        else:
                            num += ord(string) - 96
                        break
    print("Part Two:", num)





