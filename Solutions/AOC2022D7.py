

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




def cd(option, curdir,masterdict):
    if option == "..":
        curdir = masterdict.get(curdir)
    if option == "/":
        curdir = "/"
    else: curdir = "dr " + option

    return curdir


def find_dir(dirtofind,masterdict):
    return [key for key, val in masterdict.items() if val == dirtofind]

masterdict["dr /"] = "dr a"
masterdict["dr a"] = "dr e"
masterdict["dr e"] = "584 i"

print(cd("/", curdir, masterdict))
curdir = "dr e"
print(masterdict["dr e"])
print(cd("..",curdir,masterdict))
print(find_dir("dr e", masterdict))
print('hi')