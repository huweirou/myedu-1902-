# def int(a,b):
#
#     num=0
#     if a<b :
#         for i in range (a+1 , b):
#             if i%2==0:
#                 num = num +i
#         print(num)
#     else :
#         for i in range (b+1 , a):
#             if i%2==0 :
#                 num = num +i
#         print(num)
#
# if __name__ == '__main__':
#     int(15,5)


def int():
    a = 10
    b = 30
    num = 0
    if a < b:
        a_ = a + 1
        for i in range(a_, b):
            if i % 2 == 0:
                num += i

    elif a > b:
        b_ = b + 1
        for i in range(b_, a):
            if i % 2 == 0:
                num += i

    else:
        print('两数相等');
    print(num)


if __name__ == '__main__':
    int()
