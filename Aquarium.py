import tkinter as tk
from MySqlHandle import addItem, connection, close, createTable, retrieveData

window = tk.Tk()
window.geometry("600x600")
window.title("Aquarium")

def database_connection():
    print("connection...")
    connection()

def database_close():
    print("closing...")
    close()  
    print("closed")

def database_create():
    print("creating...")
    createTable()  
    print("created")  

def database_add():
    print("adding...")
    addItem()  
    print("added") 

def database_Retrive():
    print("retrievein...")
    retrieveData()  
    print("retrieved") 


connectionDBButton = tk.Button(text="Connetti al DB", command=database_connection)
connectionDBButton.grid(row=0,column=0)

closeDBButton = tk.Button(text="Chiudi al DB", command=database_close)
closeDBButton.grid(row=1,column=0)

createDBButton = tk.Button(text="crea al DB", command=database_create)
createDBButton.grid(row=2,column=0)

addDBButton = tk.Button(text="aggiungi al DB", command=database_add)
addDBButton.grid(row=3,column=0)

retrieveDBButton = tk.Button(text="retrive al DB", command=database_Retrive)
retrieveDBButton.grid(row=4,column=0)

if __name__ == "__main__":
    window.mainloop()