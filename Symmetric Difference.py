
def insert_set(a):
    i=0
    if i<=a:
        b= input().split()
        c= set(map(int,b))
    return c

m = int(input('number of integers m:' ))
a= insert_set(m)
n = int(input('number of integers n:' ))
b = insert_set(n)
c=a.symmetric_difference(b)
for i in c:
    print(i)


##number of integers m:4
##2 4 5 9
##
##number of integers n:4
##2 4 11 12
##

a = {9, 2, 4, 5}
b={2, 11, 4, 12}
