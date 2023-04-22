import itertools
alphabet = "ABCDE"
ar = itertools.product(alphabet, repeat=5) #Размещение с повторением
arl = []

for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    if e[0] != 'B'and e[-1]!= 'A' :
        count += 1
print(count)