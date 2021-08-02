import tkinter as tk
from MySqlHandle import connection

window = tk.Tk()
window.geometry("600x600")
window.title("Aquarium")

def database_connection():
    print("connection...")
    connection()
    

    



connectionDBButton = tk.Button(text="Connetti al DB", command=database_connection)
connectionDBButton.grid(row=0,column=0)

if __name__ == "__main__":
    window.mainloop()