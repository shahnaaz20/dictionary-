string = "MISSISSIPPI"
i = 0
my_dic = {}
while i < len(string):
    j=0
    count = 0
    while j < len(string):
        if string[i]==string[j]:
            count += 1
        j = j + 1
    dic = {string[i]:count}
    my_dic.update(dic)
    i = i + 1
print(my_dic)

    