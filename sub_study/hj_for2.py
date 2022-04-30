# for i in range(1,10):
#     for j in range(1,10):
#         print(i, "*", j, "=", i*j)
#-------------------------------------------
# a = [[1,2], [3,4], [5,6]]
# for i in range(len(a)):
#     #print(i)
#      for j in range(len(a[i])):
#          print(a[i][j])

# for i in range(1, 11):
#     print(i)

#-------------------------------------------
# for i in range (1,6):
#    k = i.replcae(String (i),"*") , #replace 함수는 int는 안됨..
#     # for k in range(1,6):
#     #     print(k)

''' 1부터 입력된 수 n까지의 수 중에서 n의 짝수 첫번째 배열에, 홀 수 두번째 배열에 담아 출력하라 '''
lst1 = [] #홀수 배열
lst2 = [] #짝수 배열
# i = 1
n =50


def prn(n):  # public int (int n): java구문과 같은것임
   #명령문
#   print(n)
   lst1 = []  # 홀수 배열
   lst2 = []  # 짝수 배열
   for i in range(1, n+1): # n을 사용해야됨 그래서 n+1 = 51 / 51로 썼었음
      if i % 2 == 0 :
         lst2.append(i)
      else:
         lst1.append(i)

   print(lst1)
   print(lst2)

   return lst1,lst2

if __name__ == '__main__':
   n = 50
   odd_lst, even_lst = prn(n) # 이렇게 받아 가는 것이 형식
   print(prn(n))
   print(odd_lst)
   print(even_lst)
   print(type(odd_lst))