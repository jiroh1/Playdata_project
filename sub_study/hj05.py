#리티스를 인자값으로 받아 리스트 값들의 합을 구하는 함수를 만들어보자.

def get_sum(my_lst):    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for i in my_lst:
        total += i      # 1~10까지의 합

    return total        # 55를 리턴


def make_lst_a(n):  # n = 10
    lst = []
    for i in range(1, n+1):     # 1 ~ 10
        lst.append(i)   # 리스트에 1부터 10까지 추가된다.
    total = get_sum(lst)    # total = 55

    return total

def make_lst(n):
    lst = [] # 1~10 (n)까지 숫자가 담긴 리스트를 만든다.
    for i in range(1, n+1):
        lst.append(i)
    #print(lst)
    #print(make_even(lst))
    my_even = make_even(lst) # 1~10까지 숫자가 담긴 리스트를 짝수만 담긴 리스트로만 바꿔준다. lst_even에서 받은 값이 my_even

    return my_even

def make_even(lst):
    lst_even = []
    #print(lst)
    #짝수가 담긴 리스트를 만든다. # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 들어옴
    for k in lst :
        if k % 2 == 0:
            #print(k)
            lst_even.append(k)
            #print(lst_even)
  #  print(lst_even)
    return lst_even

def get_totals(n,k):
    res = 0;
    #print(n,k)
    for i in range(n,k+1):
        res +=i
    return res
    #print(res)

def get_even_total(even_lst):
    # 짝수를 가져온다 -> get_even()함수를 사용해서 짝수를 가져온다.
    even_lst_total=[]
    for i in even_lst:
        even_lst_total +=i
        even_lst_total.append(i)
    return even_lst_total


def get_odd_total(odd_lst):
    # 홀수를 가져온다 -> get_odd()함수를 사용해서 홀수를 가져온다.
    odd_lst_total=[]
    for i in odd_lst:
        odd_lst_total +=i
        odd_lst_total.append(i)
    return odd_lst_total


def get_even(even_lst):
    return


def get_odd(odd_lst):
    return


def get_total(lst):

    odd_lst = []
    even_lst = []
    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)

    # print(even_lst)
    # print(odd_lst)
    return even_lst
    return odd_lst
    #print(even_lst)
    # 짝수의 합을 가져온다   -> get_even_total() 함수를 이용한다.
    # 홀수의 합을 가져온다   -> get_odd_total() 함수를 이용한다.
    hap_even = get_even_total(even_lst)
    hap_odd = get_odd_total(odd_lst)
    return hap_odd+hap_even    # 짝수와 홀수의 합을 리턴한다.


if __name__ == '__main__':
    # result = hap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # print(result)
   #  print("--------------")

   # #n이라는 정수를 받아서 1부터 n까지의 수를 리스트로 만드는 함수를 만들고, 이 함수를 가지고 리스트의 합을 구하는 함수를 만들자.

   #  m_result = make_lst_a(10)
   #  #print(m_result)

   #  AAAAA = make_lst(10)
   #  print(AAAAA)

    # total = get_totals(5,10)
    # print(total)

    total = get_total([5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1])
    print(total)
