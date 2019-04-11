# 取余

def jisuan(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)

# 比较符 完成后 会返回一个bool值 ,只有True 和 False
def duibi(a,b,c):
    print(a > b)
    print(a < b)
    print(a == b)
    print(a == c)
    print(a >= b)
    print(a != b)

def deng(a):
    a += 1  # a = a+1
    print(a)
    a *= 2  # a = a*2
    print(a)
    a -= 5  # a = a-5
    print(a)
    a /= 2  # a = a/2
    print(a)

if __name__ == '__main__':
   duibi(1,2,3)

