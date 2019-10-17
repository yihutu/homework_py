#conding:utf-8
height = int(input("height:"))
width = int(input("width:"))
num_height = 1
while num_height<=height:
    num_width = 2
    while num_width<=width:
        print("#",end="")
        num_width +=1
    print("#")
    num_height +=1

    
