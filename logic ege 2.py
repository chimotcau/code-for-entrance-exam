print ('x y w z') 
k = 0, 1         
for x in k:
  for y in k:
    for w in k:
      for z in k:
         if not  ((x and (not y)) or (y == z) or (not w)):
         
          print(x, y, z, w) 
          #answer: xwzy
