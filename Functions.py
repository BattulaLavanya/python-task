print('print msg using functions')

def msg():
   print('Hello')
   print('Good Evening')
msg()

print("---"*7)
print('Add 2 numbers using Functions')

def add():
    x = 10
    y = 20
    z = x+y
    print('Sum : ',z)
add()
print("---"*7)
print('Print even or odd number')

def even_odd():
    x=5
    if x%2==0:
        print('Number is even')
    else:
        print('Number is Odd')

even_odd()
print("---"*7)
print('functions with paramerts and without return values')

def add(x,y):
    z = x+y
    print('sum :', z)
m = 11
n = 12
add(m,n)
print("---"*7)


