'''with open("file.txt", "w") as file:
    file.write("Hello, World!")
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
with open("file.txt", "a") as file:
    file.write("\nThis is an appended line.")
with open("file.txt", "r") as file:
    content = file.read()
    print(content)'''
    
while True:
    try:
        number = int(input())
        print(number)
        break
    except ValueError:
        print("Error: enter integer.")
        '''
n= [10, 20, 30, 40, 50]

try:
    print(n[5])
except IndexError:
    print("error:index out of range")'''
        