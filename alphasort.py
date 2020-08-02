def alpha_sort(my_list):
    sort=[]
    for i in range(len(my_list)):
        minim = my_list[0]
        for i in my_list:
            if ord(minim[0])>ord(i[0]):
                minim=i
        sort.append(minim)
        my_list.remove(minim)
    return(sort)
my_dict = {1:["snaaz","naaz","zain"],2:["bad","good","ugly"],3:["kite","dog","tiger"]}
for i in my_dict:
    print(alpha_sort(my_dict[i]))
    
             
            

               
                


