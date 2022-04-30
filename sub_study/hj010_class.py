#단일 클래스
#파이썬 클래스 이름은 대문자로 시작한다.
#함수는 단어마다 _를 써서 이어준다.
#  ->e.g. def make_string
# class UserInfo:
#     #this.name = name in Java
#
#     def __init__(self, name): #class 생성자 : __init__
#         self.name =name
#
#     def user_info(self):
#         print("Name:",self.name)
#
#
# user1 = UserInfo("Kim") #객체를 인스턴스화 시킨다. -->메모리에 올려 놓는다.
# #선언 후 인스턴스 화 시킴 . user1은 인스턴스
# print(user1.name) #self.name =name
# user1.user_info() #def user_info(self):
#
# user2 = UserInfo("Lee")
# print(user2.name)
# user2.user_info()
#
# class SelfTest:
#     def function_1(): # class method ,공통함수로 사용하기 위해서 ->아무나 쓸 수 있게
#         print(("function1 called"))
#     def function_2(self):
#         print(("function2 called"))
#
# SelfTest.function_1()
# test = SelfTest()
# test.function_2()
# #test.function_1() #에러남
class Calculator:

    def add(self,a,b):
        self.a = a
        self.b = b
        self.a += 5
        self.b += 5
        print(a,b)
        return a + b

    def sub(self,a,b):
        self.a= a
        self.b= b
        self.a += 5
        self.b += 5
        a += 6
        b += 6
        print(self.a, self.b, a , b)
        self.result = self.a + self.b
        print(a,b)
        return self.a + self.b

    def multy(self,a,b):
        pass

    def div(self,a,b):
        pass


my_cal = Calculator()
print(my_cal.add(10,5))
print(my_cal.add(20,11))