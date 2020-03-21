# Directly extract image dimension without saving from jpeg header
from PIL import Image
import urllib.request
import io

raw_image = urllib.request.urlopen("https://jpeg.org/images/jpeg-home.jpg").read()

byteio_image = io.BytesIO(raw_image)

# ffc0 the SOF0 marker -- 2 bytes
# length               -- 2 bytes
# data precision       -- 1 byte
# -------------------------------
#                         5 bytes 
# height and width 2 bytes each
byteio_image.seek(raw_image.index(b'\xff\xc0') + 5)

height = int.from_bytes(byteio_image.read(2), 'big')
width = int.from_bytes(byteio_image.read(2), 'big')

print((width, height))
