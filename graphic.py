import tkinter as tk

def grafica():
    window = tk.Tk()
    window.wm_attributes('-fullscreen','true')

    window.geometry("600x600")
    #window.title("Aquarium")
    closebutton = tk.Button(window, text = 'Click and Quit', command=window.quit)
    closebutton.grid(row=0, column=0)

    def quit(self):
        self.root.destroy()

    #connectionDBButton = tk.Button(text="Connetti al DB", command=database_connection)
    #connectionDBButton.grid(row=0,column=0)

    window.mainloop()