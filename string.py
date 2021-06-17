s = 'AABCAAADA'
k = 3
n = len(s)
i = 0

a = set()
for i in range(0,len(s),k):
    a = s[i:i+k]
    t= []
    for y in a:
        if y not in t:
            t.append(y)
    print("".join(t))
