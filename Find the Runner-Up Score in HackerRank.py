#Given the participants' score sheet for your University Sports Day, you are
#required to find the runner-up score. You are given  scores. Store them in
#a list and find the score of the runner-up
import random
n = int(input())
arr = list(map(int,input().split()))
a= max(arr)
while max(arr) == a:
    arr.remove(max(arr))

print(max(arr))



#5
#2 3 6 6 5
#4
#57 57 -57 57
