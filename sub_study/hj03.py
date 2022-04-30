# 문장 안에서 t의 개수를 출력해라
my_first_string = "In type annotations you can now use built-in collection types such as list " \
                  "and dict as generic types instead of importing the corresponding capitalized types (e.g. List or Dict) from typing. " \
                  "Some other types in the standard library are also now generic, for example queue.Queue."

lst = []
res = my_first_string

for i in res:

    if i == "t":
        lst.append(i)
        print(i)
        print(lst)
        lst.count(i)
        anw = lst.count(i)

# a = [[10, 20], [30, 40], [50, 60]]
# '''
# 출력형식
# 10 20
# 30 40
# 50 60
# '''
# for i in a: # i = [[10, 20], [30, 40], [50, 60]]
#     for j in i: #j = [10, 20]
#         print(j,end=' ')
#     print()

'''
*
**
***
****
*****
'''

# for i in range(1,6):
#     for j in range(i):
#         print(j)
#         print('*', end='')
#     print()

'''
00000
0
00000
0
00000
# '''
for i in range(5):
    if i % 2 ==0:
        for _ in range(5):
            print(0,end='')
        print()
    else:
        print(0)
'''
00000
    0
00000
    0
00000
'''
for i in range(5):
    if i % 2 ==0:
        for _ in range(5):
            print(0,end='')
        print()
    else:
        print('    0')

for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            print(0, end='')
        else:
            if j == 0:
                print(0, end='')
            elif j == 4:
                print(0, end='')
            else:
                print(end=' ')
    print()

for i in range(1,6):
    for j in range(1,6):
        if i % 2 ==0:
            print("0",end="")
            break
        else:
            print("@", end='')
    print()

'''
  12345     = j
1 00000
2 0
3 00000
4 0
5 00000
"
i
'''

for i in range(5):
    if i % 2 == 0:
        for _ in range(5):
            print(0, end='')
        print()
    else:
        print(0)

#
if __name__ == '__main__':
    print(anw)
     #print(my_first_string.count(i))