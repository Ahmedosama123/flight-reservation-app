

import tkinter as tk
from tkinter import ttk
from database import view_all, delete
from edit_reservation import EditReservationPage
import home

class ReservationListPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Reservations", font=("Arial", 16, "bold")).pack(pady=10)

        columns = ("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=90)
        self.tree.pack(pady=10, fill="x")

        self.load_data()

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Edit", width=12, bg="#FFC107", command=self.edit_selected).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete", width=12, bg="#F44336", fg="white", command=self.delete_selected).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Back", width=12, command=self.go_back).pack(side="left", padx=5)

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in view_all():
            self.tree.insert("", "end", values=row)

    def edit_selected(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            self.destroy()
            edit_page = EditReservationPage(self.master, values)
            edit_page.pack(fill="both", expand=True)

    def delete_selected(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            delete(values[0])
            self.load_data()

    def go_back(self):
        self.destroy()
        home_page = home.HomePage(self.master)
        home_page.pack(fill="both", expand=True)
