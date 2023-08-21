import socket

import sys

Tcp_ip = '127.0.0.1'
Tcp_port = 9999
Buffer_size = 1024
Message = "Hello World"

try:
    tcp_connect=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error as e:
    print("An Error occured while connecting"+ e[0] + "Error Message:"+e[1])
    sys.exit()
    
tcp_connect.connect((Tcp_ip,Tcp_port))


try:
    tcp_connect.send(Message.encode("utf-8"))
    tcp_connect.send(b'WCDCDVFSVFVDSVDSVDVFDVGBHT')
    
except socket.error as e:
    print ("error occured while sending message" + e )
    
print("Message successfully sent")


reply=tcp_connect.recv(1024)
print ("Message gotten from the server",reply)

tcp_connect.close()
sys.exit()



    
        