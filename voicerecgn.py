#IMPORTAM BIBLIOTECILE NECESARE DUPA CE LE-AM INSTALAT CU PIP INSTALL
import speech_recognition as sr
import webbrowser as web
import os
#CREAM FUNCTIA PRINCIPALA MAIN
def main():
    #SPECIFICAM SURSA BROWSERULUI PENTRU CAUTARI
    path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

    r=sr.Recognizer()

    with sr.Microphone() as source:
        #PENTRU INDEPARTAREA ZGOMOTULUI DE FUNDAL
        r.adjust_for_ambient_noise(source)

        print("spune ceva")
        #ASCULTA COMANDA
        audio=r.listen(source)

        print("identificare comanda...")

        try:
            #IDENTIFICAM COMANDA UTILIZAND GOOGLE SPEECH SI O DAM UNEI VARIABILE
            dest=r.recognize_google(audio)

            print("ai spus :"+dest)

            #PENTRU A SE PUTEA DESCHIDE VA ROG SA VA MODIFICATI LOCATIA FISIERULUI IN FUNCTIE DE NUMELE UTILIZATORULUI

            #DESCHIDEM NOTEPADUL

            if dest=='notepad':
                 os.startfile('C:/Users/Eduard/Desktop/proiectlp/requirements.txt')

            #DESCHIDEM FISIERUL PRIMIT DE LA MINE
            elif dest=='open lab':
                os.startfile('C:/Users/Eduard/Desktop/proiectlp')
            #DESCHIDEM SKYPE
            elif dest=='call':
                os.startfile('"C:/Program Files (x86)/Microsoft/Skype for Desktop/Skype.exe"')
            #DESCHIDEM ORICE ADRESA DE PE INTERNET CU SPECIFICAREA '.COM '
            #EXEMPLU : facebook.com , google.com etc
            else:
                web.get(path).open(dest)
            #exceptie in cazul in care nu recunoaste comanda
        except Exception as e:
            print("eroare"+str(e))

if __name__=="__main__":
    main()
