my_dict = {
    'a':50, 
    'b':58,
    'c':6,
    'd':40,
    'e':10, 
    'f':200
    }
my_list=[]
for i in range(3):
    max_1 = 0
    for key in my_dict:
        if max_1 < my_dict[key]:
            max_1=my_dict[key]
            i = key
    my_list.append(max_1)
    del my_dict[i]
print(my_list)
    