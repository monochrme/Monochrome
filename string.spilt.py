#用户输入两个参数，中间用‘，’分开，前一个参数作为需要居中的对象，第二个参数是填充对象
string=input("输入两个字符，中间用‘，’分隔，用于字符串布局：")
a=string.split(',')        #利用字符串内置方法.split将输入分割为两部分
print(a)                      #打印看下实际a的效果
c=ord(a[1])                  #尝试用ord函数调取unicode
print(c)                        #调取C的unicode
print("输出结果：{0:c^20}".format(a[0]))    #未达到第二个参数是填充对象的效果。why?
