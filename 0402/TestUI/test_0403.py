import time
# from day06.Common.baseui import *
from Common.baseui import baseUI


class Test1:
    # 第一页
    def test_demo1(self, driver):
        base = baseUI(driver)

        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        base.send_keys('输入用户名' ,"//input[@name='username']", 'admin')

        # 输入密码
        base.send_keys('输入密码', "//input[@name='password']", '123456')
        # 点击登录
        base.click("点击登录", "//span[contains(text(),'登录')]")
        # 点击商品
        base.click("点击商品", "// span[contains(text(), '商品')]")
        # 点击添加商品
        base.click("添加商品", "(//span[contains(text(),'添加商品')])[1]")

    def test_demo2(self,driver):
        base = baseUI(driver)
        # 点击商品分类
        base.click("点击商品分类", "//span[@class='el-cascader__label']")
        # 点击商品分类点击服装
        base.click("点击服装", "// li[contains(text(), '服装')]")
        # 点击二级分类外套
        base.click("点击外套分类", "// li[contains(text(), '外套')]")
        # 填写商品名称
        base.send_keys("填写商品名称", "//label[contains(text(),'商品名称：')]/following-sibling::div//input", '夏装')
        time.sleep(2)

        # 写副标题
        base.send_keys("副标题", "//label[contains(text(),'副标题：')]/following-sibling::div//input", '双十一')
        time.sleep(2)

        # 点击商品品牌
        base.click("点击商品品牌", '//input[@placeholder="请选择品牌"]')
        time.sleep(2)

        # 点击小米
        base.click("选择小米", "// span[contains(text(), '小米')]")
        time.sleep(2)
        # 下滑
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        # 填写商品介绍
        base.send_keys("填写商品介绍", "//label[contains(text(),'商品介绍')]/following-sibling::div//textarea", '双十一上架')
        # 下一步
        base.click("点击下一步", "//span[text()='下一步，填写商品促销']")

    def test_demo3(self,driver):
        base = baseUI(driver)
        # 赠送积分
        base.send_keys("填写赠送积分", "//label[contains(text(),'赠送积分：')]/following-sibling::div//input", 30)
        # 赠送成长值
        base.send_keys('填写赠送成长值', "//label[contains(text(),'赠送成长值：')]/following-sibling::div//input", 200)
        # 预告商品
        base.click('预告商品', "//label[contains(text(),'预告商品')]/following-sibling::div//span")
        # 商品上架
        base.click('点击商品上架', "//label[contains(text(),'商品上架')]/following-sibling::div//span")
        time.sleep(2)
        # 滚动窗口
        base.scroll_screen('滚动')
        # 点击特惠促销
        base.click('点击特惠促销', "//span[contains(text(),'特惠促销')]")
        # 选择开始时间 //input[@placeholder="选择开始时间"] 2019-04-10 06:27:04
        base.send_keys('填写开始时间', '//input[@placeholder="选择开始时间"]', '2019-04-10 06:27:04')
        # 下一步 //span[contains(text(),'下一步，填写商品促销')]
        base.click('点击下一步', "//span[text()='下一步，填写商品属性']")

    def test_demo4(self,driver):
        base = baseUI(driver)
        # 属性类型
        base.click('属性类型','//label[contains(text(),"属性类型：")]/following-sibling::div//input')

        # 商品规格
        # 切换iframe
        iframe = driver.find_element_by_xpath("(//iframe[contains(id,vue-tinymce-)])[1]")
        driver.switch_to_frame(iframe)
        # 填写规格参数
        base.send_keys("填写规格参数","//body[@id='tinymce']","123456")
        driver.switch_to_default_content()
        # 下一步 //span[contains(text(),'下一步，选择商品关联')]
        base.click('点击下一步', "//span[contains(text(),'下一步，选择商品关联')]")
        #下滑
        base.scroll_screen('滚动')

    def test_demo5(self, driver):
        base = baseUI(driver)
        # 下一步 //span[contains(text(),'完成，提交商品')]
        base.click('点击完成提交', "//span[text()='完成，提交商品']")
        # # 切换弹框
        # driver.switch_to.alert.accept()
        # 弹框点击确定
        time.sleep(2)
        # driver.find_element_by_link_text('确定').click()
        base.click('点击取消','//span[contains(text(),"取消")]')


        # # 获取当前的页面窗口
        # first_handle = brower.current_window_handle
        # handles = brower.window_handles
        # for i in handles:
        #     if i != first_handle:
        #         brower.close()  # 关闭当前窗口
        #     brower.switch_to.window(i)
        #     brower.find_element_by_class_name("button1").click()  # 点击提交按钮，提交数据




