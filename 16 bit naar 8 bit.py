from PIL import Image
import os
import numpy as np

# Pad naar je 16-bit röntgenfoto's
input_dir = "D:\\Minor\\Classification\\Pols x-ray\\Data-class"
# Pad voor de geconverteerde 8-bit afbeeldingen
output_dir = "D:/Minor/Classification/Pols x-ray/Data-class/All-images-8bit"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.tif', '.tiff')):  # Pas eventueel aan
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        with Image.open(input_path) as img:
            # Zorg dat het echt een 16-bit afbeelding is
            if img.mode == "I;16":
                # Zet om naar numpy array en normaliseer naar 0-255
                arr = np.array(img)
                arr_8bit = (arr / arr.max() * 255).astype(np.uint8)
                img_8bit = Image.fromarray(arr_8bit, mode="L")
            else:
                # Indien het geen 16-bit is, gewoon converteren naar 8-bit "L"
                img_8bit = img.convert("L")
            
            img_8bit.save(output_path)

print("Alle afbeeldingen zijn omgezet naar 8-bit greyscale!")