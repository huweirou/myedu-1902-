import requests

def jiekou () :
    # 登录
    data={'username': "admin", 'password': "123456"}
    post_login = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    login_json = post_login.json()
    json_data_ = login_json['data']
    data__token_ = json_data_['token']
    data__tokenhead_ = json_data_['tokenhead']
    head = {'Authorization': 'data__token_' + ' ' + 'data__tokenhead_'}
#    返回数据
