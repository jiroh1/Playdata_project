def get_even_total(even_lst):
    # 짝수를 가져온다 -> get_even()함수를 사용해서 짝수를 가져온다.
    pass

def get_odd_total(odd_lst):
    # 홀수를 가져온다 -> get_odd()함수를 사용해서 홀수를 가져온다.
    odd_lst_total = []
    for i in odd_lst:
        odd_lst_total += i
        odd_lst_total.append(i)
    print(odd_lst_total)
    return odd_lst_total



def get_even(even_lst):
    pass


def get_odd(odd_lst):
    print(odd_lst)


def get_total(lst):
    odd_lst = []
    even_lst = []
    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)

    print(even_lst)
    print(odd_lst)
    # 짝수의 합을 가져온다   -> get_even_total() 함수를 이용한다
    # 홀수의 합을 가져온다   -> get_odd_total() 함수를 이용한다.
    return 0

if __name__ == '__main__':

    total = get_total([5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1])
    #print(total)
