
import json
# 声明一个全量 dict 变量 (字典)

adict = {"name":"ysl","pwd":"123456"}
adict_int = {"name":"ysl","pwd":"123456",1:'数字1'}

# 这是一个字符串 不过他是json 格式 ,也是字典的格式
adictStr = '{"name":"ysl","pwd":"123456","1":"数字1"}'

# str --> dict 字符串 转  dict
def zhuanhuanleixin():
    # 打印adictStr变量的类型
    print(type(adictStr))
    # 讲adictStr 转换为 dict 类型 并赋值给 dict_str
    dict_str = json.loads(adictStr)
    # 打印dict_str变量的类型
    print(type(dict_str))
    # 打印 dict_str 字典中 key 为 name 的值
    print(dict_str['name'])

def china_demo():
    # 字符串 转 dict
    loads = json.loads(adictStr)
    print(type(loads))
    # 字典转字符串 不处理编码格式
    json_dumps = json.dumps(loads)
    print(json_dumps)
    # 字典转字符串 , ensure_ascii=False 指定编码格式 不为 ASCII 码
    dumps = json.dumps(loads, ensure_ascii=False)
    print(dumps)

if __name__ == '__main__':
    # china_demo()
    # 打印 adict_int 字典中 key 为 1 的值
    # print(adict_int[1])
    # 打印 adict 字典
    print(adict)
    # 如何取值 ,变量名 加 [ ],然后中括号内放 key的名字
    print(adict['name'])
    # 删除 adict 字典 中key为 name 的 值,key 和 value 都会被删除
    adict.pop('name')
    print(adict)
    # 打印 adict 字典中 key 为 name 的值
    # print(adict['name'])

    # str --> dict
    pass
    # dict --> str  字典类型转换为 字符类型
    # dumps = json.dumps(adict)
    # print(type(dumps))
