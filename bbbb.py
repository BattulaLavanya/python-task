keys=[]
values=[]
n = int(input('Enter number of elements to store into dict : ')
##for x in range(1,n+1):
##	element=int(input("Enter Key"+ str(x)":"))
##	keys.append(element)
for x in range(1,n+1):
	element=int(input("Enter value"+str(x)+":"))
	values.append(element)
d=dict(zip(keys,values))
print("The Dic is :", d)


