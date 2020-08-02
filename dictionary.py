# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }
# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))
# =============================================
# Dict = {
#        'ball' : 'green',
#        'ball': 'red'
#     }
# print(Dict['ball'])
# print(Dict['ball'])
# print(Dict['bat'])
# ================================================
# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{
#      'A' : 'WELCOME',
#      'B' : 'To', 
#      'C' : 'DHARAMSALA'
#      }
# }
# print(Dic[3]["B"])
# ===================================================
# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# ====================================================
# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])
# print(person[4])
# result = person[4]['place']
# print(result)
# ======================================================
# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)
# ======================================================
# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person)
# =======================================================
# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }

# del person['place']
# print(person)
# ========================================================
# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#   	print(state)
# =========================================================
# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
#     }
    
# for state in states_capitals:
#     print(states_capitals[state],":",state)
# =========================================================
# details ={
# 	"name":  "Bijender",
# 	"age":  17,
# 	"class":  "10th"
# 	}
# for x in details.values():
# 	print(x)
# ============================================================
# movie ={
# 	"name":  "Puli",
# 	"hero":  "Vijay",
# 	"rating":  7.5
# 	}
# for x,y in movie.items():
# 	print(x,y)
# ==========================================================
# meal ={
# 	"monday":  "Chole chawal",
# 	"sunday":  "Fried rice",
# 	"wednesday":  "dosa"
# 	}
# print(len(meal))
# ===========================================================
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.items()
# print(x)
# # ==========================================================
# def checkKey(key): 
#     if key in dict.keys(): 
#         print("Present, ", end =" ") 
#         print("value =", dict[key]) 
#     else: 
#         print("Notmy_list present") 
# dict = {'a': 100, 'b':200, 'c':300}
# checkKey("b")
# ======================================================
# append:-
# a = [1]
# x = 5
# a[len(a):] = [x]
# print(a)
# ===================================
# iter on tupels:-
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# =================================
# find index:-
# list.index(x[, start[, end]])
# ======================
# iteritems:-
# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }
# for i in city_population.iteritems(): 
#     print(i) 
# ===================================
# copy:-
# a = [1,2,3]
# b = a[:]
# print(b)
# # ==============================
# delet list:-
# a = [1,2,3]
# del a[:]
# print(a)
# =============================
# pop the last element:-
# a = [1,2,3]
# a.pop()
# print(a)
# =============================
# squares = []
# for x in range(10):
#     square[len(square):] = [x**2]
# print(square)
# ==============
# squares = list(map(lambda x: x**2, range(10)))
# print(squares)
# ===================
# squares = [x**2 for x in range(10)]
# print(squares)
# =====================
# a = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(a)
# ========================
# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)
# ===========================
# vec = [-4, -2, 0, 2, 4]
# a = [x*2 for x in vec]
# print(a)
# a = [x for x in vec if x >= 0]
# print(a)
# a = [abs(x) for x in vec]
# print(a)
# =============================
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# a = [weapon.strip() for weapon in freshfruit]
# print(a)
# =====================
# a = [(x, x**2) for x in range(6)]
# print(a)
# ==========================
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# a = [num for elem in vec for num in elem]
# print(a)
# =======================
# from math import pi
# a = [str(round(pi, i)) for i in range(1, 6)]
# print(a)
# ============================
# matrix = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9, 10, 11, 12],
#  ]
#  =======
# a = [[row[i] for row in matrix] for i in range(4)]
# print(a)
# =======
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)
# =========
# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)
# =========================
# def myFun(**kwargs):  
#     for key, value in kwargs.items(): 
#         print ("%s == %s" %(key, value)) 
# myFun(first ='Geeks', mid ='for', last='Geeks')     
# ===========================
# def myFun(*argv):  
#     for arg in argv:  
#         print (arg) 
    
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# ==================
# def myFun(**argv):  
#     for arg in argv:  
#         print (argv[arg]) 
    
# myFun(arg1="Geeks", arg2="for", arg3= "Geek")
# # ================================
# a = ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# print(a[0][1])
# ====================================
d ={ 
  "fantasy": "harrypotter", 
  "romance": "me before you", 
  "fiction": "divergent"
  } 
print(d.items())
# a = iter(d)
# print(next(a))
# print(next(a))
# print(next(a))
