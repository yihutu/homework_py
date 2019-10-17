#conding:utf-8
num1 =1
while num1 <=9:
    num2 = 1
    while num2 <= num1:
        print(str(num2) + "*" + str(num1) + "=" + str(num2*num1),end="\t")  ##\t是制表符，\n是换行符
        num2 +=1
    print()
    num1 +=1
