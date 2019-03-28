alist=[0,4,5,6,1,2,3]
# 全局
def list_update():
    alist[0]=2
    return alist
    print(alist)

def orderby_demo():
    sort_demo()
    reverse_demo()
    pass
def sort_demo():
    alist.sort()
    print(alist)

def reverse_demo():
    alist.reverse()
    print(alist)

if __name__ == '__main__':
    sort_demo()
    reverse_demo()
    print(alist)


