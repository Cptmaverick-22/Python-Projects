from fpdf import FPDF
from PIL import Image
from os import listdir, path as os_path

path = r"C:\Users\soura\Desktop\WIX"
img_list = listdir(path)

img_list.sort()

pdf = FPDF("p", "mm", "A4")

x = 0
y = 0

w = 210
h = 297

for img in img_list:
    img_path = os_path.join(path, img)
    if img.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check if the image is already in a supported format
        pdf.add_page()
        pdf.image(img_path, x, y, w, h)

pdf.output("Output.pdf", "F")
