
alist=[1,2,3,4,5,9,10,45,78,63]

def list_update(alist):
    alist[0]=10
    print(alist[0])
def pop_demo(alist):
       #pop()方法两个作用 第一个去除最后一位的值 第二个从列表中删除取出的值
      print(alist.pop(5))
       #pop()带参数 参数被用作下标值/索引 两个作用 第一个取出下标值代表的元素 第二个从列表中删除取出的元素
      print(alist)

def oderby_demo():

    pass
def reverse_demo():
    blist=[3,4,5,6,9,2]
    print(blist.reverse(blist))


       #pop()带参数
if __name__ == '__main__':
    alist=[1,2,3,4,5,9,10,45,78,63]
    #list_update(alist)
    pop_demo(alist)
    print()
    