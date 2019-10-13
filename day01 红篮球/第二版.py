# -- conding:utf8--
lst = []
n = 0
while n<6:
    redball = int(input('please enter redball num:'))
    if redball >0 and redball <=32 and redball not in lst:
        lst.append(redball)
        n+=1

    else:
        if redball in lst:
            print('您输入的数字已存在')
        else:
            print('请输入1-32之间的数字')
lst2 = []
m = 0
while m<2:
    blueball = int(input('please enter blueball num:'))
    if blueball > 0 and blueball <16 and blueball not  in lst2:
        lst2.append(blueball)
        m+=1
    else:
        if blueball in lst2:
            print('您输入的数字已存在')
        else:
            print('请输入1-16之间的数字')

print('您选择了红球：',lst)
print('您选择了篮球：',lst2)