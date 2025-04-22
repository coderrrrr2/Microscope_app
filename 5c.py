import tkinter as tk

from backend.models import save_specimen, create_table

def calculate_actual_size(microscope_size, magnification):
    if magnification == 0:
        raise ValueError("Magnification cannot be zero.")
    return microscope_size / magnification


def submit():
    username = username_entry.get()
    size = float(microscope_entry.get())
    mag = float(magnification_entry.get())
    actual = calculate_actual_size(size, mag)
    save_specimen(username, size, mag, actual)
    result_label.config(text=f"Actual size: {actual:.2f} mm")

create_table()
root = tk.Tk()
root.title("Microscope Calculator")

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Microscope Size (mm)").pack()
microscope_entry = tk.Entry(root)
microscope_entry.pack()

tk.Label(root, text="Magnification").pack()
magnification_entry = tk.Entry(root)
magnification_entry.pack()

tk.Button(root, text="Calculate", command=submit).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
