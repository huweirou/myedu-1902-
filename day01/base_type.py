# model 模块 main 主要的
# print 打印 def 声明方法 int 整数 demo 例子
# class 类型,类 str (string)字符串

def int_demo():
    aint = 1
    print(aint)


# def  声明方法

def add(aint, bint):
    print(aint)
    print(bint)
    return aint + bint


#  加

if __name__ == '__main__':
    # int_demo()
    add1 = add(1, 2)
    print(add1)
    # 提取变量 crtl+alt+v


def sub(aint, bint):
    print(aint)
    print(bint)
    return bint - aint


if __name__ == '__main__':
    sub1 = sub(3, 1)
    print(sub1)


def float_demo():
    afloat=1.33
    print(afloat)
    print(type(afloat))
    
    pass
