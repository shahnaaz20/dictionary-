my_dict = {
    'a':50, 
    'b':50,
    'c':50,
    'd':10,
    'e':10, 
    'f':200
    }
unique_values=[]
for key in my_dict:
    if my_dict[key] not in unique_values:
        unique_values.append(my_dict[key])
    else:
        print(key

