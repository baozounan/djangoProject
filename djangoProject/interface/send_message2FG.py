import socket
import time


def get_csv_message(csv_path,frequency,ip,port):
    print(ip)
    print(port)
    if frequency<=0:
        frequency=20

    with open(csv_path,'r') as f:
        while (f.readline()):
            data=f.readline()
            print(data)
            udp_send_message(data,ip,port)
            time.sleep(1/frequency)

def udp_send_message(data,ip,port):
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #可以使用套接字收发数据
    udp_socket.sendto(data.encode("UTF-8"),(ip,port))
    #关闭套接字
    udp_socket.close()




