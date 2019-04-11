
# break 终止 所有循环 , continue终止本次循环

def break_demo():
    for i in range(5):
        print('第%s次循环'%i)
        # 如果i 等于2
        if i ==2:
            # 终止所有循环
            break

def continue_demo():
    for i in range(5):
        print('第%s次循环' % i)
        # 如果i 等于2
        if i == 2:
            print('')
            # 终止本次循环
            continue
        print('第%s次循环,if判断之后' % i)
        print('')

if __name__ == '__main__':
    # for i in range(5):
    #     print(i)
    #     if i == 3 :
    #         # 终止所有循环
    #         break
    #     print('第%s次循环至最后一行代码\n'%i)

    #
    for i in range(5):
        print(i)
        if i == 3 :
            # 终止本次循环
            continue
        # %s : 占位符   %i : i是变量 加百分号就是被替换的内容
        print('第%s次循环至最后一行代码\n'%i)

    # \n : 换行符
    # print('aaaa\nbbb')