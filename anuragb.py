data = {}
list1 = [{"a":10},{"a":2},{"a":20},{"c":2},{"c":90},{"c":8},{"d":10}]
for i in list1:
    key = list(i.keys())[0]
    if key not in data:
        data[key]=i[key]
    else:
        data[key]=data[key]+i[key]
for key ,val in data.items():
    print (str(key) + "-" + str(val))
