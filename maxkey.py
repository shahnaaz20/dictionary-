my_dict= {"a":10,"b":8,"c":3,"d":4}
max_1 = 0
for i in my_dict:
    if max_1<my_dict[i]:
        max_1 = my_dict[i]
        key = i
print(key)

