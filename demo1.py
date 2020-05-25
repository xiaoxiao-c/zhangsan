
def panduan(acount,password):
    """
    实现判断账号，密码。
    """
    if len(acount)<5 or len(acount)>8:
            print("请输入账号长度为5-8")
    else:
        if acount[0] in "qwertyuioplkjhgfdsazxcvbnm":
            print("您账号输入正确")
            if len(password)<12 or len(password)>6:
                return "注册成功！"
            else:
                print("您输入的密码长度不是6-12位")
        else:
                print("您输入的账号首字母不是小写")


print(panduan("a12345","802380"))

