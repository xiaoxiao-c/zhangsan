b={}
"""a["name"]=input("请输入姓名")
a["sex"]=input("性别")
a["age"]=input("请输入年龄")
print("姓名",a["name"])
print("性别：",a["sex"])
print("年龄：",a["age"])
b.update(name=input("姓名"))
b.update(age=input("年龄"))
b.update(sex=input("sex"))
print(b)
print(b["name"]+b["age"])

a=1
b=3
if type(a) is int:
    print("数字")
else:
    print("不是数字")

a=1
while a<10:
    print("haha!!!!!!!!!")
    a=a+1
    """
hig60={}
low60={}
stulist=["车小晓","王2","李小","李平芳","车穿过"]
a=0
while a<5:
    grade=int(input("请输入"+stulist[a]+"的成绩"))
    if(grade>60):
        hig60[stulist[a]]=grade
    else :
        low60[stulist[a]]=grade
    a=a+1

print(hig60,low60)