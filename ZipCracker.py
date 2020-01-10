import zipfile
import itertools
import string
from threading import Thread


def bruteforce():
    path = input("Bitte Pfad angeben: ")
    zipFile = zipfile.ZipFile(path)
    minlengh = int(input("Bitte minimale länge des Paswords angeben: "))
    maxlengh = int(input("Bitte maximale Länge des Passwords eingeben: "))
    myLetters = string.ascii_letters + string.digits + string.punctuation
    for i in range(minlengh, maxlengh):
        for j in map(''.join, itertools.product(myLetters, repeat=i)):
            t = Thread(target=crack,args=(zipFile, j))
            t.start()
            #print(j)

def dictionary():
    path = input("Bitte Pfad angeben: ")
    zipFile = zipfile.ZipFile(path)
    passwords = open("cain.txt")
    for line in passwords.readlines():
        pwd = line.strip("\n")
        t = Thread(target=crack, args=(zipFile, pwd))
        t.start()

def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print("Erfolg das Password ist: " + pwd)
    except:
        pass

#zipFile = zipfile.ZipFile(path)
#zipFile = zipfile.ZipFile("geheim.zip")

