import requests


def login_demo():
    data = {"username": "admin", "password": "123456"}
    r = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    text_body = r.text
    print(type(text_body))
    print(text_body)

    json_body = r.json()
    print(type(json_body))
    print(json_body)

    assert 200 == r.status_code
    assert 200 == json_body ['code']


    data_ = json_body['data']
    token_head_ = data_['tokenHead']
    token_ = data_['token']
    head = {'Authorization' : token_head_+' '+ token_}
    # 返回响应
    r_get = requests.get('http://192.168.60.132:8080/admin/info',headers= head)
    get_json = r_get.json()
    print(get_json)
    assert 200 == r_get.status_code
    assert 200 == get_json['code']
    assert '成功' in get_json['message']


    # 第二种 get  请求,讲参数封装成一个字典,请求的时候指定 params = 参数,将封装的字典传给这个参数
    # param= {'pageNum: 1 ,pageSize: 3}
    # requests.get('http://192.168.60.132:8080/order/list', headers=head , params= param,headers=head )
    response = requests.get('http://192.168.60.132:8080/order/list?pageNum=1&pageSize=10', headers=head)
    print(response.text)
    response_json = response.json()
    json_data_ = response_json ['data']
    list_ = json_data_['list']
    list_1 = list_[0]

    # 发货
    requests_post = requests.post('http://192.168.60.132:8080/order/update/delivery ', headers=head)
    print(requests_post.text)
    json = requests_post.json()

    # 关闭
    get = requests.post('http://192.168.60.132:8080/order/update/close ', headers=head)
    print(get.text)
    json1 = get.json()


if __name__ == '__main__':
    login_demo()
    pass





