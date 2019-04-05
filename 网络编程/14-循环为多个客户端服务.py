import socket


def main():
	# 1 socket创建套接字
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 2 bind绑定ip和port
	tcp_server_socket.bind(("", 7890))
	# 3 listen使套接字变为可以被动链接
	tcp_server_socket.listen(128)
	while True:
		# 4 accept等待客户端的链接	
		new_client_socket, client_addr = tcp_server_socket.accept()  # 返回的是元组
		print("客户端地址为：%s" % str(client_addr))
		# 5 recv接收客户端发送来的请求
		recv_data = new_client_socket.recv(1024)
		print("客户发送来的请求为：%s" % recv_data.decode("utf-8"))
		# 6 回送一部分数据给客户端
		new_client_socket.send("-----ok-----".encode("utf-8"))
		# 7 关闭套接字
		new_client_socket.close()
		print("服务完毕...")
	tcp_server_socket.close()


if __name__ == '__main__':
	main()
