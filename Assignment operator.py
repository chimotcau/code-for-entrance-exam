def f(x,y):
    if x==y :
        return 1
    if x>y :
        return 0
    if x<y:
        return f(x+1,y) + f(x+3,y)
print(f(1,8)*f(8,15))
#answer:  30