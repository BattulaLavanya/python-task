s ='banana'
word = ['a','e','i','o','u']
a = 0;b = 0
for i in range(len(s)):
    if s[i] in word:
        a += (len(s)-i)
        print('a',a)
    else:
        b += (len(s)-i)
        print('b',b)
print(a ,'&', b)
