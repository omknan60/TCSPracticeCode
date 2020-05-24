N = int(input())
T = int(input())
P = {}
for i in range(1,N+1):
    inp = [int(x) for x in input().split()]
    P[i] = inp

for x in P:
    for i in range(T):
        P[x][i+1] = P[x][i+1] + P[x][i]
print(P)
for x in P:
    P[x] = P[x] * P[x][-1]

winners = []
for i in range(1,T+1,2):
    max = 0

    for k in P:
        if P[k][i] >= max:
            max = P[k][i]
    for k in P:
        if P[k][i] == max:
            winners.append(k)

result = {}

for i in range(1,N+1):
    for k in winners:
        if i == k:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
max = 0
tkey = 0
for i in result:
    if result[i] > max:
        max = result[i]
        tkey = i

print(tkey)







