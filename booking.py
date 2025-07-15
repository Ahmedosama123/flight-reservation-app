

import tkinter as tk
from database import insert
import home

class BookingPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Book a Flight", font=("Arial", 16, "bold")).pack(pady=20)

        self.entries = {}
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]

        for field in fields:
            tk.Label(self, text=field).pack()
            entry = tk.Entry(self)
            entry.pack()
            self.entries[field] = entry

        tk.Button(self, text="Submit", bg="#4CAF50", fg="white", width=15, command=self.submit).pack(pady=10)
        tk.Button(self, text="Back", command=self.go_back).pack()

    def submit(self):
        values = [self.entries[f].get() for f in self.entries]
        if all(values):
            insert(*values)
            self.go_back()

    def go_back(self):
        self.destroy()
        home_page = home.HomePage(self.master)
        home_page.pack(fill="both", expand=True)
