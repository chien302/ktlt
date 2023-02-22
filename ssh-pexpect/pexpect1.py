import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
    child.sendline(cmd) 
    child.expect(PROMPT)
    print(child.before) 

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to connect to continue connecting'
    connStr = 'ssh ' + user + '@' + host 
    child = pexpect.spawn(connStr)
    ret  = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 1:
        child.sendline('yes')
        ret = child.expect('password:')
    if ret != 0:
        print ('[-] Error Connecting')
        return 
    child.sendline(password)
    child.expect(PROMPT)
    return child
def main():
    host = '192.169.0.212'
    user = 'chien'
    password = '123456'
    child = connect(user, host, password)
    if child is not None:
        send_command(child)
    else:
        print ("Problem connecting!")

if __name__ == '__main__':
    main()