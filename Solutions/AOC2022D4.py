with open('../InputFiles/InputFile4', 'r') as file:
    lines = file.readlines()

def create_list(n1, n2):
    string = "|"
    while n1 < n2 + 1:
        string += str(n1) + "|"
        n1 += 1
    return string

def hash_list(n1, n2):
    dict = {}
    while n1 < n2 + 1:
        dict[n1] = 0
        n1 += 1
    return dict


def compare_list2(n1, n2,fin):
    while n1 < n2 + 1:
        if n1 in fin:
            return True
        n1 += 1
    return False

countP1 = 0
countP2 = 0
for line in lines:
    pairs = line.split(",")
    pair1 = pairs[0]
    pairs1 = pair1.split("-")
    pairs11 = int(pairs1[0])
    pairs12 = int(pairs1[1])
    pair2 = pairs[1]
    pairs2 = pair2.split("-")
    pairs21 = int(pairs2[0])
    pairs22 = int(pairs2[1])

    if create_list(pairs11, pairs12) in create_list(pairs21, pairs22):
        countP1 += 1
        # print(pairs11, pairs12, pairs21, pairs22)
    elif create_list(pairs21, pairs22) in create_list(pairs11, pairs12):
        # print(pairs11, pairs12, pairs21, pairs22)
        countP1 +=1

    if compare_list2(pairs11, pairs12, hash_list(pairs21,pairs22)):
        countP2 += 1
    elif compare_list2(pairs21, pairs22, hash_list(pairs11,pairs12)):
        countP2 += 1
print("Part One:", countP1, "\nPart Two:", countP2)