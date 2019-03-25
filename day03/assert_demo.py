

# assert 判断 是否 try except 用来捕捉异常


if __name__ == '__main__':
    a = '1000'
    b = '3000'
    if a<b :
        try :
            assert '3' in a
        except :
            print('xiao')
        finally:
            print('--')


