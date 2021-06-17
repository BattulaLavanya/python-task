#if __name__ == '__main__':

n = int(input())
count = 0
a = []
va = []
for i in range(0,n):
    a=input()
    va.append(a)
    count+=1
print(len(set(va)))
