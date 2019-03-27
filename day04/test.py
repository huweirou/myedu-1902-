import requests

def demo_mall():
    # 登录
    data= {'username': "admin", 'password': "123456"}
    response = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    response_text = response.text

    response_json = response.json()

    response_text_data_ = response_json['data']
    token_head_ = response_text_data_['tokenHead']
    token_ = response_text_data_['token']
    print(response.json())


#     查看订单
    orderlist_param = {'pageNum': 1, 'pageSize': 10}
    requests_get = requests.get(url='http://192.168.60.132:8080/order/list', params=orderlist_param)
    requests_get_json = requests_get.json()
    print(requests_get.json())

    
#     退货
    get = requests.get(url='http://192.168.60.132:8080/returnApply/list')
    json_tui = get.json()
    tui_data_ = json_tui['data']
    tui_data__list_ = tui_data_['list']
    data__list__id_ = tui_data__list_[0]
    list__order_id = tui_data__list_[1]


if __name__ == '__main__':
    demo_mall()


