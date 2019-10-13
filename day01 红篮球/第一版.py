# 习题讲解
# 双色球
# 先让用户依次选择6个红球（红球的选择范围是1-32）
n = 0
s1 = ''
while n < 6:
    num1 = input('请输入红球的号码 :')
    num = int(num1)
    if num <= 32 and num >= 1:
        print('您选择了红球',num1)  # '23' ,'24'
        n = n + 1
        if n < 6:
            s1 = s1 + num1 +','  # '23,'+'24'+',' = '23,24,25,26,27,'
        else:
            s1 = s1 + num1    # '23,24,25,26,27,'+'28'
    else:
        print('请选择1-32之间的数字')
m = 0
s2 = ''
while m < 2:
    num2 = input('请输入蓝球的号码 ：')
    num = int(num2)
    if num <= 16 and num >= 1:
        print('您选择了蓝球', num2)
        m = m + 1
        if m<2:
            s2 = s2 + num2 + ','  # 除最后一个数字以外的拼接
        else:
            s2 = s2 + num2   # 最后一个数字的拼接
    else:
        print('请选择1-16之间的数字')
print('您选择的红球有 ：',s1)
print('您选择的蓝球有 ：',s2)