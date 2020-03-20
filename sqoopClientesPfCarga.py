import time
from SSHClient import SSHClient

hostNameIp = ""
userName = ""
passWord = ""
privateKey = ""

clientSSH = SSHClient(hostNameIp, userName, passWord, privateKey)
response = clientSSH.sshConnection()
print (response)

response = clientSSH.sshCommand("sqoop import --connect jdbc:mysql://<IP>/bases_teste --username <USER> -password <PASSWD> --table <TABLE_NAME>  --target-dir s3://<PATH>")
print (response)
tempoEspera=600 #segundos
time.sleep(tempoEspera)
response = clientSSH.closeSSHConnection()
print ("Comando sqoop encerrado com sucesso!")