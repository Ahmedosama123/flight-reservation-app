

import tkinter as tk
from booking import BookingPage
from reservation import ReservationListPage


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        title = tk.Label(self, text="Flight Reservation System", font=("Arial", 20, "bold"))
        title.pack(pady=40)


        btn_book = tk.Button(self, text="Book Flight", width=20, height=2, bg="#4CAF50", fg="white",
                             command=lambda: self.open_booking())
        btn_book.pack(pady=10)

        btn_view = tk.Button(self, text="View Reservations", width=20, height=2, bg="#2196F3", fg="white",
                             command=lambda: self.open_reservations())
        btn_view.pack(pady=10)

    def open_booking(self):
        self.destroy()
        booking_page = BookingPage(self.master)
        booking_page.pack(fill="both", expand=True)

    def open_reservations(self):
        self.destroy()
        reservations_page = ReservationListPage(self.master)
        reservations_page.pack(fill="both", expand=True)
