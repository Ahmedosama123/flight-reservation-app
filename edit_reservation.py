
import tkinter as tk
from database import update
import reservation


class EditReservationPage(tk.Frame):
    def __init__(self, master, data):
        super().__init__(master)

        self.reservation_id = data[0]

        tk.Label(self, text="Edit Reservation", font=("Arial", 16, "bold")).pack(pady=20)

        self.entries = {}
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]

        for i, field in enumerate(fields):
            tk.Label(self, text=field).pack()
            entry = tk.Entry(self)
            entry.insert(0, data[i + 1])
            entry.pack()
            self.entries[field] = entry

        tk.Button(self, text="Update", width=15, bg="#4CAF50", fg="white", command=self.update_reservation).pack(pady=10)
        tk.Button(self, text="Back", width=15, command=self.go_back).pack()

    def update_reservation(self):
        values = [self.entries[f].get() for f in self.entries]
        if all(values):
            update(self.reservation_id, *values)
            self.go_back()

    def go_back(self):
        self.destroy()
        reservations = reservation.ReservationListPage(self.master)
        reservations.pack(fill="both", expand=True)
