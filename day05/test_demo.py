
import allure

@allure.feature('类上装饰器')

class TestHwr:
    @allure.story('max方法上的')
    def test_Max(self):
        assert 1<2

    @allure.story('max1方法上的')
    def test_Max1(self):
        assert 3<2

    @allure.story('max2方法上的')
    def test_Max2(self):
        assert 5>2


