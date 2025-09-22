import requests
import os

# -------------------------------
# USER CONFIGURATION
# -------------------------------
# Replace with the IP address of the server (Laptop2)
SERVER_IP = "REPLACE_WITH_SERVER_IP"

# Replace with the port if you changed it on the server (default is 5000)
SERVER_PORT = 5000

# The full URL of the wallpaper server
SERVER_URL = f"http://{SERVER_IP}:{SERVER_PORT}/set_wallpaper"


def send_wallpaper():
    """
    Prompts the user for an image file and sends it to the server
    to set as the remote wallpaper.
    """
    # Ask user for local image path
    image_path = input("Enter the full path of the wallpaper image on your laptop: ").strip()

    # Check if file exists
    if not os.path.isfile(image_path):
        print("File does not exist. Exiting.")
        return

    # Open file and send to server
    with open(image_path, 'rb') as f:
        files = {'file': (os.path.basename(image_path), f)}
        try:
            response = requests.post(SERVER_URL, files=files)
            print("Server response:", response.json())
        except Exception as e:
            print("Error connecting to server:", str(e))


if __name__ == "__main__":
    send_wallpaper()
