from selenium import webdriver
import time
import os

from Common.Assert import Assertions


class Test1 :
    def test_demo1(self):

        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "../../chromedriver/chromedriver.exe")

        # 打开浏览器
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.implicitly_wait(8)  # 设置隐式时间等待

        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        username = driver.find_element_by_xpath("//input[@name='username']")
        username.clear()
        username.send_keys('admin')
        # 输入密码
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys('123456')
        # 点击登录
        login = driver.find_element_by_xpath("//span[contains(text(),'登录')]")
        login.click()
        time.sleep(2)
        print(driver.page_source)
        # 断言

        assertions = Assertions()
        assertions.assert_in_text(driver.page_source,'首页')


        # 点击营销
        dianji = driver.find_element_by_xpath("// span[contains(text(), '营销')]")
        dianji.click()
        assertions = Assertions()
        assertions.assert_in_text(driver.page_source, '秒杀活动列表')
        time.sleep(2)
        # 点击优惠券列表
        youhui = driver.find_element_by_xpath("// span[contains(text(), '优惠券列表')]")
        youhui.click()
        time.sleep(2)
        assertions = Assertions()
        assertions.assert_in_text(driver.page_source, '优惠券类型')
        time.sleep(2)

        # 输入优惠券名称
        mingcheng = driver.find_element_by_xpath("//label[contains(text(),'优惠券名称')]/following-sibling::div//input")
        mingcheng.clear()
        # mingcheng.click()
        mingcheng.send_keys('全品类')
        time.sleep(2)
        assertions = Assertions()
        assertions.assert_in_text(driver.page_source, '全品类')
        time.sleep(2)
        # 点击查询搜索
        chaxun = driver.find_element_by_xpath("// span[contains(text(), '查询')]")
        chaxun.click()
        assertions = Assertions()
        assertions.assert_in_text(driver.page_source, '全品类')




        # 退出
        driver.quit()
        pass
