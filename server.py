from flask import Flask, request
import ctypes
import os
from PIL import Image

app = Flask(__name__)

def change_wallpaper(image_path):
    """
    Set the Windows desktop wallpaper to the given image.
    Converts image to BMP format as required by Windows API.
    """
    image_path = os.path.abspath(image_path)
    
    # Convert image to BMP (Windows requires BMP for SystemParametersInfoW)
    bmp_path = os.path.splitext(image_path)[0] + ".bmp"
    img = Image.open(image_path)
    img.save(bmp_path, "BMP")
    
    # Apply wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, bmp_path, 3)


@app.route('/set_wallpaper', methods=['POST'])
def set_wallpaper():
    """
    Endpoint to receive wallpaper files from clients and set them as wallpaper.
    """
    if 'file' not in request.files:
        return {"status": "error", "message": "No file provided"}, 400

    file = request.files['file']
    if file.filename == '':
        return {"status": "error", "message": "Empty filename"}, 400

    # -------------------------------
    # CHANGE THIS PATH IF DESIRED
    # Default: Saves wallpapers in a 'wallpapers' folder in the current directory
    # -------------------------------
    save_dir = os.path.join(os.getcwd(), "wallpapers")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, file.filename)

    file.save(save_path)

    try:
        change_wallpaper(save_path)
        return {"status": "success", "message": f"Wallpaper changed to {file.filename}"}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500


if __name__ == "__main__":
    # -------------------------------
    # USER CONFIGURATION
    # -------------------------------
    # host: use "0.0.0.0" to listen on all network interfaces
    # port: change if needed
    HOST = "0.0.0.0"
    PORT = 5000

    app.run(host=HOST, port=PORT)
