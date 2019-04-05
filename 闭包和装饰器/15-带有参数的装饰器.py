def set_func(func):
    def call_func(*args, **kwargs):
        level = args[0]
        if level == 1:
            print("----权限级别1验证----")
        elif level == 2:
            print("----权限级别2验证----")
        return func()
    return call_func


@set_func
def test1():
    print("-----test1-----")
    return "OK"


@set_func
def test2():
    print("-----test2-----")
    return "OK"


test1(1)
test2(2)
