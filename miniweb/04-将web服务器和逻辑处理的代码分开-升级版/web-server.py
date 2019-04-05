import socket
import re
import multiprocessing
import time
import mini_frame


class WSGIServer(object):

    def __init__(self):
        # 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.tcp_server_socket.bind(("", 7890))
        # 监听套接字
        self.tcp_server_socket.listen(128)

    def service_client(self, new_socket):
        """为这个客户端返回数据"""
        # 接受浏览器发送来的请求，即http请求， GET /HTTP/1.1 ....
        request = new_socket.recv(1024).decode("utf-8")
        request_lines = request.splitlines()
        print("")
        print(">"*50)
        print(request_lines)
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"
        # 返回http格式的数据给浏览器, header, body
        # 如果请求的资源不是.py结尾，则认为是静态资源，如html/css/js/png,jpg等
        if not file_name.endswith(".py"):
            try:
                f = open("./html" + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "-----file not found-----"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                new_socket.send(response.encode("utf-8"))
                new_socket.send(html_content)
        else:
            # 如果是.py结尾，则认为是动态资源的请求
            header = "HTTP/1.1 200 OK\r\n"
            header += "\r\n"
            # body = mini_frame.login()
            body = mini_frame.application(file_name)
            response = header + body
            # 发送响应给浏览器
            new_socket.send(response.encode("utf-8"))
        # 关闭套接字
        new_socket.close()

    def run_forever(self):
        """用来完成整体的控制"""
        while True:
            # 等待新客户端的链接
            new_socket, client_addr = self.tcp_server_socket.accept()
            p = multiprocessing.Process(target = self.service_client, args = (new_socket,))
            p.start()
            # 进程之间不共享资源
            # 创建子进程复制主进程资源，创建硬链接，如果没有这句话，子线程关闭硬链接后，主线程还没有关
            new_socket.close()  
        # 关闭监听套接字
        self.tcp_server_socket.close()


def main():
    """控制整体，创建一个web对象，调用方法run_forever运行"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()
