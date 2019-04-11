# 这是一个注释
# model  模块  就是一个.py的文件 一个文件是一个小模块,如果包内有 __init__.py文件 那他就是一个大模块
# main 主要的
# print 打印
# def 声明方法 语法格式: def 方法名():  后面缩进四个空格(一个tab) 写方法内的代码 (如果缩进不一致他就不是方法内的代码)
# int 整数
# 声明变量 语法:  变量名 = 变量值
# demo 例子
# return 返回  方法return 之后 会返回一个值
# 代码的层级关系 通过 缩进来表示
# class 类,类型
# str string 字符
# 合法标识符(变量名方法名) : 必须以字母或者_开头,剩下的可以是字母数字,下划线,大小写敏感, 不可用关键字做标识符
# ctrl+alt+L 格式化代码
# ctrl+K  commit 代码
# ctrl + shift + K  push 代码

intqq = 50

# 声明一个int_demo 方法
def int_demo():
    # 声明aint变量 , 并赋值 1
    aint = 1
    # 打印 aint 的值
    print(aint)
    # 打印 aint 的 类型; type(aint): 获取aint的类型
    print(type(aint))

# 声明一个 str_demo 方法
def str_demo():
    # 声明astr变量 , 并赋值 '1'
    astr = '1'
    # 打印 astr 的值
    print(astr)
    # 打印 astr 的 类型; type(astr): 获取astr的类型
    print(type(astr))

    # 不写
    print('--------------')
    astr = 1
    # 打印 astr 的值
    print(astr)
    # 打印 astr 的 类型; type(astr): 获取astr的类型
    print(type(astr))

# 演示字符串拼接 : +
def str_demo1():
    a= 'hello'
    b= ' world'
    return a+b

# 字符串拼接: %s
def str_demo2():
    a= 'hello '
    b= 250
    # print(a+ str(b))
    print('a 是 : %s;b 是 : %s'%(a,b))

# 去掉两头空格
def str_demo3():
    astr = ' ysl '
    # astr 是变量 也叫 对象  ,对象 . 可以调用对象的方法
    print(astr)
    print(astr.strip())


# 12
# 声明一个add 方法 参数有两个 aint,bint
def add(aint, bint):
    # 打印aint参数
    # print(aint)
    # 打印bint参数
    # print(bint)
    # 返回 aint+bint
    aint_bint = aint + bint
    return aint_bint
    # 代码不要写到 return 下面 代码执行到return 就会结束这个方法,后面不会被执行

# 声明一个 float_demo 方法
def float_demo():
    # 声明afloat变量 , 并赋值 1.90
    afloat = 1.90
    # 打印 afloat 的值
    print(afloat)
    # 打印 afloat 的 类型; type(afloat): 获取afloat的类型
    print(type(afloat))

if __name__ == '__main__':
    # add(aint=1, bint=2)  调用 add 方法, 传入1(变量aint), 2(变量bint),得到返回值
    # sub =  声明sub 变量 ,并得到赋值,值是add 方法执行完的return 结果
    sub = add(aint=1, bint=2)
    print(sub)

    # print(str_demo1())
    # float_demo()
    # str_demo()
    # int_demo()
    # 提取变量  ctrl+alt+V
    #
    # 指定参数传参
    # print(result)
    # 默认参数传参
    # add(2,1)
    pass
