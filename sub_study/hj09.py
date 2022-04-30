my_lst = [1,2,3,4,5]
str_lst=['a','b','c','d','e','f']

print(my_lst,str_lst)
#형식 -> del my_lst[index]
#del 예약어 (함수 x) -->my_lst.remove : remove는 함수 , my_lst.del(x, 이렇게 쓸 수 없다.)
del my_lst[4]
print(my_lst)
del str_lst[4]
print(str_lst)

del str_lst[2:]
print(str_lst)

str_lst.remove('b')
print(str_lst)


for i in range(0, len(my_lst)):
    print(my_lst[i])