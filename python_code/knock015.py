import sys

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

ls_size = len(lines)
for i in range(int(sys.argv[2]), 0, -1):
    print(lines[ls_size - i].strip())
