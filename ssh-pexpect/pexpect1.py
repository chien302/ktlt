import pexpect
import sys
PROMPT = ['# ','>>> ','> ','\$ ']

def send_command(child, cmd):
        child.sendline(cmd)
        child.expect(PROMPT)
        print (child.before)

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password', pexpect.EOF])
    if ret == 0:
            print ('[-] Error Connecting')
            return
    if ret == 1:
            child.sendline('yes')
            ret = child.expect([pexpect.TIMEOUT, 'password', pexpect.EOF])
            if ret == 0:
                    print ('[-] ERROR Connecting')
                    return
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
        host = '192.168.0.171'
        user = 'chien'
        password = '123456'
        child = connect(user, host , password)
        # send_command(child, 'uname -a')
        child.interact()


if __name__ == '__main__':
        main()