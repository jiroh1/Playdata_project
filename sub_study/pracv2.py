def get_even_total(lst):    # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1]
    even_total = 0
    # 짝수를 가져온다 -> get_even()함수를 사용해서 짝수를 가져온다.
    for i in lst:   # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1]
        my_even = get_even(i)   # 0
        if my_even == 0:
            pass
        even_total += my_even # 0 + 0
        print(my_even, end='   ')
    return even_total
def get_odd_total(lst): # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1])
    odd_total = 0
    # 홀수를 가져온다 -> get_odd()함수를 사용해서 홀수를 가져온다.
    for i in lst:
        my_odd = get_odd(i) # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1])
        if my_odd == 0:
            continue
        odd_total += my_odd
        print(my_odd, end='   ')
    return odd_total
def get_even(number):    # 5
    if number % 2 == 0:
        return number
    else:
        return 0
def get_odd(number):
    if number % 2 != 0:
        return number
    else:
        return 0
def get_total(lst):
    # 짝수의 합을 가져온다   -> get_even_total() 함수를 이용한다.
    total_even = get_even_total(lst)
    print('=  ', total_even)   # 0 + 0 + 2 + 0 + 0 + 56 + 34 + 0 + 6 + 0 + 0 = 98
    # 홀수의 합을 가져온다   -> get_odd_total() 함수를 이용한다.
    total_odd = get_odd_total(lst)
    print('=  ', total_odd)    # 5 + 7 + 9 + 11 + 21 + 3 + 1 = 57
    return total_even + total_odd    # 짝수와 홀수의 합을 리턴한다.
# make_lst(10)
if __name__ == '__main__':
    # result = hap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # print(result)
    print("-----------------------------")
    # n이라는 정수를 받아서 1부터 n까지의 수를 리스트로 만드는 함수를 만들고, 이 함수를 가지고 리스트의 합을 구하는 함수를 만들자
    #m_result = make_lst_a(10)   # m_reuslt = 55
    # print(m_result)
    total = get_total([5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1])
    print(total)