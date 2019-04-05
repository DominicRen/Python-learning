def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print(a)
        yield a  # 如果一个函数中有yield,则这个不再是函数,而是一个生成器的模板
        a, b = b, a+b
        current_num += 1


# 不是调用函数,而是创建一个生成器对象
obj = create_num(10)
obj2 = create_num(5)
ret = next(obj)
print(ret)
ret = next(obj)
print(ret)
ret = next(obj2)
print(ret)
# for num in obj:
#     print(num)
