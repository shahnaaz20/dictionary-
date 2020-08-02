my_dict={
    'bijender':45,
    'deepak':60,
    'param':20,
    "anjili":30,
    'roshini':50
    }
my_list={}
for i in range(len(my_dict)):
    max_1 = 0
    for key in my_dict:
        if max_1 < my_dict[key]:
            max_1=my_dict[key]
            i = key
    my_list.update({i:max_1})
    del my_dict[i]
print(my_list)
    