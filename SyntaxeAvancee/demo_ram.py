import os 
from PIL import Image 

dossier = "C:/Users/PaulE/Documents/DataSet/AbstractArt"

images = []
for img_name in os.listdir(dossier):
    if img_name.endswith(".jpg"):
        img_path = os.path.join(dossier, img_name)
        
        print(img_path)
        images.append(Image.open(img_path))
    
for index, img in enumerate(images):
    img.save(os.path.join(dossier, "tmp", f"{index}.jpg"))

