# 导入 requests 第三方包
import requests

def req_demo():
    # 封装请求参数 这是一个字典类型的数据
    data = {"username": "admin", "password": "123456"}
    # 发送请求 带上两个参数 url  和 请求正文 json
    response = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    print(type(requests))
    print(type(response))
    # 获取字符串类型的响应报文
    text_body = response.text
    print(type(text_body))
    print(text_body)

    # 获取响应报文 , response.json() :报文转换成 字典类型; 报文必须是json 才能转换
    json_body = response.json()
    print(type(json_body))
    print(json_body)

    # 断言响应状态码 是否是200
    assert 200 == response.status_code
    # 断言 响应正文 message 的值 是否包含 成功  两个字
    assert '成功' in json_body['message']
    # 断言 响应正文 code的 值 是否是 200 , 注意响应正文的code值 是 int 类型  所以用 == 不用in
    assert 200 == json_body['code']

    # 提取响应中的data 的值(这是一个字典类型的值)
    data_dict = json_body['data']
    # 提取 data_dict 字典 中 tokenHead 的值
    token_head = data_dict['tokenHead']
    # 提取 data_dict 字典 中 token 的值
    token_ = data_dict['token']
    # 封装 请求头
    head = {'Authorization': token_head + ' ' + token_}
    # 发起 Info 请求 , 传入指定参数 headers 值为 head
    get_info = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    # 打印响应正文
    print(get_info.text)
    info_json = get_info.json()

    # 断言响应状态码 是否是200
    assert 200 == get_info.status_code
    # 断言 响应正文 message 的值 是否包含 成功  两个字
    assert '成功' in info_json['message']
    # 断言 响应正文 code的 值 是否是 200 , 注意响应正文的code值 是 int 类型  所以用 == 不用in
    assert 200 == info_json['code']

    # 第一种 get 请求 直接将参数放入 url
    requests_get = requests.get('http://192.168.60.132:8080/brand/list?pageNum=1&pageSize=100',headers=head)
    # 第二种 get 请求 ,将参数 封装成一个 字典 ,请求的时候指定 params= 参数, 将封装的字典传给这个参数
    param = {'pageNum':1,'pageSize':3}
    get = requests.get('http://192.168.60.132:8080/brand/list', params=param, headers=head)
    print(get.text)
    # 获取 字典格式 的 响应正文
    json = get.json()
    # 获取 响应正文 中的data 的值
    json_data_ = json['data']
    # 获取json_data_字典的 key 为 list 的值,注意这个值是一个list的 对象 可以被遍历
    list_ = json_data_['list']
    # 遍历 list_
    for i in list_:
        print(i)

if __name__ == '__main__':
    req_demo()