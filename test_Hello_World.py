#hello world.py/python123.io answer
num=input("请输入一个整数：")
data="Hello World"
if eval(num)==0:
    print("Hello World")
elif eval(num)>0:
    for i in range(len(data)):
        m=data[i]
        print(m,end="")
        n=i%2
        if n==1:
            print("\n",end="")
else :
    for i in range(len(data)):
        m=data[i]
        print(m)
