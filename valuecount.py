dic ={
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2',"subj3"]
    }
count = 0
for i in dic:
    for j in range(len(dic[i])):
        count = count + 1
print(count)