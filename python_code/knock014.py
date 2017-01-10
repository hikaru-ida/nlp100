import sys

with open(sys.argv[1], 'r') as f:
    i = 0
    for line in f:
        print(line.strip())
        i += 1
        if int(sys.argv[2]) <= i:
            break
