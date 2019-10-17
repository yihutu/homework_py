#conding:utf-8
num1 = input("num1:")
num2 = input("num2:")
num3 = input("num3:")
if num1>num2:
    max = num1
    if max > num3:
        print("max is",max)
    else:
        print("max is",num3)
else:
    max = num2
    if max > num3:
        print("max is",max)
    else:
        print("max is",num3)
