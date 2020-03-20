
import time
from SSHClient import SSHClient

hostNameIp = ""
userName = ""
passWord = ""
privateKey = ""

clientSSH = SSHClient(hostNameIp, userName, passWord, privateKey)
response = clientSSH.sshConnection()
print (response)

response = clientSSH.sshCommand("mkdir <path>")
print (response)

tempoEspera = 60 #segundos
time.sleep(tempoEspera)

response = clientSSH.closeSSHConnection()
print (response)