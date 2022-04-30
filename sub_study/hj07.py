import numpy as np

np.random.seed(1)
myArr = np.random.randint(1,30,16).reshape(4,4)
print(myArr)
for i in range(len(myArr)):#0,3
    for j in range(len(myArr[i])): #len(myArr[0])) ->4 j=0,3
        if myArr[i][j] ==8: #myArr[0][0]
            print("8의 위치",i,',',j)

print(np.where(myArr==2))

for i in range(len(myArr)):#0,3
    for j in range(len(myArr[i])): #len(myArr[0])) ->4 j=0,3
        if myArr[i][j] %2 ==0: #myArr[0][0]
            print(myArr[i][j],"는 짝수")
        else:
            print(myArr[i][j], "는 홀수")

print('*' *30)
#각 컬럼 별 합이 짝수인지 홀수 인지

for i in myArr:
    total = 0
    for k in i:
        total += k
    if total %2 ==0:
        print(total, "짝수")
    else:
        print(total,"홀수")
print('*' *30)

for i in myArr:
    for k in i[2:]:
        print(k,end=' ')
    print()
print('*' *30)

for i, v in enumerate(myArr):#  [ 6 12 13  9],  [10 12  6 16],  [ 1 17  2 13], [ 8 14 29  7]
    total = 0
    for j in v: #[10 12 6 16]
        total += j
    if total % 2 ==0:
        print(i, "번째 row의 합은", total,"이고, 짝수입니다.")
    else:
        print(i, "번째 row의 합은", total, "이고, 홀수입니다.")

print('*' *30)

odd_row_total = 0
even_row_total = 0
for i, v in enumerate(myArr):#  [ 6 12 13  9],  [10 12  6 16],  [ 1 17  2 13], [ 8 14 29  7]
    total = 0
    for j in v: #[10 12 6 16]
        total += j
    if i % 2 ==0:
        odd_row_total += total
    else:
        even_row_total += total
print("홀수 줄의 합:",odd_row_total,"짝수 줄의 합:",even_row_total)
print('*' *30)
print(myArr)
print('*' *30)


for i in range(len(myArr)): # i = 0,1,2,3
    #print(i)
    hap = 0
    for k in range(len(myArr[i])): # j = 0,1,2,3
        #print(type(myArr[k][i]))
        #print(myArr[k][i])
        hap += myArr[k][i]
    print(i,"번째열의 합은",hap)
    # pass
        # continue
    #     #print(myArr[i][k])
    #     #print(myArr[i])
#print('**')
#print("다음열")
print('*'*30)
for i ,v in enumerate(myArr):
    print(i,v)
    for k,j in i,v:
        print(k,j)
        # hap += myArr[]


# for i in myArr:
#     for j in i:
#         if j == '8':
#             print(j)
        # for k in j:
        #     if k == '2':
        #         print(myArr[k])
#     list.append(i)
# print(list)
#arr = np.random.randn(4,4)
# [print(arr,"!!!!")
# for i in myArr:
#     print(i)]
