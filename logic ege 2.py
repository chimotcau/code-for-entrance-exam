print ('x y w z') 
k = 0, 1         
for x in k:
  for y in k:
    for w in k:
      for z in k:
         if  ((x and y)or(y and z))==((x<=w) and (w<=z)):
         
          print(x, y, z, w) 
          #answer: xwzy
