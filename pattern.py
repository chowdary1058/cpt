'''n=5
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
for i in range(n):
    for j in range(i):
        print("*", end="")
    print()
for i in range(n):
    for j in range(n - i):
        print("*", end="")
    print()'''
'''for i in range(1,n):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(n,0, -1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()'''
'''n=370
b=0
for i in str(n):
    x=int(i)**3
    b+=x
if b == n:
    print("am no")
else:
    print("not am no")'''
#hallow square pattern
'''for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#pascal pattern 
'''n=5
for i in range(1,n):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        b=1
        b+=j
        print(b, end="")
    print()'''
'''x, y, z = "", "python", 0
print((x or y) and (z or len(y)))'''
'''x = 5
x = x + 2.0
x = str(x) + "3"
x = x * 2
x = [x]
x = x + [10]
print(x)
print(type(x))'''
'''[[[s = 0
i = 0
while i < len(data):
    j = 0
    while _________:
        if data[i][j] % 2 == 0 and data[i][j] > 3:
            s += data[i][j]
        j += 1
    i += 1
print(s)]]]'''
'''t = (5, [10, 20], (30, [40, 50], (30,)))
#t[1].append(25)(tuple)
#t[2] += (60,)(list)
#t[2][0] = 35(list)
#t[2][2].append(60)(tuple dont has append)
t[2][1][0] = 4
print(t)'''
'''if x:
    print('x')
else:
    if y:
        if z:
            print('z')
        print('y')
    else:
        print('none')'''
'''for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 2):
            if i == j:
                print("-")
            else:
                print("*", end=" ")
        print("+")'''
'''for i in range(1, 5):
    for j in range(1, 5):
        if j == 3:
            break
    if i == 2:
        continue
    print(i, j)'''
P = {1, 2, 3, 4}
Q = {3, 4, 5, 6}
R = {4, 5, 6, 7}
S = {2, 4, 6, 8}
result = ((P | Q) - R) & S
print(result)