import tkinter as tk
from tkinter import messagebox
from Attacks.manage_attacks import *




def setup_gui():
    def start_attack_wrapper():
        # Get values from entry fields
        target = target_entry.get().strip()
        port = port_entry.get().strip()
        attack_type = attack_type_var.get().strip()
        payload = payload_entry.get().strip()
        interval = interval_entry.get().strip()
        num_threads = num_threads_entry.get().strip()

        # Call the start_attack function with arguments
        start_attack(target, port, attack_type, payload, interval, num_threads)
    
    root = tk.Tk()
    root.title("DDoS Simulation Tool")

    # Dark theme configuration
    dark_bg = "#2E2E2E"
    dark_fg = "#FFFFFF"

    # Input fields
    tk.Label(root, text="Target IP/Domain:", bg=dark_bg, fg=dark_fg).grid(row=0, column=0, sticky="e")
    target_entry = tk.Entry(root)
    target_entry.grid(row=0, column=1, columnspan=2, sticky="w")

    tk.Label(root, text="Port:", bg=dark_bg, fg=dark_fg).grid(row=1, column=0, sticky="e")
    port_entry = tk.Entry(root)
    port_entry.grid(row=1, column=1, columnspan=2, sticky="w")

    tk.Label(root, text="Attack Type:", bg=dark_bg, fg=dark_fg).grid(row=2, column=0, sticky="e")
    attack_type_var = tk.StringVar()
    tk.Radiobutton(root, text="TCP", variable=attack_type_var, value='TCP', bg=dark_bg, fg=dark_fg, selectcolor=dark_bg).grid(row=2, column=1)
    tk.Radiobutton(root, text="HTTP", variable=attack_type_var, value='HTTP', bg=dark_bg, fg=dark_fg, selectcolor=dark_bg).grid(row=2, column=2)
    tk.Radiobutton(root, text="HTTPS", variable=attack_type_var, value='HTTPS', bg=dark_bg, fg=dark_fg, selectcolor=dark_bg).grid(row=2, column=3)

    tk.Label(root, text="Payload:", bg=dark_bg, fg=dark_fg).grid(row=3, column=0, sticky="e")
    payload_entry = tk.Entry(root)
    payload_entry.grid(row=3, column=1, columnspan=2, sticky="w")

    tk.Label(root, text="Interval (seconds):", bg=dark_bg, fg=dark_fg).grid(row=4, column=0, sticky="e")
    interval_entry = tk.Entry(root)
    interval_entry.grid(row=4, column=1, columnspan=2, sticky="w")

    tk.Label(root, text="Number of Threads:", bg=dark_bg, fg=dark_fg).grid(row=5, column=0, sticky="e")
    num_threads_entry = tk.Entry(root)
    num_threads_entry.grid(row=5, column=1, columnspan=2, sticky="w")
    print(port_entry)
    tk.Button(root, text="Start Attack 🚀", command=start_attack_wrapper, bg="#4CAF50", fg=dark_fg).grid(row=6, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Stop Attack 🛑", command=stop_attack, bg="#F44336", fg=dark_fg).grid(row=6, column=2, columnspan=2, pady=10)

    root.configure(bg=dark_bg)
    root.mainloop()
