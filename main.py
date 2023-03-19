from tkinter import *
import requests
from tkinter import messagebox,filedialog


root = Tk()
root.title('Server Client')
root.geometry("800x400")
root.config(bg="#434445")
root.resizable(0,0)
TOKEN = ""

SERVER_ADDRESS = "http://192.168.200.121:8000"
#SERVER_ADDRESS = "http://127.0.0.1:8000"

def get_message():
    data = requests.get(SERVER_ADDRESS + "/message", headers={"token": TOKEN}).json()
    #messagebox.showinfo("Dane", data)
    Wiadomosci.delete(1.0,END)
    if "messages" not in data:
        messagebox.showerror(message=data["message"])
    else:
        messages = data["messages"]
        Wiadomosci.insert(END, "\n".join(messages))





get_button = Button(root, text ="Odbierz wiadomości", command = get_message,width=33,fg="white",font=("Helvetica","8","bold"),bg="#18587d")
get_button.place(x=550,y=360)

MessageInput = Entry(root,bg="#383a3b",fg="white",width=17,font=("Helvetica","15","bold"))
MessageInput.place(x=320,y=65)

DataInput = Entry(root,bg="#383a3b",fg="white",width=17,font=("Helvetica","15","bold"))
DataInput.place(x=320,y=220)

LoginLabel1 = Label(root,text="User Name:",bg="#202224",fg="white",font=("Helvetica","10","bold"),bd="1px").place(x=15,y=50)
LoginLabel2 = Label(root,text=" Password: ",bg="#202224",fg="white",font=("Helvetica","10","bold"),bd="1px").place(x=15,y=75)
LoginLabel3 = Label(root,text="Login",bg="#434445",fg="white",font=("Helvetica","20","bold"),bd="1px").place(x=130,y=10)


RegisterLabel1 = Label(root,text="User Name:",bg="#202224",fg="white",font=("Helvetica","10","bold"),bd="1px").place(x=15,y=200)
RegisterLabel2 = Label(root,text=" Password: ",bg="#202224",fg="white",font=("Helvetica","10","bold"),bd="1px").place(x=15,y=225)
RegisterLabel3 = Label(root,text="Register",bg="#434445",fg="white",font=("Helvetica","20","bold"),bd="1px").place(x=110,y=160)


RegisterUser = Entry(root,bg="aqua",width=25,font=("Helvetica","10","bold"))
RegisterUser.place(x=90,y=200)

RegisterPass = Entry(root,bg="aqua",show="*",width=25,font=("Helvetica","10","bold"))
RegisterPass.place(x=90,y=225)



LoginUser = Entry(root,bg="aqua",width=25,font=("Helvetica","10","bold"))
LoginUser.place(x=90,y=50)

LoginPass = Entry(root,bg="aqua",show="*",width=25,font=("Helvetica","10","bold"))
LoginPass.place(x=90,y=75)


def send_message():
    text = MessageInput.get()
    body = {
        "message": text
    }
    response = requests.post(SERVER_ADDRESS + "/send-message", json=body, headers={"token": TOKEN})
    messagebox.showinfo("Wynik", response.json()["message"])
    get_message()


def send_date():
    text = MessageInput.get()
    body = {
        "message": f"set-notification {DataInput.get()} {text}"
    }
    response = requests.post(SERVER_ADDRESS + "/send-message", json=body, headers={"token": TOKEN})
    messagebox.showinfo("Wynik", response.json()["message"])
    get_message()


def zatwierdzRegister():
    global TOKEN
    username = RegisterUser.get()
    password = RegisterPass.get()
    if username == "" or password == "" or (username == "" and password == ""):
        messagebox.showerror("ERROR","nie poprawne dane")
    else:
        body = {
            "username": username,
            "password": password
        }
        response = requests.post(SERVER_ADDRESS + "/register", json=body)
        data = response.json()
        messagebox.showinfo("Wynik", data["message"])
        if "token" in data:
            TOKEN = data["token"]
        RegisterUser.delete(0, END)
        RegisterPass.delete(0, END)


def zatwierdzLogin():
    global TOKEN
    username = LoginUser.get()
    password = LoginPass.get()
    body = {
        "username": username,
        "password": password
    }
    response = requests.post(SERVER_ADDRESS + "/login", json=body)
    data = response.json()
    messagebox.showinfo("Wynik", data["message"])
    if "token" in data:
        TOKEN = data["token"]


send_button = Button(root, text ="Podaj Nazwe", command = send_message,width=23,fg="white",font=("Helvetica","10","bold"),bg="#18587d")
send_button.place(x=320,y=95)

send_DataButton = Button(root, text ="Potwierdz date", command = send_date,width=23,fg="white",font=("Helvetica","10","bold"),bg="#18587d")
send_DataButton.place(x=320,y=250)



get_button1 = Button(root, text ="Zaloguj",width=24, command = zatwierdzLogin,fg="white",font=("Helvetica","8","bold"),bg="#18587d")
get_button1.place(x=90,y=98)

get_button2 =Button(root, text ="Zarejestruj sie",width=24, command = zatwierdzRegister,fg="white",font=("Helvetica","8","bold"),bg="#18587d")
get_button2.place(x=90,y=248)

info = Label(root,text="Produkty",width=30,fg="white",font=("Helvetica","18","bold"),bg="#434445").place(x=440,y=20)
DataInfo1 = Label(root,text="Podaj Date Ważności",width=30,fg="white",font=("Helvetica","14","italic"),bg="#434445").place(x=250,y=170)
DataInfo2 = Label(root,text="Dzien-Miesiac-Rok",width=30,fg="lightgray",font=("Helvetica","10","bold"),bg="#434445").place(x=290,y=198)

Wiadomosci = Text(root,width=30,fg="white",height=18,bg="#383a3b")
Wiadomosci.place(x=550, y=60)



root.mainloop()