# 🖥️ Key Log Simulator

A Python-based keylogger simulation tool for educational purposes, consisting of a server and client. The client captures keystrokes and sends them to the server over a TCP connection. Features a neon-colored CLI and ethical use disclaimer.

**⚠️ Disclaimer:** This tool is for training and educational purposes ONLY. Unauthorized use is illegal and unethical.

---

## 🚀 Features
✅ **Server Mode:** Listens for incoming connections and displays keylogs in real-time  
✅ **Client Mode:** Captures keystrokes and sends them to the server  
✅ **Ethical Use Prompt:** Displays a mandatory disclaimer before proceeding  
✅ **Reverse TCP Connection:** Ensures secure client-server communication  
✅ **Special Key Handling:** Captures keys like `Space`, `Enter`, and `Backspace`  
✅ **Vibrant CLI:** Neon-colored interface with animated banner  

---

## 📋 Prerequisites
- Python 3.8 or higher  
- **Windows:** Install [Npcap](https://npcap.com/#download) for packet capturing  
- **Linux:** Run with `sudo` for interface access  
- Network access between client and server (same network or port forwarding)  

---

## 💻 Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/NeospectraX/PRODIGY_CS_04.git
cd key-log-simulator
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

---

## 🟡 Usage

### 1. Run the Server
- **File:** `server.py`
- **Command:**
```bash
python server.py
```
- **Prompt:**
```
Enter port to listen on: 4444
```
- **Output:**
```
[+] Waiting for connection on 0.0.0.0:4444...
[+] Connection established from ('192.168.1.100', 54321)
```

### 2. Run the Client
- **File:** `client.py`
- **Command:**
```bash
python client.py
```
- **Prompts:**
```
[!] This is a keylogger simulation for educational and training purposes ONLY.
[!] Do not misuse this knowledge. Unauthorized access is illegal.
Do you agree to continue? (yes/no): yes
Enter server IP for reverse connection: 192.168.1.10
Enter server port: 4444
```
- **Output:**
```
[+] Connected to 192.168.1.10:4444
```
- Keystrokes will appear on the server in real-time.

---

## 📊 Example Output
**Server:**
```
h e l l o  [SPACE] w o r l d  [ENTER]
[BACKSPACE]  [SPACE] t e s t
```

---

## 🧩 How It Works
- **Server:** Binds to `0.0.0.0` (all interfaces) on a user-specified port and listens for client connections. Displays received keylogs.  
- **Client:** Connects to the server’s IP and port, captures keystrokes using `pynput`, and sends them over TCP.  
- **Communication:** Uses a reverse TCP connection (client initiates connection to server).  

---

## ❗ Important Notes
✅ **Permissions:** Run server on a port > 1024 to avoid admin/root requirements.  
✅ **Network:** Ensure the server IP is reachable from the client (check firewall/port settings).  
✅ **Termination:** Press `Ctrl+C` to stop either program safely.  
✅ **Ethics:** Only use with explicit consent on systems you own or are authorized to test.  

---

## 🛠️ Troubleshooting
- **Connection Failed:** Verify server IP, port, and network connectivity. Ensure the server is running first.  
- **No Output:** Check if the client connected successfully (server will log it).  
- **Port in Use:** Choose a different port if you get a binding error.  

---

## 📝 License
This project is licensed under the **MIT License**.

💬 _Developed by Ashok (Nickname: NeospectraX). Contributions are welcome!_

