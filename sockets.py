#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import socket
import json
from urllib.parse import urlparse, parse_qs

def handle_request(request):
    # 解码请求数据
    request = request.decode('utf-8')
    # 解析请求头
    request_lines = request.split('\r\n')
    request_method, request_path, request_version = request_lines[0].split()

    # 查找 Authorization 头
    authorization_header = None
    for line in request_lines[1:]:
        print(f'----- {line}')
        if line.lower().startswith('authorization:'):
            authorization_header = line[len('authorization:'):].strip()
            break

    # 处理 Authorization 头的值
    if authorization_header:
        # 在这里处理 authorization 头的值
        print(f'Authorization: {authorization_header}')
        return True
    else:
        print('No Authorization header')
        return False


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

            # 解析请求头
            request_lines = data.decode().split('\r\n')
            request_method = request_lines[0].split()[0]
            request_path = request_lines[0].split()[1]
            # 解析请求参数    
            query_params = parse_qs(urlparse(request_path).query)
            token = query_params.get('token', [None])[0]
            authorization = query_params.get('authorization', [None])[0]
            print(f'request_lines: {request_lines}')
            print(f'request_method: {request_method}')
            print(f'request_path: {request_path}')
            print(f'query_params: {query_params}')
            print(f'token: {token}')
            print(f'authorization: {authorization}')
            auth_flag = handle_request(data)
            print(f'auth_flag is {True if auth_flag else False}')
            # 处理 GET 请求
            if request_method == 'GET' and request_path == '/api/sys/profile' and auth_flag:
                # 构造响应数据
                response_data = {
                    'success': True,
                    'code': 200,
                    'data': {
                        'role': [
                            {
                                'id': '1',
                                'title': '超级管理员'
                            }
                        ],
                        '_id': '612710a0ec87aa543c9c341d',
                        'id': '0',
                        'username': 'super-admin',
                        'title': '超级管理员',
                        'avatar': 'https://m.imooc.com/static/wap/static/common/img/logo-small@2x.png',
                        'permission': {
                            'menus': [
                                'userManage',
                                'roleList',
                                'permissionList',
                                'articleRanking',
                                'articleCreate'
                            ],
                            'points': [
                                'distributeRole',
                                'importUser',
                                'removeUser',
                                'distributePermission'
                            ]
                        }
                    },
                    'message': '获取资料成功'
                }
            else:            
                # 构造 HTTP 的 JSON 响应
                response_data = {
                    'success': True,
                    'code': 10000,
                    'data': {
                        'token': 'd8c6ed7a-3fd4-46e4-a477-b20d1ce9cda0'
                    },
                    'message': '执行成功'
                }
            # 将 JSON 响应序列化为字符串
            response_str = json.dumps(response_data)
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
