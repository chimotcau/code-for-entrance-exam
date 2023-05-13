import math 
b=0
def f(n):
    if int(math.sqrt(n))**2==n:
        return True 
    return False    
for i in range(2,1000):
    a=[]
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            a.append(j)
            b=i//j
            if j!=b:
                a.append(b)
    if len(a)==3:
        a.sort()
        print(i,a[1])            