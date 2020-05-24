n = int(input())
s = input()
q = int(input())

result = []
for i in range(q):
    a = int(input())
    count = 0
    for x in s[:a-1]:
        if x == s[a-1]:
            count += 1
    result.append(count)
print()
for i in result:
    print(i)