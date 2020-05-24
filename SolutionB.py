from itertools import combinations

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

x = int(input())
s = int(input())
y = int(input())
m = int(input())
z = int(input())
c = int(input())
twice = input().lower().split()
once = input().lower()

easy = list(combinations(alpha[:x], s))
medium = list(combinations(alpha[x:y+x], m))
hard = list(combinations(alpha[y+x:z+y+x], c))

a = len(list(easy))
b = len(list(medium))
e = len(list(hard))
result = a*b*e
print(result)

take1 = alpha[:x]
take2 = alpha[x:y+x]
take3 = alpha[y+x:z+y+x]

if once in take1:
    take1.remove(once)
if once in take2:
    take2.remove(once)
if once in take3:
    take3.remove(once)

easy = list(combinations(take1, s))
medium = list(combinations(take2, m))
hard = list(combinations(take3, c))

a = len(list(easy))
b = len(list(medium))
e = len(list(hard))

result = a*b*e

i = 0
j = 0
k = 0

for z in twice:
    if z in take1:
        i += 1
        take1.remove(z)
    if z in take2:
        j += 1
        take2.remove(z)
    if z in take3:
        k += 1
        take3.remove(z)

easy = list(combinations(take1, s - i))
medium = list(combinations(take2, m - j))
hard = list(combinations(take3, c - k))

a = len(list(easy))
b = len(list(medium))
e = len(list(hard))

print(result - a*b*e + 1)

