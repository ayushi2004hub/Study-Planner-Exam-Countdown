# gui.py (Final UI with proper labels)
import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime, timedelta
import threading
import time

DATA_FILE = 'planner_data.json'
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def calculate_subject_rate(week):
    total = len(week)
    if total == 0:
        return 0
    completed = sum(1 for d in week.values() if d['status'] == 'Done')
    return int((completed / total) * 100)

def run_gui():
    root = tk.Tk()
    root.title("📚 Study Planner")
    root.geometry("1000x600")
    root.configure(bg="white")

    data = load_data()
    subjects = list(data.keys())

    def refresh_subjects():
        nonlocal data, subjects
        data = load_data()
        subjects = list(data.keys())
        subject_cb['values'] = subjects
        countdown_cb['values'] = subjects
        update_table()

    def add_exam():
        sub = subject_entry.get().strip()
        date = date_entry.get().strip()
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except:
            messagebox.showerror("Invalid Date", "Use format DD-MM-YYYY")
            return
        if sub in data:
            messagebox.showinfo("Exists", "Subject already exists.")
            return
        data[sub] = {
            "exam_date": date,
            "weekly_plan": {day: {"task": "", "status": "Not Done"} for day in days}
        }
        save_data(data)
        subject_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        refresh_subjects()

    def update_task():
        sub = subject_cb.get()
        day = day_cb.get()
        task = task_entry.get().strip()
        if sub and day and task:
            data[sub]["weekly_plan"][day]["task"] = task
            data[sub]["weekly_plan"][day]["status"] = "Not Done"
            save_data(data)
            update_table()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Fill all fields.")

    def mark_done():
        sub = subject_cb.get()
        day = day_cb.get()
        if sub and day:
            data[sub]["weekly_plan"][day]["status"] = "Done"
            save_data(data)
            update_table()
        else:
            messagebox.showerror("Error", "Select subject & day.")

    def update_table():
        for row in table.get_children():
            table.delete(row)
        for sub, details in data.items():
            week = details["weekly_plan"]
            row = [sub]
            for day in days:
                t = week[day]["task"]
                s = week[day]["status"]
                row.append(f"{t}\n({s})" if t else "")
            row.append(f"{calculate_subject_rate(week)}%")
            table.insert("", "end", values=row)

    def show_countdown():
        sub = countdown_cb.get()
        if sub not in data:
            messagebox.showerror("Error", "Select subject.")
            return
        try:
            edate = datetime.strptime(data[sub]["exam_date"], "%d-%m-%Y")
            diff = edate - datetime.now()
            d, h, m = diff.days, diff.seconds // 3600, (diff.seconds % 3600) // 60
            messagebox.showinfo("Countdown", f"{sub} exam in: {d}d {h}h {m}m")
        except:
            messagebox.showerror("Error", "Invalid date format in data.")

    def start_alert():
        def checker():
            while True:
                for sub, details in data.items():
                    try:
                        edate = datetime.strptime(details["exam_date"], "%d-%m-%Y")
                        if 0 <= (edate - datetime.now()).days <= 1:
                            root.after(0, lambda s=sub: messagebox.showwarning("Alert", f"{s} exam is today/tomorrow!"))
                    except: pass
                time.sleep(3600)
        threading.Thread(target=checker, daemon=True).start()

    # Labels for clarity
    tk.Label(root, text="Subject Name", bg="white").grid(row=0, column=0)
    subject_entry = tk.Entry(root, width=20)
    subject_entry.grid(row=1, column=0, padx=5, pady=2)

    tk.Label(root, text="Exam Date (DD-MM-YYYY)", bg="white").grid(row=0, column=1)
    date_entry = tk.Entry(root, width=20)
    date_entry.grid(row=1, column=1, padx=5, pady=2)

    add_btn = tk.Button(root, text="Add Exam", bg="lightgreen", command=add_exam)
    add_btn.grid(row=1, column=2, padx=10)

    tk.Label(root, text="Select Subject", bg="white").grid(row=2, column=0)
    subject_cb = ttk.Combobox(root, values=subjects, width=18, state="readonly")
    subject_cb.grid(row=3, column=0)

    tk.Label(root, text="Select Day", bg="white").grid(row=2, column=1)
    day_cb = ttk.Combobox(root, values=days, width=18, state="readonly")
    day_cb.grid(row=3, column=1)

    tk.Label(root, text="Task for that Day", bg="white").grid(row=2, column=2)
    task_entry = tk.Entry(root, width=30)
    task_entry.grid(row=3, column=2)

    tk.Button(root, text="Add/Edit Task", bg="skyblue", command=update_task).grid(row=3, column=3)
    tk.Button(root, text="Mark Done", bg="orange", command=mark_done).grid(row=3, column=4)

    tk.Label(root, text="Countdown", bg="white").grid(row=4, column=0, pady=10)
    countdown_cb = ttk.Combobox(root, values=subjects, width=18, state="readonly")
    countdown_cb.grid(row=5, column=0)
    tk.Button(root, text="Show Countdown", command=show_countdown).grid(row=5, column=1)

    # Table
    cols = ["Subject"] + days + ["% Done"]
    table = ttk.Treeview(root, columns=cols, show="headings", height=12)
    for col in cols:
        table.heading(col, text=col)
        table.column(col, anchor="center", width=100)
    table.grid(row=6, column=0, columnspan=6, padx=10, pady=10)

    update_table()
    start_alert()
    root.mainloop()

if __name__ == '__main__':
    run_gui()
