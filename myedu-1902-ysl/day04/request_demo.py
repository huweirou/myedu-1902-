# 导入 requests 包(第三方类库)
import requests

if __name__ == '__main__':
    # 声明 login_data 变量名 用来存 登录的请求数据
    login_data = {"username": "admin", "password": "123456"}
    #  = 后面就是发起一个请求,使用requests.post方法 ,入参 有两个,url:请求地址,json : 请求数据
    #  = 前面 就是声明一个变量 ,来存方法执行完后 return 的内容
    login_resp = requests.post(url='http://192.168.60.132:8080/admin/login', json=login_data)
    # .text 就是获取响应正文 (str 类型)
    # print(login_resp.text)

    # 获取 响应正文 (字典类型)  响应正文 必须是json 格式
    login_resp_json = login_resp.json()

    assert '成功' in login_resp_json['message']

    # 取出 响应正文 中 key 为的 message 的 值
    # print(login_resp_json['message'])
    print(login_resp_json)

    # 取出响应正文 中的 key 为 data 的值 (这个值是一个字典类型), 存入data_token变量
    data_token = login_resp_json['data']
    # 取出 data_token 里面 key 为 tokenHead 的值
    token_head = data_token['tokenHead']
    # 取出 data_token 里面 key 为 token 的值
    token = data_token['token']

    # 封装 head
    head = {'Authorization':token_head+token}
    # print(head)

    # getinfo 接口
    get_info_resp = requests.get(url='http://192.168.60.132:8080/admin/info',headers=head)
    print(get_info_resp.json())

    # get 请求 : url?k=v&k2=v2
    getoder_param = {'pageNum': 1, 'pageSize': 10}
    get_order_resp = requests.get(url='http://192.168.60.132:8080/order/list', params=getoder_param)
    print(get_order_resp.json())
    order_json = get_order_resp.json()
    assert '成功' in order_json['message']
    order_json_data = order_json['data']
    order_json_data_list = order_json_data['list']
    print(type(order_json_data_list))
    # print(order_json_data_list[0])
    # print(type(order_json_data_list[0]))
    # 遍历 订单列表
    for i in order_json_data_list:
        print(i)

