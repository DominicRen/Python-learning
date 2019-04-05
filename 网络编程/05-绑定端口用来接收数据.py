import socket


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定一个本地信息
    localaddr = ("", 7788)
    udp_socket.bind(localaddr)
    # 接收数据 接收到的数据是元组:(b"接收的内容", 对方的ip以及port)
    recv_data = udp_socket.recvfrom(1024)
    # 打印接受到的数据
    print(recv_data)
    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
