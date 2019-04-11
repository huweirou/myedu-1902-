# assert 就是 断言 语法: assert 条件
# try except 用来捕捉异常
def try_demo():
    a = "123456"
    # try 用于异常处理 ;如果出现异常 则执行 except 内的代码
    try:
        # 判断 a 是否包含 5
        assert '5' in a
    # except 报错后执行
    except:
        print('a里面没有7')
    print('------')

def zuihou():
    a = "123456"
    # try 用于异常处理 ;如果出现异常 则执行 except 内的代码
    try:
        # 判断 a 是否包含 5
        assert '7' not in a
    # except 报错后执行
    except:
        print('a里面没有7')
    # 不管 是否有异常,finally里面的代码 都会被执行
    finally:
        print('最后----')


if __name__ == '__main__':
    # 断言为True 不会有报错
    # assert 4 > 2
    # 断言 为False 会报错 AssertionError
    # assert 1>2

    # 断言字符串
    astr = '的尽快了解爱发科来得及罚款是'
    # 判断 astr 字符 内 是有包含 你 这个字
    # assert '你' in astr
    # 判断 astr 字符内 是否不包含 你 这个字
    # assert '你' not in astr

    # try 用于异常处理 ;如果出现异常 则执行 except 内的代码; 不会影响后面的代码 继续执行
    # 应用场景: 用于 包裹 可能会出错的代码块,出错执行 except内的代码,不出错不执行 except的代码
    try:
        assert '你' in astr
    except:
        print('报错啦,断言没通过')

    print('--------')