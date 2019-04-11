import time
# from day06.Common.baseui import *

from Common.baseui import baseUI


class Testll:
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
        # 点击营销
        base.click("点击营销","//span[contains(text(),'营销')]")
        base = baseUI(driver)
        # 点击优惠券列表
        base.click("点击优惠券列表", "//span[contains(text(),'优惠券列表')]")
        # 点击编辑
        base.click("点击编辑", "//span[contains(text(),'编辑')]")
        # 输入优惠券名称
        base.send_keys("输入优惠券名称", "//label[contains(text(),'优惠券名称')]/following-sibling::div//input", 'youhuiquan')
        # 点击提交
        base.click("点击提交", "//span[contains(text(),'提交')]")
        time.sleep(2)
        # 点击确定// span[contains(text(), '确定')]
        base.click("点击确定", "//span[contains(text(),'确定')]/parent::button")
        # 断言 /html[@class=' ']/body/div[@class='el-message el-message--success']
        source = driver.page_source
        print(source)
        tishi = driver.find_element_by_xpath("//div[@role = 'alert']/p")
        assert "修改成功" in tishi.text

    def tellst_tianjia(self, driver):
        base = baseUI(driver)
        # 点击优惠券列表
        base.click("点击优惠券列表","//span[contains(text(),'优惠券列表')]")
        # 点击添加
        base.click("点击添加", "(//span[contains(text(),'添加')])[2]")
        # 输入优惠券名称
        base.send_keys("输入优惠券名称", "//label[contains(text(),'优惠券名称')]/following-sibling::div//input",'youhuiquan')
        # 输入总发行量


# 输入面额
# 输入使用门槛
# 点击提交
