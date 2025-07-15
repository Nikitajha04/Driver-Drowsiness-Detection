# import tkinter as tk
# from tkinter import messagebox
# import os

# def start_detection():
#     try:
#         import main
#         main.main()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to start detection:\n{e}")

# def plot_graph():
#     try:
#         import utils.plot_graph
#         utils.plot_graph.plot_graph()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to plot graph:\n{e}")

# def view_logs():
#     try:
#         os.startfile("logs/events.log")
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to open log file:\n{e}")

# def exit_app():
#     if messagebox.askokcancel("Exit", "Do you really want to exit?"):
#         root.destroy()

# root = tk.Tk()
# root.title("Driver Drowsiness Detection System")
# root.geometry("400x300")
# root.configure(bg="#2E4053")

# label = tk.Label(root, text="Driver Drowsiness Detection", font=("Arial", 16, 'bold'), fg="white", bg="#2E4053")
# label.pack(pady=20)

# btn1 = tk.Button(root, text="Start Detection", command=start_detection, width=25, bg="#1ABC9C", fg="white")
# btn1.pack(pady=10)

# btn2 = tk.Button(root, text="Plot Drowsiness Graph", command=plot_graph, width=25, bg="#3498DB", fg="white")
# btn2.pack(pady=10)

# btn3 = tk.Button(root, text="View Event Logs", command=view_logs, width=25, bg="#F39C12", fg="white")
# btn3.pack(pady=10)

# btn4 = tk.Button(root, text="Exit", command=exit_app, width=25, bg="#E74C3C", fg="white")
# btn4.pack(pady=10)

# root.mainloop()

# run command
# py -3.13 "C:\Users\NIKITA_JHA\minor project\driver_drowsiness_detector_project\app_gui.py"


import tkinter as tk
from tkinter import messagebox
import os

# Correct import for plot_graph function
from utils.plot_graph import plot_graph

# Callback to start detection
def start_detection():
    try:
        import main
        main.main()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start detection:\n{e}")

# Callback to plot drowsiness graph
def plot_graph_callback():
    try:
        plot_graph()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to plot graph:\n{e}")

# Callback to view log file
def view_logs():
    try:
        log_file_path = os.path.join("logs", "events.log")
        if os.path.exists(log_file_path):
            os.startfile(log_file_path)
        else:
            messagebox.showwarning("Log Not Found", "The log file does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open log file:\n{e}")

# Callback to exit application
def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

# Initialize main window
root = tk.Tk()
root.title("Driver Drowsiness Detection System")
root.geometry("400x300")
root.configure(bg="#2E4053")
root.resizable(False, False)

# Header label
label = tk.Label(root, text="Driver Drowsiness Detection", font=("Arial", 16, 'bold'), fg="white", bg="#2E4053")
label.pack(pady=20)

# Buttons
btn1 = tk.Button(root, text="Start Detection", command=start_detection, width=25, bg="#1ABC9C", fg="white")
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Plot Drowsiness Graph", command=plot_graph_callback, width=25, bg="#3498DB", fg="white")
btn2.pack(pady=10)

btn3 = tk.Button(root, text="View Event Logs", command=view_logs, width=25, bg="#F39C12", fg="white")
btn3.pack(pady=10)

btn4 = tk.Button(root, text="Exit", command=exit_app, width=25, bg="#E74C3C", fg="white")
btn4.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

