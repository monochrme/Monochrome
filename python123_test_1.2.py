#python123.io +-*/
num=input()
for i in range(len(num)-1):
    if num[i+1] in ['+']:
        ans=num.split('+')
        ans1=eval(ans[0])+eval(ans[1])
        print("{:.2f}".format(ans1))
    elif num[i+1] in ['-']:
        ans=num.split('-')
        ans1=eval(ans[0])-eval(ans[1])
        print("{:.2f}".format(ans1))
    elif num[i+1] in ['*']:
        ans=num.split('*')
        ans1=eval(ans[0])*eval(ans[1])
        print("{:.2f}".format(ans1))
    elif num[i+1] in ['/']:
        ans=num.split('/')
        ans1=eval(ans[0])/eval(ans[1])
        print("{:.2f}".format(ans1))

