#
class Human(object):

    def __init__(self,name,age,sex):
        self.name= name
        self.age = age
        self.sex=sex
    def myInfo (self):
        print('我叫%s,我今年%s岁,%s'%(self.name,self.age,self.sex))

class Tester(Human):
    def zhixingcehi(self):
        print('我在执行测试')
        print(self.age)
        self.myInfo()

if __name__ == '__main__':
    test=Human('hu',20,'nv')
    test.myInfo()

    tester = Tester('1','2','3')
    tester.zhixingcehi()