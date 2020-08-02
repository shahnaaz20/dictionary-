my_dict = {
    'a':58, 
    'b':5, 
    'c':560,
    'd':40, 
    'e':100, 
    'f':200
    }
my_list=[]
for i in range(3):
    max_1 = 0
    for key in my_dict:
        if max_1 < my_dict[key]:
            max_1=my_dict[key]
            i = key
    my_list.append(i)
    del my_dict[i]
print(my_list)
    