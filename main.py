import tkinter
import requests
from tkinter import messagebox


root = tkinter.Tk()
root.title('Server Client')
root.geometry("600x400")


def get_message():
    data = requests.get("http://127.0.0.1:8000/message").text
    messagebox.showinfo("Dane", data)


get_button = tkinter.Button(root, text ="Odbierz wiadomości", command = get_message)

get_button.place(x=320,y=30)

MessageInput = tkinter.Entry(root,bg="aqua",font=("Helvetica","10","bold"))
MessageInput.place(x=320,y=50)

LoginLabel1 = tkinter.Label(root,text="User Name:",bg="turquoise",font=("Helvetica","10","bold"),bd="1px").place(x=15,y=50)
LoginLabel2 = tkinter.Label(root,text=" Password: ",bg="turquoise",font=("Helvetica","10","bold"),bd="1px").place(x=15,y=75)
LoginLabel3 = tkinter.Label(root,text="Login",bg="deepskyblue",font=("Helvetica","20","bold"),bd="1px").place(x=110,y=10)




LoginUser = tkinter.Entry(root,bg="aqua",width=25,font=("Helvetica","10","bold"))
LoginUser.place(x=90,y=50)

LoginPass = tkinter.Entry(root,bg="aqua",width=25,font=("Helvetica","10","bold"))
LoginPass.place(x=90,y=75)


def send_message():
    text = MessageInput.get()
    body = {
        "author": "ja",
        "message": text
    }
    response = requests.post("http://127.0.0.1:8000/send-message", json=body)
    messagebox.showinfo("Wynik", str(response))


def zatwierdzUser():
    return "ok"

def zatwierdzPass():
    return "ok"



send_button = tkinter.Button(root, text ="Wyślij wiadomość", command = send_message)
send_button.place(x=320,y=70)

get_button = tkinter.Button(root, text ="✔", command = zatwierdzUser,fg="white",font=("Helvetica","8","bold"),bg="green").place(x=270,y=47)

root.mainloop()