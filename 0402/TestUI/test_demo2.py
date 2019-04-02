import time
# from day06.Common.baseui import *
from Common.baseui import BaseUI


class Test1:
    def test_demo1(self, driver):
        base = BaseUI(driver)

        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        base.send_keys('输入用户名' ,"//input[@name='username']", 'admin')
        # username = driver.find_element_by_xpath("//input[@name='username']")
        # username.clear()
        # username.send_keys('admin')

        # 输入密码
        base.send_keys( '输入密码',"//input[@name='password']", '123456')
        # password = driver.find_element_by_xpath("//input[@name='password']")
        # password.clear()
        # password.send_keys('123456')

        # 点击登录
        base.click("点击登录", "//span[contains(text(),'登录')]")
        # login = driver.find_element_by_xpath("//span[contains(text(),'登录')]")
        # login.click()
        time.sleep(2)

        # 点击商品
        base.click("点击商品", "// span[contains(text(), '商品')]")
        # dianji = driver.find_element_by_xpath("// span[contains(text(), '商品')]")
        # dianji.click()
        time.sleep(2)

        # 点击添加商品
#         base.click("添加商品", "(//span[contains(text(),'添加商品')])[1]")
#         # tjsp = driver.find_element_by_xpath("(//span[contains(text(),'添加商品')])[1]")
#         # tjsp.click()
#         time.sleep(2)
#         # assertions = Assertions()
#         # assertions.assert_in_text(driver.page_source, '填写商品信息')
#
#         # 点击商品分类
#         base.click("点击商品分类", "//span[@class='el-cascader__label']")
#         # djspfl = driver.find_element_by_xpath("//span[@class='el-cascader__label']")
#         # djspfl.click()
#
#         # 点击商品分类点击服装
#         base.click("点击服装", "// li[contains(text(), '服装')]")
#         # djspfl = driver.find_element_by_xpath("// li[contains(text(), '服装')]")
#         # djspfl.click()
#
#         # 点击二级分类外套
#         base.click("点击外套分类", "// li[contains(text(), '外套')]")
#         # djej = driver.find_element_by_xpath("// li[contains(text(), '外套')]")
#         # djej.click()
#         time.sleep(2)
#
#         # 填写商品名称
#         base.send_keys("填写商品名称", "//label[contains(text(),'商品名称：')]/following-sibling::div//input", '夏装')
#         # xpath_mc = driver.find_element_by_xpath("//label[contains(text(),'商品名称：')]/following-sibling::div//input")
#         # xpath_mc.send_keys('夏装')
#         time.sleep(2)
#
#         # 写副标题
#         base.send_keys("副标题", "//label[contains(text(),'副标题：')]/following-sibling::div//input", '双十一')
#         # xpath_fbt = driver.find_element_by_xpath("//label[contains(text(),'副标题：')]/following-sibling::div//input")
#         # xpath_fbt.send_keys('双十一')
#         time.sleep(2)
#
#         # 点击商品品牌
#         base.click("点击商品品牌", '//input[@placeholder="请选择品牌"]')
#         # xpath_pingpai = driver.find_element_by_xpath('//input[@placeholder="请选择品牌"]')
#         # xpath_pingpai.click()
#         time.sleep(2)
#
#         # 点击小米
#         base.click("选择小米", "// span[contains(text(), '小米')]")
#         # xpath_xiaomi = driver.find_element_by_xpath("// span[contains(text(), '小米')]")
#         # xpath_xiaomi.click()
#         time.sleep(2)
#
#         # 下滑
#         js = "var q=document.documentElement.scrollTop=10000"
#         driver.execute_script(js)
#
#         # 填写商品介绍
#         base.send_keys("填写商品介绍", "//label[contains(text(),'商品介绍')]/following-sibling::div//textarea", '双十一上架')
#         # xpath_mc = driver.find_element_by_xpath("//label[contains(text(),'商品介绍')]/following-sibling::div//textarea")
#         # xpath_mc.send_keys('双十一上架')
#         time.sleep(2)
#
#         # 下一步
#         base.click("点击下一步", "//span[text()='下一步，填写商品促销']")
#         # shangpcuxiao = driver.find_element_by_xpath("//span[text()='下一步，填写商品促销']")
#         # shangpcuxiao.click()
#         time.sleep(2)
#
# #
# #         # 赠送积分
#         base.send_keys("填写赠送积分", "//label[contains(text(),'赠送积分：')]/following-sibling::div//input", 30)
# #         # xpath_jifen = driver.find_element_by_xpath("//label[contains(text(),'赠送积分：')]/following-sibling::div//input")
# #         # xpath_jifen.send_keys(30)
# #
# #         # 赠送成长值
#         base.send_keys('填写赠送成长值', "//label[contains(text(),'赠送成长值：')]/following-sibling::div//input", 200)
# #         # xpath_chenngzhangzhi = driver.find_element_by_xpath("//label[contains(text(),'赠送成长值：')]/following-sibling::div//input")
# #         # xpath_chenngzhangzhi.send_keys(200)
# #
# #         # 预告商品
#         base.click('预告商品', "//label[contains(text(),'预告商品')]/following-sibling::div//span")
# #         # xpath_yugao = driver.find_element_by_xpath("//label[contains(text(),'预告商品')]/following-sibling::div//span")
# #         # xpath_yugao.click()
# #
# #         # 商品上架
#         base.click('点击商品上架', "//label[contains(text(),'商品上架')]/following-sibling::div//span")
# #         # xpath_shangjia = driver.find_element_by_xpath("//label[contains(text(),'商品上架')]/following-sibling::div//span")
# #         # xpath_shangjia.click()
# #         time.sleep(2)
# #
# #         # 下滑
#         js = "var q=document.documentElement.scrollTop=10000"
#         driver.execute_script(js)
# #
# #         # 点击特惠促销
#         base.click('点击特惠促销', "//span[contains(text(),'特惠促销')]")
# #
# #         # 选择开始时间 //input[@placeholder="选择开始时间"] 2019-04-10 06:27:04
#         base.send_keys('填写开始时间', '//input[@placeholder="选择开始时间"]', '2019-04-10 06:27:04')
# #
# #         # 下一步 //span[contains(text(),'下一步，填写商品促销')]
#         base.click('点击下一步', "//span[text()='下一步，填写商品属性']")
# #         # shangpcuxiao = driver.find_element_by_xpath("//span[text()='下一步，填写商品属性']")
# #         # shangpcuxiao.click()
# #         time.sleep(2)
# #
# #         # 下滑
#         js = "var q=document.documentElement.scrollTop=10000"
#         driver.execute_script(js)
# #
# #         # 下一步 //span[contains(text(),'下一步，填写商品促销')]
#         base.click('点击下一步', "//span[text()='下一步，选择商品关联']")
# #         # shangpcuxiao = driver.find_element_by_xpath("//span[text()='下一步，填写商品属性']")
# #         # shangpcuxiao.click()
# #         time.sleep(2)
# #
# #         # 下一步 //span[contains(text(),'完成，提交商品')]
#         base.click('点击完成提交', "//span[text()='完成，提交商品']")
# #         # shangpcuxiao = driver.find_element_by_xpath("//span[text()='下一步，填写商品属性']")
# #         # shangpcuxiao.click()
# #         time.sleep(2)
# #
# #         # 完成
# #         base.click('确定提交', "(//span[contains(text(),'确定')])[3]")
#
#         pass


