import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://images8.alphacoders.com/431/431350.png")
print("Staus Code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image1." + image.format
try:
    image.save(path, image.format)

except IOError:
    print("Cannot save image.")
