N = int(input())
re = int(input())
hun = int(input())
thun = int(input())
fhun = int(input())
thou = int(input())
T = N
total = 0
if thou<N:
    total = total + thou*1000
    N = N - thou
else:
    total = total + N*1000
    N = 0
if fhun <= N:
    total = total + fhun*500
    N = N - fhun
if thun <= N:
    total = total + fhun*200
    N = N - thun
if hun < N:
    total = total + hun * 100
else:
    total = total + N * 100


hn = 0
thn = 0
fhn = 0
tn = 0

while re >= 1000:
    re = re - 1000
    thou -= 1
    tn += 1
while re >= 500:
    re = re - 500
    fhun -= 1
    fhn += 1
while re >= 200:
    re = re - 200
    thun -= 1
    thn += 1
while re >= 100:
    re = re - 100
    hun -= 1
    hn += 1

while tn > 0:
    if fhun >= 2:
        tn -= 1
        thou += 1
        fhun -= 2
        fhn += 2
    else:
        break

while fhn > 0:
    if thun >= 1 and hun >= 3:
        fhn -= 1
        fhun += 1
        thun -= 1
        thn += 1
        hun -= 3
        hn += 3
    elif thun >= 2 and hun >= 1:
        fhn -= 1
        fhun += 1
        thun -= 2
        thn += 2
        hun -= 1
        hn += 1
    else:
        break

while thn > 0:
    if hun >= 2:
        hun -= 2
        hn += 2
        thn -= 1
        thun += 1
    else:
        break

while hn+thn+fhn+tn > T:
    if thun > 0:
        hun += 2
        hn -= 2
        thun -= 1
        thn += 1
        if hn+thn+fhn+tn <= T:
            break

while hn+thn+fhn+tn > T:
    if fhun > 0:
        hun += 1
        hn -= 1
        thun += 2
        thn -= 2
        fhun -= 1
        fhn += 1
        if hn+thn+fhn+tn <= T:
            break

while hn+thn+fhn+tn > T:
    if thou > 0:
        thou -= 1
        tn += 1
        fhn -= 2
        fhun += 2
        if hn+thn+fhn+tn <= T:
            break

print(hn+thn+fhn+tn)