#if __name__ == '__main__':

##n = int(input())
##s = set(map(int, input().split()))
if __name__ == '__main__':
    n, m = map(int,input().split())
    a = set(map(int,input().split()))  
    A= set(map(int,input().split()))
    B= set(map(int,input().split()))
    print(sum((i in A)-(i in B) for i in a))        
    
    
    
