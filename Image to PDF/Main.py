from fpdf import FPDF 
from os import listdir 

path = "C:/Users/soura/Desktop/WIX"
img_list = listdir(path)

img_list.sort()

pdf = FPDF("p","mm","A4")

x = 0
y = 0

w = 210
h = 297

for img in img_list:
    pdf.add_page()
    pdf.image(path + img,x,y,w,h)

pdf.output("Output.pdf","F")