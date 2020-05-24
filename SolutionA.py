"""Solution for Problem A"""

N = int(input())

result: list = []

for i in range(N):
    inp = [int(x) for x in input().split()]
    result.append(inp)
print()

def tie_breaker(i, k, a, b, table):
    A = table[i+1][k]
    B = table[i][k+1]
    C = table[a+1][b]
    D = table[a][b+1]
    if A<C and A<D or B<C and B<D:
        return [i, k]
    if C<A and C<B or D<A and D<B:
        return [a, b]


def exit_code(N, result):

    S = 0
    i = 0
    k = 0

    while True:
        if i == N-1 and k != N-1 :
            A = result[i][k+1]
            S = S//2 + A
            k = k+1


        if k == N-1 and i != N-1:
            A = result[i+1][k]
            S = S // 2 + A
            i = i+1


        if i != N-1 and k != N-1:
            A = result[i + 1][k]
            B = result[i][k + 1]
            SA = S // 2 + A
            SB = S // 2 + B
            if SA < SB:
                S = SA
                i += 1
            if SB < SA:
                S = SB
                k += 1
            if SA == SB:
                i, k = tie_breaker(i + 1, k, i, k + 1, result)
                S = S // 2 + result[i][k]
        if i == N-1 and k == N-1:
            break

    return S

print(exit_code(N, result))