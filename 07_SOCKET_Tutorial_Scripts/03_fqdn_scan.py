import socket

socket.setdefaulttimeout(.5)

print('\n'+ '#'*50+'\n Started Executing Script from '+socket.gethostname()+ '\n'+ '#'*50)

def port_check(ip,port):
    print('~'*20)
    print ('FQDN is  :'+socket.getfqdn(ip))
    try :
        print ('IP is  :'+socket.gethostbyname(ip))
    except :
        print ('Exception occured while getting IP ')
        pass

    try:

        DEVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_of_check = DEVICE_SOCKET.connect_ex((ip,port))

        if result_of_check == 0:
            print(str(ip)+ ' is Listening on Port ' + str(port))
            DEVICE_SOCKET.close()
        else:
            print(str(ip)+ ' is not listening on Port '+ str(port))
            DEVICE_SOCKET.close()
    except socket.gaierror:
            print ('Could not resolve host : '+ ip)
            pass
    except :
            print ('Exception occured')
            pass


port_check('192.168.0.10',80)
port_check('cisco.com',443)
port_check('192.168.0.1',80)
port_check('192.168.0.10',801)

print('\n'+ '#'*50+'\n Finished Executing Script'+ '\n'+ '#'*50)
