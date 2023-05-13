from functools import lru_cache
@lru_cache(None)
def f(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return f(n-2)+f(n-1)
for i in range(2,2222):
    f(i)    
print (f(2022)/f(2002)) 
#answer:34       
