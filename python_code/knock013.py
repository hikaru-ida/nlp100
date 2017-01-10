with open('../data/col1.txt', 'r') as col1,\
        open('../data/col2.txt', 'r') as col2, \
        open('../data/col1_2.txt', 'w') as col1_2:
    for line1, line2 in zip(col1, col2):
        line1 = line1.strip()
        line2 = line2.strip()
        s = line1 + "\t" + line2
        col1_2.write("%s\n" % s)
