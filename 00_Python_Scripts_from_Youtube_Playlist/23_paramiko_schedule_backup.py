
import paramiko
import time
import datetime
import schedule

def BACKUP():
    TNOW = datetime.datetime.now().replace(microsecond=0)

    username = 'admin'
    password = 'admin'


    DEVICE_LIST = open ('09_devices')
    for RTR in DEVICE_LIST:
        RTR = RTR.strip()
        print ('\n #### Initiating the backup of device ' + RTR + '#### at ' + str(TNOW) )
        SESSION = paramiko.SSHClient()
        SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        SESSION.connect(RTR,port=22,
                        username=username,
                        password=password,
                        look_for_keys=False,
                        allow_agent=False)

        DEVICE_ACCESS = SESSION.invoke_shell()
        DEVICE_ACCESS.send(b'terminal len 0\n')
        DEVICE_ACCESS.send(b'show run\n')

        time.sleep(5)
        output = DEVICE_ACCESS.recv(65000)
        print (output.decode('ascii'))
        SAVE_FILE = open('ROUTER_' + RTR + str(TNOW), 'w')
        SAVE_FILE.write(output.decode('ascii'))
        SAVE_FILE.close()

        SESSION.close()

schedule.every().minute.at(":00").do(BACKUP)
while True:
    schedule.run_pending()
    time.sleep(1)

