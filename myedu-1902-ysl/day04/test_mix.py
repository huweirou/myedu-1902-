
# 如何使用pytest 做测试
# 1 设置Pycharm
# 2 新建模块: 以 test_ 开头
# 3 新建类  以 Test 开头
# 4 在类中新建方法 以 test_ 开头

class TestYsl:

    def test_Max(self):
        assert 1<2

    def test_Max1(self):
        assert 3<2

    def test_Max2(self):
        assert 5>2

