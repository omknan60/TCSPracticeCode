N = int(input())
T = int(input())
P = {}
for i in range(1,N+1):
    inp = [int(x) for x in input().split()]
    P[i] = inp
G = {}
for x in P:
    G[x] = []
    for i in range(0, T):
        G[x].append(sum(P[x][:i+1])*P[x][-1])

winners = {}
for k in G:
    winners[k] = 0
for i in range(1,T+1,2):
    max = 0
    for k in G:
        if G[k][i] > max:
            max = G[k][i]
    for k in G:
        if G[k][i] == max:
            winners[k] += 1

result = 0
mx = 0
for k in winners:
    if winners[k] > mx:
        result = k
        mx = winners[k]

print(result)






