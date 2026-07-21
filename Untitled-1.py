'''print("sai")
print(r"\tcurent\nnew\ffolder")
#odd or evn 
def oe(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(oe(4))
l=[1,2,3,4,5]
print(l[0:3])
print(l[2])
l.pop(1)
print(l)
dict={
    "name" : "sai  kishore ",
    "gender": "male",
    "age": 22,
    "course": "python"
}

dict.update({"age": 23})
print(dict)
dict["name"] = "kanna"
print(dict)
'''

'''def co(*args):
    print(type(args))
co(1,2,3,4,5)
def di(**kargs):
    print(type(kargs))
di(name="sai", age=22)
def defa(gender, age=22):
    print(gender, age)
'''
'''l=[1,2,3,4,5]
s="string"
len(l)
len(s)'''
'''x="vijay"
a=x[1:len(x)-1]
print(a[::-1])'''
'''x="vijay"
print(x[1:len(x)-1][::-1])'''

'''while True:
    print("hello")
    break'''
'''x=int(input())
b=0
for i in range(1,x+1):
    b+=i
print(b)
    
x=int(input())
b=0
while x>0:
    b += x
    x -= 1
print(b)'''


"""
value error
type error
index error
key error
"""
'''x=int(input())
y=int(input())
try:
    print(x/y)
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
except ValueError as e:
    print("ValueError", e)
finally:
    print("finally block executed")'''
'''for i in range(5):
    print(i)
    if i == 4:
        break
        print(i)
    else:
        print("done ")'''
'''try:
    a=int(input())
    print(a)
except ValueError as e:
    print("ValueError", e)
else:
    print("no error")'''
#to throw error 
a=int(input())
if a<0:
    raise ValueError("a should be positive")
else:
    print(a)