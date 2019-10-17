#conding:utf-8
death_age = 80

name = input("your name:")
age = input("your age:")  ##input接收的所有数据都是字符串，即便输入的是数字也会当成字符串处理

print( type(age) )
##int insert = 整数   把字符串转成int，用int（被转的数据）
##str string = 字符串 把数据转成字符串用str(被转的数据)
print("your name:",name)
#print("your can still live for",str(death_age - int(age)),"years.....")  ##数字和字符串不能相加
#或print("your can still live for",death_age - int(age),"years.....")  ##数字和字符串不能相加

#print("your can still live for", + death_age - int(age), + "years.....")  ##报错，数字和字符串不能拼接

print("your can still live for", + str(death_age - int(age)), + "years.....")
