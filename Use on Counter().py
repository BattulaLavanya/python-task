from collections import Counter

a = [1,2,2,3,3,3,3,4]

counts = Counter(a)
print(a)
print('Counter(a)= ',counts)
print('counts[2]= ', counts[2])
print('counts[3]= ', counts[3])
print('counts[10]= ',counts[10])#non exist numb
print('counts.keys()= ',counts.keys())
print('counts.values()= ',counts.values())
counts[1] = 5 # change of existing numb in the list
print('change of existing numb= ', counts, counts[1])
del counts[1]
print('del counts[1]= ', counts)# delete exising numb form list
x = list(counts.elements())
print('list(counts.elements()= ',x)
y = counts.most_common(2)
print('y = counts.most_common(2)= ',y)
print('y[0]= ',y[0])
print('y[0][1]= ',y[0][1])
a2 = [5,5,6,6,6,7,7,4,4,4]
print(a2)
count2 = Counter(a2)
print('count2 = Counter(a2): ',count2)
z = counts + count2
print('z=counts + count2:-',z)
b = counts - count2
print('b=counts - count2:-',b)


    
