import os
n = 0
while n<5:
    val =os.system('curl -vL "http://127.0.0.1"')
    print(val)
    n+=1
