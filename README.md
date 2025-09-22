# Remote-Wallpaper-Changer

**Remote-Wallpaper-Changer** is a Python project that allows you to **remotely change the desktop wallpaper** of a Windows machine over a local network. It uses a **client-server setup** where the server runs on the target machine and authorized clients can send images to update the wallpaper automatically.

---

## Features
- Remotely update wallpapers without physically accessing the target machine  
- Client-server architecture using Python and Flask  
- Upload and set images from the client machine  
- Lightweight and easy to set up  
- Permission-based and safe for controlled environments  

---

## Requirements
- Python 3.x  
- Flask  
- Requests  
- Pillow  

Install dependencies using:
```bash
pip install -r requirements.txt
Setup
Server (Target Machine)

Place server.py on the target Windows machine.

Run the server:

python server.py


The server listens on http://<server_IP>:5000 for incoming wallpaper requests.

Client (Your Machine)

Place client.py on your machine.

Open client.py and replace the placeholders:

SERVER_IP → IP of the server machine

SERVER_PORT → Port if different from 5000

IMAGE_PATH → Path to your wallpaper image

Run the client:

python client.py


Enter the full path of the wallpaper image if prompted.

The wallpaper will update on the server machine automatically.

Usage Notes

Ensure both machines are on the same network (or configure for remote access).

Only use with explicit permission from the target user.

Supports any Windows-compatible image file.

Future Improvements

Remote access over the internet

Scheduled wallpaper changes

Cross-platform support (Linux/macOS)

Web interface for easier image uploads

Contributing / Suggestions

This is a basic project intended for learning and experimentation with Python, client-server communication, and remote automation.

I am open to upgrades and improvements, so if you have any ideas, suggestions, or enhancements — feel free to open an issue or submit a pull request. Any contributions or feedback are highly appreciated!
