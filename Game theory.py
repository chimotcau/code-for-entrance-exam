count = answer = 0
f = open('17.txt')
a = [int(i) for i in f]
for j in range(len(a)-1):
    for k in range(j+1,len(a)):
        if ((a[j]-a[k])%60 ==0):
            count += 1
            answer = max(answer, a[j]-a[k])
print (count,answer)
#answer: 832722 9960        