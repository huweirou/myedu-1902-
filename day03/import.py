import os

def os_demo() :
    # 获取当前目录的路径
    getcwd = os.getcwd()
    print(getcwd)

    # 获取上级目录的路径
    abspath = os.path.abspath('..')
    print(abspath)

    # 获取上上级目录
    path_abspath = os.path.abspath('../..')
    print(path_abspath)



if __name__ == '__main__':
    text_io = open('../test.text','w+')
    text_io.write("xxxxx")
    pass