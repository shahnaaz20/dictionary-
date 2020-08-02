my_dic = {}
i = 0
while i < 10:
    name = input("eneter the name: ")
    marks = int(input("enter marks: "))
    dic = {name:marks}
    my_dic.update(dic)
    i = i + 1
print(dic)
