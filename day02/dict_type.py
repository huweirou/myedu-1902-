
import json
# 声明一个全量dict 变量
# 字符---字符串
adict={"name":"huwr","pwd":123456,"1":"数字"}
adictstr = '{"name":"huwr","pwd":123456,"1":"数字"}'

adict.pop('name')
print(adict)

def china_demo():
    loads = json.loads(adictstr)
    print(type(loads))

    json_dumps = json.dumps(loads)
    print(json_dumps)

    dumps = json.dumps(loads, ensure_ascii=False)
    print(dumps)

loads = json.loads(adictstr)

if __name__ == '__main__':
    print(type(adictstr))

    loads = json.loads(adictstr)
    print(type(loads))

    dumps = json.dumps(adict)
    print(type(dumps))
    json_dumps = json.dumps(loads)
    print(json_dumps)

    dumps = json.dumps(loads, ensure_ascii=False)
    print(dumps)


