from tkinter import *

def invia():
    name=nome.get()   
    Targhetta5.config(text=f"Grazie per averci scelto  , {name}!")


root=Tk()

Targhetta=Label(root,text="Pagina di registrazione ")
Targhetta1=Label(root,text="Inserisci il nome  ")
nome=Entry(root)
Targhetta2=Label(root,text="Inserisci il telefono  ")
telefono=Entry(root)
Targhetta3=Label(root,text="Inserisci il cognome  ")
cognome=Entry(root)
Targhetta4=Label(root,text="Inserisci  l'email  ")


email=Entry(root)
Targhetta.pack()
Targhetta1.pack()
nome.pack()
Targhetta2.pack()
telefono.pack()
Targhetta3.pack()
cognome.pack()

Targhetta4.pack()
email.pack()
invi=Button(root,text="Invia", command=invia)
Targhetta5=Label(root,text="")
invi.pack()
Targhetta5.pack()
root.title("Registrati")

root.mainloop()