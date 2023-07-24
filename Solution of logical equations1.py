count=0
for a in range (300,0,-1):
    b=0
    for x in range (0,200):
        for y in range(0,200):
            if ((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6)):
                b+=1
    if b==40000:
        print(a)
       
#answer:23