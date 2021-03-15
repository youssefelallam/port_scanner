import socket

host = input("Please enter the ip address : ")

try:
    for port in range(1,1024):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((host,port))
        if result == 0:
            name = socket.getservbyport(port)
            print(f"Port {port} {name} is open.")
        s.close()
except:
    pass
