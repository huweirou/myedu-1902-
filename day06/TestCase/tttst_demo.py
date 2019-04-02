import allure
from Common import Request, Assert

# 新建一个 Assert.Assertions() 的对象 对象名: assertions
assertions = Assert.Assertions()

# 新建一个 Request.Request() 的对象 对象名: request
request = Request.Request()

myToken = ''
head = {'Authorization' : myToken}
url = 'http://192.168.60.132:8080'
# url_yuming = ''

@allure.feature("登录模块")
class TestLogin(object):

    @allure.story("登录系统")
    def test_case_login(self):
        login_data = {"password": "123456", "username": "admin"}
        login_resp = request.post_request(url=url+"/admin/login", json=login_data)
        # .assert_code 用来断言 状态码 ; 第一个参数 填 响应的状态码, 第二个参数 期望值
        assertions.assert_code( login_resp.status_code,200)
        # 获取响应正文  字典格式
        login_resp_json = login_resp.json()
        data_token = login_resp_json['data']
        token = data_token['token']
        token_head = data_token['tokenHead']

        # global : 引入 全局变量 然后才可以对全局变量重新赋值
        global myToken
        global head
        myToken = token_head + token
        head = {'Authorization': myToken}

    @allure.story("获取用户信息")
    def test_case_info(self):
        get_info_resp = request.get_request(url=url+'/admin/info', headers=head)

        assertions.assert_code( get_info_resp.status_code,400)

    @allure.story("订单列表")
    def test_case_list(self):
        get_request = request.get_request(url=url+'/order/list', headers=head)
        assertions.assert_code(get_request.status_code,300)

    @allure.story("订单发货")
    def test_case_delivery(self):
        delivery_data = [{"deliveryCompany": "顺丰快递", "deliverySn": "5896545", "orderId": "21"}]
        request_post_request = request.post_request(url=url+'/order/update/delivery',headers=head, json=delivery_data)
        assertions.assert_code(request_post_request.status_code,200)
        code = request_post_request.json(['code'])
        assertions.assert_code(code,200)



    @allure.story("删除订单")
    def test_case_delete(self):
         ids_ = {'ids': '27'}
         request_get_request = request.get_request(url=url + '/order/delete', params=ids_, headers=head)
         assertions.assert_code(request_get_request.status_code, 200)
         request_json = request_get_request.json(['code'])
         assertions.assert_code(request_json,200)