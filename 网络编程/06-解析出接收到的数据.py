import socket


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定一个本地信息
    localaddr = ("192.168.1.11", 7788)
    udp_socket.bind(localaddr)  # 必须绑定自己的ip以及port
    # 接收数据
    recv_data = udp_socket.recvfrom(1024)
    # 接收到的数据是元组:(b"接收的内容", (对方的ip以及port))
    recv_msg = recv_data[0]  # 存储接收到的数据
    send_addr = recv_data[1]  # 存储发送方的地址信息
    # 打印接受到的数据
    # print(recv_data)
    print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))  # windows系统编码格式是gbk
    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
