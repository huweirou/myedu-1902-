# break 终止 所有循环 continue 终止本次循环

def continue_demo():
    for i in range(1, 10):
        i += 3
        print('第%s次循环' % i)
        if i == 5 or i == 4:
            continue
        if i == 10:
            break
        print('3')


if __name__ == '__main__':

# if  i == 4 :
#     break
