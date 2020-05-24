T = int(input())

came = {}
for i in range(T):
    c = []
    c.append(input())
    c.append(input())
    came[i] = c

for i in came:
    result = ""
    for x in came[i][0]:
        if x in came[i][1]:
            result = result + x
    print(result)