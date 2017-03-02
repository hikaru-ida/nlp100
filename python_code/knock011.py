f = open('../data/hightemp.txt')

for line in f:
    line = line.strip().replace("\t", " ")
    print(line)
