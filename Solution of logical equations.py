for a in range (1,101):
    c=0
    for x in range (1,101):
        if (x%45 == 0)and ((750 %x == 0)<=(a % x!=0)<=(120 %x!=0)):
            c+=1
            if c== 100:
                print (c)