"""
for i in range(0,31):
    print("红灯还有",30-i,"秒")
for i in range(0,36):
    print("绿灯还有",35-i,"秒")
for i in range(0,6):
    print("黄灯还有",5-i,"秒")
    """
name={}
acount=input("请输入账号以小写字母开头，5-8长度:")
password=input("请输入密码，长度为6-12位:")
if len(acount)<5 or len(acount)>8:
    print("请输入账号长度为5-8")
else:
    if acount[0] in "qwertyuioplkjhgfdsazxcvbnm":
        print("您账号输入正确")
        if len(password)<12 or len(password)>6:
            print("注册成功！")
        else:
            print("您输入的密码长度不是6-12位")
    else:
        print("您输入的账号首字母不是小写")
    

