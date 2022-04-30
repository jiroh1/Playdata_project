# def combine_list(a):
# #    print(a, "string")
#   for i in a:
#     # print(i, end=' ')
#     # print(i)
#     return i
#
# def prn(i): # 위에서 만든 것을 단순 출력하는 함수
# #    print(a)
#     return i
#
# if __name__ == '__main__':
#     string_list = ['Hi', 'My', 'name', 'is', 'HJ']
#     #함수 호출
#     prn()
#     print(prn(string_list), end =' ')

# def combine_list(str_list):
#                 # 바꿔줄 데이터 타입, 리스트, 튜플
#     my_str = ' '.join(map(str, str_list)) # ' ' 이부분은 형식
#     prn(my_str)
#
# def prn(combine_str):
#     print(combine_str)

# def my_function(se):
#     for i in se:
#     #    print(i)
#         #print(i)
#         if len(i)>=5:
#             print(i)
#         else:
#             pass
def upp_s(i):
    upp = i.lower()
    return upp
def low_s(i):
    low = i.upper()
    return low
def prn_s(k):
    lst = []
    for i in k:
        if i.isupper() == True:
            #upp_s(i)
            #print(upp_s(i))
            lst.append(upp_s(i))
        elif i.islower() == True:
            #low_s(i)
            lst.append((low_s(i)))
    print(lst)
if __name__ == '__main__':
#     # string_list = ['Hi', 'My', 'name', 'is', 'HJ']
#     # combine_list(string_list)
#    q2 = ["nice","study","python","annaconda","!"]
#    my_function(q2)

    q3 = ['A','B','c','D','e','F','G','h']
    prn_s(q3)