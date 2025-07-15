

import tkinter as tk
import home
import database

def main():

    database.connect()
    root = tk.Tk()
    root.title("Flight Reservation System")
    root.geometry("600x400")
    app = home.HomePage(root)
    app.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()
