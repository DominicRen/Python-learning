from greenlet import greenlet
import time


def test_1():
    while True:
        print("-----A-----")
        gr2.switch()
        time.sleep(0.5)


def test_2():
    while True:
        print("-----B-----")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test_1)
gr2 = greenlet(test_2)
gr1.switch()  # 切换到gr1中运行
