#if __name__ == '__main__':

#pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")        



import math
import os
import random
import re
import sys
import copy

n = int(input())
#k = [input().split() for _ in range(n-1)]
a = 0

for _ in range(1,n):
    a = (n*(n-1)%(10**9+7))
print(a//n)

