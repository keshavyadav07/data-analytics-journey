from pathlib import Path

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time

# Optional desktop notifications:
# Install with: python -m pip install plyer
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False


class WaterReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Drinking Reminder")
        self.root.geometry("430x500")
        self.root.minsize(360, 430)
        self.root.configure(bg="#eef7ff")

        self.running = False
        self.reminder_job = None
        self.interval_minutes = 60

        tk.Label(
            root, text="💧 Water Reminder",
            font=("Segoe UI", 22, "bold"),
            bg="#eef7ff", fg="#075985"
        ).pack(pady=(22, 6))

        tk.Label(
            root, text="A gentle reminder to take a water break",
            font=("Segoe UI", 10), bg="#eef7ff", fg="#475569"
        ).pack(pady=(0, 18))

        card = tk.Frame(root, bg="white", padx=18, pady=18)
        card.pack(fill="x", padx=20, pady=6)

        tk.Label(
            card, text="Remind me every",
            font=("Segoe UI", 12, "bold"),
            bg="white", fg="#0f172a"
        ).pack(anchor="w")

        self.interval_var = tk.StringVar(value="60")
        options = [
            ("15 minutes", "15"),
            ("30 minutes", "30"),
            ("45 minutes", "45"),
            ("60 minutes", "60"),
            ("90 minutes", "90"),
            ("120 minutes", "120"),
        ]

        for label, value in options:
            # Use a dropdown below instead of multiple radio buttons.
            pass

        self.interval_menu = tk.OptionMenu(
            card, self.interval_var,
            *[value for _, value in options]
        )
        self.interval_menu.config(
            font=("Segoe UI", 11), bg="#dbeafe",
            activebackground="#bfdbfe", relief="flat"
        )
        self.interval_menu.pack(fill="x", pady=(8, 4))

        tk.Label(
            card, text="Interval is in minutes (choose 15, 30, 45, 60, 90, or 120).",
            font=("Segoe UI", 9), bg="white", fg="#64748b",
            wraplength=330, justify="left"
        ).pack(anchor="w", pady=(0, 8))

        self.status_label = tk.Label(
            root, text="Status: Stopped",
            font=("Segoe UI", 11, "bold"),
            bg="#eef7ff", fg="#334155"
        )
        self.status_label.pack(pady=14)

        buttons = tk.Frame(root, bg="#eef7ff")
        buttons.pack(pady=4)

        self.start_button = tk.Button(
            buttons, text="Start reminders",
            command=self.start_reminders,
            font=("Segoe UI", 11, "bold"),
            bg="#0284c7", fg="white", activebackground="#0369a1",
            activeforeground="white", relief="flat", padx=16, pady=10
        )
        self.start_button.grid(row=0, column=0, padx=6)

        self.stop_button = tk.Button(
            buttons, text="Stop",
            command=self.stop_reminders,
            font=("Segoe UI", 11, "bold"),
            bg="#e2e8f0", fg="#0f172a",
            activebackground="#cbd5e1", relief="flat",
            padx=16, pady=10, state="disabled"
        )
        self.stop_button.grid(row=0, column=1, padx=6)

        tk.Button(
            root, text="Test notification",
            command=self.test_notification,
            font=("Segoe UI", 10), bg="#dcfce7", fg="#166534",
            relief="flat", padx=14, pady=8
        ).pack(pady=12)

        tk.Label(
            root,
            text="Keep this app open while reminders are running.\n"
                 "Notifications depend on your operating system settings.",
            font=("Segoe UI", 9), bg="#eef7ff", fg="#64748b",
            justify="center"
        ).pack(pady=(6, 12))

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def show_notification(self, title, message):
        # Windows desktop notification when plyer is installed.
        if PLYER_AVAILABLE:
            try:
                notification.notify(
                    title=title,
                    message=message,
                    app_name="Water Reminder",
                    timeout=10
                )
                return
            except Exception:
                pass

        # Fallback: visible popup if desktop notifications aren't available.
        try:
            self.root.after(
                0, lambda: messagebox.showinfo(title, message)
            )
        except tk.TclError:
            pass

    def test_notification(self):
        self.show_notification(
            "💧 Water Reminder",
            "Time for a water break! Have some water if you're thirsty."
        )

    def start_reminders(self):
        try:
            interval = int(self.interval_var.get())
            if interval not in (15, 30, 45, 60, 90, 120):
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid interval", "Please choose a listed interval.")
            return

        self.interval_minutes = interval
        self.running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.interval_menu.config(state="disabled")
        self.status_label.config(
            text=f"Status: Running — every {self.interval_minutes} minutes",
            fg="#15803d"
        )

        # First reminder occurs after the selected interval.
        self.schedule_next()

    def schedule_next(self):
        if self.running:
            self.reminder_job = self.root.after(
                self.interval_minutes * 60 * 1000,
                self.send_reminder
            )

    def send_reminder(self):
        if not self.running:
            return

        self.show_notification(
            "💧 Time for a water break",
            "Pause for a moment and have some water if you're thirsty."
        )
        self.schedule_next()

    def stop_reminders(self):
        self.running = False

        if self.reminder_job is not None:
            try:
                self.root.after_cancel(self.reminder_job)
            except tk.TclError:
                pass
            self.reminder_job = None

        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.interval_menu.config(state="normal")
        self.status_label.config(text="Status: Stopped", fg="#334155")

    def on_close(self):
        self.stop_reminders()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = WaterReminderApp(root)
    root.mainloop()

