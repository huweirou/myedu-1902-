import selenium
from selenium import webdriver
from selenium import webdriver
import time
import os
from day06.Common.baseui import *

from day06.Common.Assert import Assertions


class Test1 :
    def test_demo1(self,driver):



        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        send_keys(driver,"//input[@name='username']",'admin')
        # username = driver.find_element_by_xpath("//input[@name='username']")
        # username.clear()
        # username.send_keys('admin')


        # 输入密码
        send_keys(driver, "//input[@name='password']", '123456')
        # password = driver.find_element_by_xpath("//input[@name='password']")
        # password.clear()
        # password.send_keys('123456')

        # 点击登录
        click(driver,"//span[contains(text(),'登录')]")
        # login = driver.find_element_by_xpath("//span[contains(text(),'登录')]")
        # login.click()
        time.sleep(2)

        # 点击商品
        click(driver,"// span[contains(text(), '商品')]")
        # dianji = driver.find_element_by_xpath("// span[contains(text(), '商品')]")
        # dianji.click()
        time.sleep(2)


        # 点击添加商品
        tjsp = driver.find_element_by_xpath("(//span[contains(text(),'添加商品')])[1]")
        tjsp.click()
        time.sleep(2)
        # assertions = Assertions()
        # assertions.assert_in_text(driver.page_source, '填写商品信息')


        # 点击商品分类
        djspfl = driver.find_element_by_xpath("//span[@class='el-cascader__label']")
        djspfl.click()

        # 点击商品分类点击服装
        click(driver, "// li[contains(text(), '服装')]")
        # djspfl = driver.find_element_by_xpath("// li[contains(text(), '服装')]")
        # djspfl.click()

        # 点击二级分类外套
        click(driver,"// li[contains(text(), '外套')]")
        # djej = driver.find_element_by_xpath("// li[contains(text(), '外套')]")
        # djej.click()
        time.sleep(2)

        # 填写商品名称
        send_keys(driver, "//label[contains(text(),'商品名称：')]/following-sibling::div//input", '夏装')
        # xpath_mc = driver.find_element_by_xpath("//label[contains(text(),'商品名称：')]/following-sibling::div//input")
        # xpath_mc.send_keys('夏装')
        time.sleep(2)

        # 写副标题
        send_keys(driver,"//label[contains(text(),'副标题：')]/following-sibling::div//input",'双十一')
        # xpath_fbt = driver.find_element_by_xpath("//label[contains(text(),'副标题：')]/following-sibling::div//input")
        # xpath_fbt.send_keys('双十一')
        time.sleep(2)


        # 点击商品品牌
        click(driver,'//input[@placeholder="请选择品牌"]')
        # xpath_pingpai = driver.find_element_by_xpath('//input[@placeholder="请选择品牌"]')
        # xpath_pingpai.click()
        time.sleep(2)

        # 点击小米
        xpath_xiaomi = driver.find_element_by_xpath("// span[contains(text(), '小米')]")
        xpath_xiaomi.click()
        time.sleep(2)

        # 填写商品介绍
        xpath_mc = driver.find_element_by_xpath("//label[contains(text(),'商品介绍')]/following-sibling::div//textarea")
        xpath_mc.send_keys('双十一上架')
        time.sleep(2)

        # 下一步
        shangpcuxiao = driver.find_element_by_xpath("//span[text()='下一步，填写商品促销']")
        shangpcuxiao.click()
        time.sleep(2)

        # 赠送积分
        xpath_jifen = driver.find_element_by_xpath("//label[contains(text(),'赠送积分：')]/following-sibling::div//input")
        xpath_jifen.send_keys(30)

        # 赠送成长值
        xpath_chenngzhangzhi = driver.find_element_by_xpath("//label[contains(text(),'赠送成长值：')]/following-sibling::div//input")
        xpath_chenngzhangzhi.send_keys(200)

        #预告商品
        xpath_yugao = driver.find_element_by_xpath("//label[contains(text(),'预告商品')]/following-sibling::div//span")
        xpath_yugao.click()

        # 商品上架
        xpath_shangjia = driver.find_element_by_xpath("//label[contains(text(),'商品上架')]/following-sibling::div//span")
        xpath_shangjia.click()
        time.sleep(2)

        # 下一步 //span[contains(text(),'下一步，填写商品促销')]
        shangpcuxiao = driver.find_element_by_xpath("//span[text()='下一步，填写商品属性']")
        shangpcuxiao.click()
        time.sleep(2)


        pass
