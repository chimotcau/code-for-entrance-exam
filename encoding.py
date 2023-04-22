a = {0: "Л", 1: "Н", 2: "Р", 3: "Т"}
k = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for m in range(0, len(a)):
                for n in range(0, len(a)):
                    k += 1
                    if k == 150:
                        print(a[i], a[j], a[g], a[m], a[n], end=" ")