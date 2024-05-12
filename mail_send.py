from text_speech import speak
import speech_recognition as sr
import smtplib
from email.message import EmailMessage

listenser = sr.Recognizer()

def mic():
    with sr.Microphone() as source:
        print("program is listening....")
        voice = listenser.listen(source)
        data = listenser.recognize_google(voice)
        print(data)
        return data.lower()

def send_mail(receiver,subject,body):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("csnobel2001@gmail.com","uzkzdixgjwizmhth")
    email = EmailMessage()
    email["From"] = "csnobel2001@gmail.com"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(body)
    server.send_message(email)


dict = {"binil":"binilvb08@gmail.com"}
def main_poc():
    speak("Whom do you want to send?")
    name = mic()
    receiver = dict[name]
    speak("What is the subject of the mail?")
    subject = mic()
    speak("What is the content of the mail?")
    body = mic()
    send_mail(receiver,subject,body)
    speak("Your mail has been send successfully!!!")

# main_poc()