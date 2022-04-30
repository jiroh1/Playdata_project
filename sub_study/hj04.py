#리티스를 인자값으로 받아 리스트 값들의 합을 구하는 함수를 만들어보자.

def hap(get_lst):
    res = 0;
    for i in get_lst:
        #print(i)
        # print(res)
        res = res +i
        #print(res)
        # for res in i:
        #     print(res)
    return res


if __name__ == '__main__':
    result = hap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(result)


    #반복문 제어 break 반복문을 종료
    #continue는 조건문의 많이 씀 바로 for 문으로 다시올라감 /속도의 차이 느낌
    #그래서 혹시 코드가 길어서 continue를 써서 한 for 문안에서만 돌게 하는 것으로
    #pass는 바로 pass 밑의 명령문