import allure
import pytest
from Common import read_excel
from Common import Request, Assert

assertions = Assert.Assertions()

request = Request.Request()
url = 'http://192.168.60.132:8080'
excel_list = read_excel.read_excel_list("../day06/documents/test.xlsx")
idsList = []
for i in range(len(excel_list)):
    idsList.append(excel_list[i].pop())

myToken = ''
head = {'Authorization' : myToken}
f_order_id =0
s_order_id =0
id = []

@allure.feature("登录模块")
class TestLogin(object):



    @allure.story("登录系统")
    @pytest.mark.parametrize('name,pwd,msg',excel_list,
                                    ids=idsList)
    def test_case_login(self,pwd,name,msg):
        login_data = { "username": name,"password": pwd}
        login_resp = request.post_request(url=url+"/admin/login", json=login_data)
        # .assert_code 用来断言 状态码 ; 第一个参数 填 响应的状态码, 第二个参数 期望值
        assertions.assert_code( login_resp.status_code,200)
        login_resp_json = login_resp.json()
        data_token = login_resp_json['data']
        if(bool(data_token)):
            token = data_token['token']
            token_head = data_token['tokenHead']
            global myToken
            global head
            myToken = token_head + token
            head = {'Authorization': myToken}



    @allure.story("获取用户信息")
    def test_case_info(self):
        get_info_resp = request.get_request(url=url + '/admin/info', headers=head)
        assertions.assert_code(get_info_resp.status_code, 200)

    @allure.story("订单列表")
    def test_case_list(self):
        get_request = request.get_request(url=url+'/order/list', headers=head)
        assertions.assert_code(get_request.status_code,200)


#
    @allure.story("查看代发货订单列表")
    def test_case_list(self):
        param = {'pageNum':1,'pageSize':10,'status':1}
        get_request = request.get_request(url=url + '/order/list',params=param, headers=head)
        assertions.assert_code(get_request.status_code, 200)
        json_data = get_request.json()
        data_ = json_data['data']
        data_ = data_['list']
        print(data_)
        global f_order_id
        a = data_[0]
        f_order_id = a['id']

    @allure.story("订单发货")
    def test_case_delivery(self):
        delivery_data = [{"deliveryCompany": "顺丰快递", "deliverySn": "5896545", "orderId": f_order_id}]
        request_post_request = request.post_request(url=url+'/order/update/delivery',headers=head, json=delivery_data)
        assertions.assert_code(request_post_request.status_code,200)
        code = request_post_request.json()
        assertions.assert_code(code['code'],200)

    @allure.story("查看可删除订单")
    def test_case_keshanchu(self):
        status_ = {'pageNum': 1, 'pageSize': 10, 'status': 4}
        get_request = request.get_request(url=url+'/order/list', headers=head,params=status_)
        assertions.assert_code(get_request.status_code,200)
        request_json = get_request.json()
        print(request_json)
        json_data = get_request.json()
        data_ = json_data['data']
        data_ = data_['list']
        print(data_)
        global s_order_id
        a = data_[0]
        s_order_id = a['id']





    @allure.story("删除订单")
    def test_case_delete(self):

         ids_ = {'ids': s_order_id}
         request_get_request = request.post_request(url=url + '/order/delete', params=ids_, headers=head)
         assertions.assert_code(request_get_request.status_code, 200)
         request_json = request_get_request.json()
         assertions.assert_code(request_json['code'],200)

    # @allure.story("查看商品列表")
    # def test_case_chakan(self):
    #     num_ = {'total': 11, 'totalPage': 1, 'pageSize': 100, list: '[,…]', 'pageNum': 1}
    #     request_get_request = request.get_request(url=url + '/brand/list', params=num_, headers=head)
    #     assertions.assert_code(request_get_request.status_code, 200)
    #     request_json = request_get_request.json('code')
    #     assertions.assert_code(request_json, 200)
    #
    # @allure.story("编辑商品")
    # def test_case_bianji(self):
    #     num_ = {'id': 32, 'brandId': 50, 'productCategoryId': 8, 'feightTemplateId': 0, 'productAttributeCategoryId': 'null',}
    #     request_get_request = request.get_request(url=url + '/product/updateInfo/32', params=num_, headers=head)
    #     assertions.assert_code(request_get_request.status_code, 200)
    #     request_json = request_get_request.json('code')
    #     assertions.assert_code(request_json, 200)

