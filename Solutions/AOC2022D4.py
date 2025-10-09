with open("../InputFiles/InputFile4", "r") as file:
    lines = file.readlines()
    counter = 0


    for line in lines:
        pairs = line.split(",")
        pair1 = pairs[0]
        num_pair1 = pair1.split("-")
        num_pair1_first = int(num_pair1[0])
        num_pair1_last = int(num_pair1[1])
        pair2 = pairs[1]
        num_pair2 = pair2.split("-")
        num_pair2_first = int(num_pair2[0])
        num_pair2_last = int(num_pair2[1])
        if (num_pair1_last > num_pair2_last) & (num_pair1_first < num_pair2_first):
            counter = counter + 1
        if (num_pair2_last > num_pair1_last) & (num_pair2_first < num_pair1_first):
            counter = counter + 1
print(counter)