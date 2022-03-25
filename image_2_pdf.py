import os
from fpdf import FPDF

Pdf = FPDF()list_of_images = ["1.jpg", "2.jpg"]
for i in list_of_images: # list of images
    Pdf.add_page()
    Pdf.image(i,x,y,w,h)
Pdf.output("yourfile.pdf", "F")