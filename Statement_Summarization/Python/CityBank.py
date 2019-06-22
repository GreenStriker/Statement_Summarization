import cv2
import numpy as np
import pytesseract
from wand.image import Image
from wand.color import Color
import re
import fileinput
# from PyPDF2 import PdfFileReader
import PyPDF2

# Path of working folder on Disk
# src_path = "C:\Demo"
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

######################### Imagic Magick ##########################

# Getting pdf pagge number

# pdf = PyPDF2.PdfFileReader(open('PDF/test.pdf','rb'))
# number = pdf.getNumPages()
# page = pdf.getPage(0)
# print(number)
# print(page)

with Image(filename='PDF/cityBank-pages-1.pdf', resolution=200) as img:
    print("Processing...........")
    img.compression_quality = 99
    img.type = 'grayscale'
    img.resize(3500, 4800)
    img.crop(1, 1, 3500, 4800)
    # img.level(0.5, 0.9, gamma=1.66)
    # img.level(0.5, 0.7, gamma=1.0)

    # Better one (Level)
    img.level(0.6, 0.8, gamma=2.00)

    img.trim(fuzz=80)
    img.normalize(channel=None)
    img.modulate(saturation=50)
    # img.background_color = Color("white")
    # img.image_median = 1
    # img.image_contrast = 100

    # img.contrast_stretch(1.0, 0.0, "black")
    # img.linear_stretch(0.1, 1.0)
    # img.type='bilevel'

    img.save(filename='Images/grayscale.png')

# print(type(img))

# ########################## Gaussian Filter ##########################
kernel = np.array([[-1, -1, -1, -1, -1], [-1, 2, 2, 2, -1], [-1, 2, 8, 2, -1],
                    [-2, 2, 2, 2, -1], [-1, -1, -1, -1, -1]]) / 8.0

image = cv2.imread("Images/grayscale.png")
output = cv2.filter2D(image, -1, kernel)
output = cv2.GaussianBlur(output, (5, 5), 0.0)

# output = cv2.fastNlMeansDenoising(output, None, 14, 10, 25)
cv2.imwrite("Images/kernel.png", output)


# Apply dilation and erosion to remove some noise
# kernel2 = np.ones((1, 1), np.uint8)
# img = cv2.dilate(output, kernel2, iterations=1)
# img = cv2.erode(output, kernel2, iterations=1)

# ########################## OpenCV Threshold ##########################

retval, threshold = cv2.threshold(output, 150, 255, cv2.THRESH_BINARY)
cv2.imwrite("Images/last.png", threshold)

# #####################################################################

result = pytesseract.image_to_string(threshold, config="-c tessedit_char_whitelist=/0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.- --psm 6")
open('Text file/dutch.txt', 'w', encoding="utf-8")
f = open('Text file/document.txt', 'w', encoding="utf-8")
f.write(result)

# ########################## Getting only date ##########################

with open("Text file/document.txt", "r", encoding="utf-8") as f:
    for line in f:
        if (re.match(r"([A-Za-z0-9_]{1,2}/[A-Za-z0-9_]{2}/[\d]{4})", line)):
            f = open('Text file/dutch.txt', 'a+', encoding="utf-8")
            f.write(line)
            # print(line)
f.close()

# Finding error

# Read in the file
with open("Text file/dutch.txt", 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('.00', '')
# filedata = filedata.replace('lS', '15')
filedata = filedata.replace('.', '')
filedata = filedata.replace(',', '')

# Write the file out again
with open('Text file/dutch.txt', 'w') as file:
  file.write(filedata)


print("PDF to text conversation is done!")


# Found 40/41 row