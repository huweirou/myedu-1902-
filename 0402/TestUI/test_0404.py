import time
# from day06.Common.baseui import *

from Common.baseui import baseUI


class CampusTest(object):
    pass


class Test1:
    def test_111(self,driver):
        base = baseUI(driver)
        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        base.send_keys('输入用户名', "//input[@name='username']", 'admin')
        # 输入密码
        base.send_keys('输入密码', "//input[@name='password']", '123456')
        # 点击登录
        base.click("点击登录", "//span[contains(text(),'登录')]")
        # 点击订单
        base.click("点击订单", "//span[contains(text(),'订单')]")
        # 点击订单列表
        base.click("点击订单列表", "//span[contains(text(),'订单列表')]")
        # 下滑
        base.scroll_screen('下滑')
        # 点击订单状态
        base.click("点击订单状态","//label[contains(text(),'订单状态')]/following-sibling::div//input")
        # 点击待发货
        base.click("点击待发货", "//span[contains(text(),'待发货')]")
        # 点击查找
        base.click("点击查找", "//span[contains(text(),'查询搜')]")
        # 记录一条订单的编号
        num = base.get_text('获取编号', "//tbody/tr[1]/td[2]/div")
        order_num = base.get_text("获取订单编号", "//tbody/tr[1]/td[3]/div")
        # 点击第一条订单的发货按钮
        base.click("点击第一条订单的发货按钮", "(//span[contains(text(),'订单发货')])[1]")
        # 点击配送方式
        base.click("点击配送方式", "//input[@placeholder='请选择物流公司']")
        # 点击圆通快递//span[text()='圆通快递']
        base.click("点击圆通快递", "//span[text()='圆通快递']")
        # 输入物流单号//tbody/tr/td[7]//input
        base.send_keys("输入物流单号", "//tbody/tr/td[7]//input", "123456789")
        # 点击确定
        base.click("点击确定", "(//span[contains(text(),'确定')])[1]")
        # 提示框点击确定
        base.click("提示框点击确定", "(//span[contains(text(),'确定')])[2]")
        # 获取提示框文本
        text = base.get_text("获取提示框文本", "//div[@role='alert']/p")
        # 断言
        assert "成功" in text
        # 点击订单状态
        base.click("点击订单状态", "//label[contains(text(),'订单状态')]/following-sibling::div//input")
        # 点击已发货
        base.click("点击已发货", "//span[contains(text(),'已发货')]")
        # 点击查找
        base.click("点击查找", "//span[contains(text(),'查询搜索')]")
        # 输入订单编号
        base.send_keys("输入订单编号", '//input[@placeholder="订单编号"]', order_num)
        # 点击查找
        base.click("点击查找", "//span[contains(text(),'查询搜')]")
        time.sleep(2)
        nums = driver.find_elements_by_xpath("//tbody[1]/tr/td[2]")

        b = False
        for n in nums:
            print(n.text)
            if n.text == num:
                b= True

        assert True == b
        time.sleep(3)

    def test_122(self,driver):
        base = baseUI(driver)
        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        base.send_keys('输入用户名', "//input[@name='username']", 'admin')
        # 输入密码
        base.send_keys('输入密码', "//input[@name='password']", '123456')
        # 点击登录
        base.click("点击登录", "//span[contains(text(),'登录')]")
        # 点击订单
        base.click("点击订单", "//span[contains(text(),'订单')]")
        # 点击订单列表
        base.click("点击订单列表", "//span[contains(text(),'订单列表')]")
        # 下滑
        base.scroll_screen('下滑')
        # 点击订单状态
        base.click("点击订单状态","//label[contains(text(),'订单状态')]/following-sibling::div//input")
        # 点击待发货
        base.click("点击待发货", "//span[contains(text(),'待发货')]")
        # 点击查找
        base.click("点击查找", "//span[contains(text(),'查询搜索')]")
        # 编号全选
        base.click("编号全选","(//label[@role='checkbox'])[1]")
        # 点击批量操作
        base.click("点击批量操作", "//input[@placeholder='批量操作']")
        # 点击批量发货
        base.click("点击批量发货", "//span[contains(text(),'批量发货')]")
        # 点击确定
        base.click("点击确定", "//span[contains(text(),'确定')]")
        #输入发货公司 //tbody/tr[1]td[%s]%i
        aint = 20190404
        len1 = len(driver.find_elements_by_xpath("//tbody/tr"))
        for i in range(1,len1+1):
        # num = base.get_text('获取编号', "//tbody/tr[1]//div")

            base.click("点击物流公司", "//tbody/tr[{0}]/td[6]//input".format(i))
            base.click("点击顺丰", "(//span[text()= '顺丰快递'])[10]")
            aint = aint + 1
            base.send_keys("输入快递单号","//tbody/tr[{0}]/td[7]//input".format(i),aint)





        #
        # b = False
        # for n in nums:
        #     print(n.text)
        #     if n.text == num:
        #         b = True
        #
        # assert True == b


