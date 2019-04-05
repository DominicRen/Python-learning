import threading
import time


def test1(temp):
    temp.append(33)
    print("-----in test1 temp = %s-----" % str(temp))


def test2(temp):
    print("-----in test2 temp = %s-----" % str(temp))


g_nums = [11, 22]


def main():
    t1 = threading.Thread(target=test1, args=(g_nums,))  # args指定调用函数时传递的参数(元组)
    t2 = threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("-----in main Thread g_nums = %s-----" % str(g_nums))


if __name__ == "__main__":
    main()
