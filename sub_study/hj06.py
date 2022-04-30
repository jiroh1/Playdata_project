# single function
#단일 함수

def count_word(word_list):
    print(word_list)
    cnt = 0;
    for i in word_list:
#        print(i)
        for k in i:
            cnt += 1;
#    print(cnt)
    return cnt

if __name__ == '__main__':
    mylst = ['Hello']
    result = count_word(mylst)
    print(result)