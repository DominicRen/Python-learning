def add_yyy(func):
    print("-----开始进行装饰yyy的功能-----")
    def call_func(*args, **kwargs):
        print("----这是yyy功能-----")
        return func(*args, **kwargs)  # 相当于拆包
    return call_func


def add_xxx(func):
    print("-----开始进行装饰xxx的功能-----")
    def call_func(*args, **kwargs):
        print("----这是xxx功能-----")
        return func(*args, **kwargs)  # 相当于拆包
    return call_func


@add_yyy
@add_xxx
def test1():
    print("-----test1-----")


test1()
