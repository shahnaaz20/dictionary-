def remove(index):
   del dics[index]

dics = [{"a":2},{"b":34},{"b":23}]
def check(key):
   list1 = list(key)
   list1 = list1[0]
   value = key[list1]
   # print(value)
   # print(list1)
   for i in range(1,len(dics)):
      list2 = list(dics[i])
      list2 = list2[0]
      value1 = dics[i][list2]
      if list1 == list2:
         print(value1)
         remove(i)


listn = []
def dic(d):
   for sub_dic in d :
      check(sub_dic)
dic(dics)

