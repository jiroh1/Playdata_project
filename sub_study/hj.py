# #for문
# for i in range(11):
#     print(i)
# #while 조건문
# #실행문
# print("============================")
# i=1
# while i<11:
#     i+=1
#     print(i)
# print("===============")
# print("for문")
# a=[10,22,32,41,51]
# for i in range(len(a)):
#     print(a[i])
# #list 사용해서 할떄는 len을 써서 하는 것을 적극권유
# print("===============")
# print("while문")
# i=0;
# while i<len(a):
#     print(a[i])
#     i+=1
# print("================")
# print("홀짝")
#number = [11,2,6,9,25,7,3,23]
# dbl=[]
# odd=[]
# for i in range(len(number)):
#     if number[i] % 2 == 0:
#         dbl.append(number[i])
#     else:
#         odd.append(number[i])
# print("짝수 :" + str(dbl))
# print("홀수 :" + str(odd))
# print("총합")
#
# hap=0;
# for i in range(len(number)):
#     print(hap, number[i], end=' ')
#     hap+=number[i];
#     print(hap)
number = [11,2,6,9,25,7,3,23]
# 1번 방법
# for i in range(len(number)):
#     print(str(number[i])+"는")
#     if number[i] % 2 == 0:
#         if number[i] %3 ==0:
#             pass
#         elif number[i] %2 ==0:
#             print("2의 배수입니다.")
#        # print("2의배수 입니다.")
#     if number[i] % 3 ==0:
#         print("3의배수 입니다.")
#        # print(number[i])
#         if number[i] %2 ==0:
#             print("2의배수이기도 하고요")
#     elif number[i] %2 ==0:
#         pass
#     else:
#         print("아무것도 아니에요~")

# 2번 방법
for i in range(len(number)):
    print(str(number[i])+"는")
    if number[i] % 2 == 0:
        print("2의배수 입니다.")
        if number[i] %3 ==0:
            print("3의 배수입니다.")
        elif number[i] %2 ==0:
            pass
    elif number[i] % 3 ==0:
        print("3의배수 입니다.")

    else:
        print("아무것도 아니에요~")