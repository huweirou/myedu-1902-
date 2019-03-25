import  requests
# 登录
def login():
    data = { "password": "123456","username": "admin"}
    requests_post = requests.post(url='http://192.168.60.132/admin/login', json=data)
    text_login = requests_post.text
    print(text_login)

    json_body = requests_post.json()
    print(json_body)

    data_ = json_body['data']
    token_head_ = data_['tokenHead']
    token_ = data_['token']
    head={'Authorization':'token'+' '+'tokenHead'}
#     返回数据

    response = requests.get('http://192.168.60.132/admin/info', headers=head)
    json_info = response.json()
    print(json_info)

#     查看订单列表
    get_list = requests.get('http://192.168.60.132/order/list', headers=head)


if __name__ == '__main__':
   login()

   pass
