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
n=5
for i in range(1,n):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        b=1
        b+=j
        print(b, end="")
    print()