
import sys


def sums(args):
    sum = 0
    for n in range(1,len(args)):
        sum = sum + int(args[n])
    return sum    

result = sums(sys.argv)
print(result)