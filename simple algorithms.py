def F( x,y,h):
    if x +y >= 20 and h == 3:
        return True
    if x + y <84 and h ==3:
        return False
    return F(x+1,y,h+1) or F(x,y+1,h+1) or F(x*2,y,h+1) or F(x,y*3,h+1) 
for s in range(1,68):
    if F(16,s,1) == True:
        print(s)
        break               

            

