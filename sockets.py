#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import socket
import json

def serve():
    # 创建一个 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # 绑定端口号
        server_socket.bind(('localhost', 50010))
        # 开始监听端口
        server_socket.listen()
        print('Server is listening on port 50010...')
        while True:
            # 接收客户端连接请求
            client_socket, client_address = server_socket.accept()
            print(f'Connected by {client_address}')
            # 接收客户端发送的数据
            data = client_socket.recv(1024)
            print(f'Received data: {data.decode()}')
            # 构造 HTTP 的 JSON 响应
            response = {
                'success': True,
                'code': 10000,
                'data': {
                    'token': 'd8c6ed7a-3fd4-46e4-a477-b20d1ce9cda0'
                },
                'message': '执行成功'
            }
            # 将 JSON 响应序列化为字符串
            response_str = json.dumps(response)
            # 构造 HTTP 响应头
            headers = [
                'HTTP/1.1 200 OK',
                'Content-Type: application/json',
                f'Content-Length: {len(response_str)}',
                '',
                ''
            ]
            # 将 HTTP 响应头和 JSON 响应发送给客户端
            client_socket.sendall('\r\n'.join(headers).encode() + response_str.encode())
            # 关闭连接
            client_socket.close()

if __name__ == '__main__':
    serve()
