from PIL import Image
import os
import numpy as np
#Path to your images
input_dir = "D:\\Minor\\Classification\\Pols x-ray\\Data-class"
#Path where you want your new images to go
output_dir = "D:/Minor/Classification/Pols x-ray/Data-class/All-images-8bit"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.tif', '.tiff')): 
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        with Image.open(input_path) as img:
        
            if img.mode == "I;16":
                
                arr = np.array(img)
                arr_8bit = (arr / arr.max() * 255).astype(np.uint8)
                img_8bit = Image.fromarray(arr_8bit, mode="L")
            else:
              
                img_8bit = img.convert("L")
            
            img_8bit.save(output_path)

print("Alle afbeeldingen zijn omgezet naar 8-bit greyscale!")
