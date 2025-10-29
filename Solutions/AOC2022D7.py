

with open('../InputFiles/InputFile7', 'r') as file:
    inputfile = file.readlines()


updlines = []
for line in inputfile:
    line = line.replace("\n","")
    updlines.append(line)


masterdict={}
filesize = {}
curdir = "/"


masterdict["/"] = "dr a"

def ls_mode(input,curdir,masterdict):
    arr = input.split(" ")
    size = arr[0]
    fileName = arr[1]

    if size.isdigit():
        filesize[fileName] = int(size)
        masterdict[curdir] = masterdict[curdir] + "|" + fileName + " " + size
    else:
        masterdict[curdir] = "dr " + fileName

curdir = "dr a"
ls_mode("dir e", curdir, masterdict)
print(masterdict)
ls_mode("29116 f", curdir, masterdict)
ls_mode("2557 g", curdir, masterdict)


print(masterdict)




def change_dir(dir, curdir,masterdict):
    if dir == "..":
        curdir = masterdict.get(curdir)
    if dir == "/":
        curdir = "/"
    else: curdir = dir

    return curdir

change_dir("dr a", curdir, masterdict)
print(curdir)