with open('../InputFiles/InputFile7', 'r') as file:
    inputfile = file.readlines()


updlines = []
for line in inputfile:
    line = line.replace("\n","")
    updlines.append(line)


masterdict={}
curdir = "/"


masterdict["/"] = "a"

def ls_mode(input,curdir,masterdict):
    arr = input.split[" "]
    size = arr[0]
    fileName = arr[1]
    masterdict[curdir] = masterdict[curdir] + fileName






def change_dir(dir, curdir,masterdict):
    if dir == "..":
        curdir = masterdict.get(curdir)
    if dir == "/":
        curdir = "/"
    else: curdir = dir

    return curdir
