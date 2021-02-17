from socket import *

def main():
    host =gethostname()
    portno = 8088
    s = socket()
    s.connect((host,portno))
    s.send(b'hello naval')
    msg = s.recv(1024)
    print(msg)
    s.close()

main()
