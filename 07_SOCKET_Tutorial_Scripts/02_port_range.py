import socket

socket.setdefaulttimeout(.5)

print('\n'+ '#'*50+'\n Started Executing Script'+ '\n'+ '#'*50)

def scan_range(ip,sp,ep):
    ep = ep + 1
    print('\n'+'~'*10 + 'Scanning '+ip +'~'*10)
    try:
        for port in range(sp,ep):
            DEVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result_of_check = DEVICE_SOCKET.connect_ex((ip,port))

            if result_of_check == 0:
                print(str(ip)+ ' is Listening on Port ' + str(port))
                DEVICE_SOCKET.close()
            else:
                print(str(ip)+ ' is not listening on Port '+ str(port))
                DEVICE_SOCKET.close()
    except:
        print('Exception occured')

scan_range('192.168.0.10',75,80)
scan_range('192.168.0.1',75,81)


print('\n'+ '#'*50+'\n Finished Executing Script'+ '\n'+ '#'*50)
