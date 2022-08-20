import math
import os
import random
import re
import sys
# Complete the 'theLoveLetterMystery' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as paramete
def theLoveLetterMystery(s):
    # Write your code here
    al = 'abcdefghijklmnopqrstuvwxyz'
    r_s = s[::-1]
    c = 0
    for i in range(len(s)//2):
        c += abs(al.find(s[i]) - al.find(r_s[i]))
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        fptr.write(str(result) + '\n')
    fptr.close()