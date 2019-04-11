# 如何调用别人的代码
#  第一步: 导入: import   如果是大模块导入 ,需要加 from 大模块的名字 import 小模块的名字
from day01 import base_type

if __name__ == '__main__':
    # 如何使用 小模块的方法
    # 小模块的名字.方法名() : 若有参数,入参,写括号内,可指定参数入参,可默认参数入参;没有参数不管
    # = 后面是 调用方法
    # = 前面是 给方法的返回值起个名字 ,存起来
    result = base_type.add(aint=10, bint=5)
    print(result)
    # base_type.intqq 不带括号 ,说明调用了一个变量 ,这个变量是这个模块里面有的
    print(base_type.intqq)
