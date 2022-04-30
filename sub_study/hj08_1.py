def for_moon(): # def for_moon(n):
    for i in range(1, 11): # for i in n:
        print(i, end=" ")

def whil_moon():
    i = 0
    while i < 10 :
        i += 1  #초기 값은 while 밖에서 선언해야 한다.
        print(i, end=" ")

if __name__ == '__main__':
    #lst = [1,2,3]
    for_moon() # for_moon(lst)
    whil_moon()