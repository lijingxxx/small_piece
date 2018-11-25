import sys
args = sys.argv
max = args[1]
for n in range(2,len(args)):
    if max < args[n]:
        max = args[n]

print(max)        