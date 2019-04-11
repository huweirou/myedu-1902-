
import pytest

if __name__ == '__main__':
    # pass
    # 调用测试框架 pytest  --alluredir: 指定 allure的目录地址; ../Report/xml/: 实际地址
    # pytest.main(['-s', '-q','--alluredir','../Report/xml/', '.'])

    # allure generate ./Report/xml/ -o ./Report/html/ --clean

    try:
        assert 5<2
    except:
        print('错了')
        raise # 抛出异常