col1 = open('../data/col1.txt', 'w')
col2 = open('../data/col2.txt', 'w')

with open('../data/hightemp.txt', "r") as f:
    for line in f:
        ls = line.strip().split()
        col1.write("%s\n" % ls[0])
        col2.write("%s\n" % ls[1])

col1.close()
col2.close()
