# -*- coding:utf-8 -*-

import socket,thread

address = ('127.0.0.1', 1234)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
def log_data(data):
    print data
while True:
    data, addr = s.recvfrom(1024)
    thread.start_new_thread(log_data, (data,))


s.close()