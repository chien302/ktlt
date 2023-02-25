import optparse
from pexpect import pxssh

class Client:
    def __init__(self, host, user, password): 
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()
    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] error connecting')
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before
def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print('[*] output from ' + client.host)
        print('[+] '+str(output, encoding='utf-8')+ '\n')

def add_client(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

botNet = []

add_client('192.168.0.171', 'chien', '123456')
botnetCommand('uname -v')
        
        
