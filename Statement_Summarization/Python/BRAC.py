import cv2
import numpy as np
import pytesseract
from wand.image import Image
import re
import PyPDF2
import pdf_page_to_png
import Text_To_Excel
import os

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

directory_path = os.path.dirname(__file__)

# Making directory
Images = directory_path+'/Images'
PDF = directory_path+'/PDF'
Text_File = directory_path+'/Text File'

if not os.path.exists(Images):
    os.makedirs(Images)

if not os.path.exists(PDF):
    os.makedirs(PDF)

if not os.path.exists(Text_File):
    os.makedirs(Text_File)

pdf_path = directory_path + "/PDF/BRAC_2.pdf"
get_pdf_name = pdf_page_to_png.Get_PDF_File_Name(pdf_path)
get_pdf_length = pdf_page_to_png.Get_PDF_Length(pdf_path)
open_pdf = PyPDF2.PdfFileReader(open(pdf_path, "rb"))

######################### Imagic Magick ##########################

open(directory_path + '/Text file/dutch.txt', 'w', encoding="utf-8")

# Convert each page to a png image.
for x in range(get_pdf_length):
    # filename = pdf_page_to_png.Get_PDF_File_Name(pdf_path) + "_" + (x+1).__str__() + ".png"

    img = pdf_page_to_png.pdf_page_to_png(open_pdf, pagenum=x, resolution=300)
    # img.save(filename="Images/" + filename)

    with Image(img, resolution=200) as img:
        print("Processing Page " + (x+1).__str__())
        img.compression_quality = 99
        img.type = 'grayscale'
        img.resize(3500, 4800)
        img.crop(1, 1, 3260, 4800)
        # img.level(0.5, 0.9, gamma=1.66)
        # img.level(0.5, 0.7, gamma=1.0)

        # Better one (Level)
        img.level(0.6, 0.8, gamma=2.00)

        img.trim(fuzz=40)
        img.normalize(channel=None)
        img.modulate(saturation=50)
        # img.background_color = Color("white")
        # img.image_median = 1
        # img.image_contrast = 100

        # img.contrast_stretch(1.0, 0.0, "black")
        # img.linear_stretch(0.1, 1.0)
        # img.type = 'bilevel'

        img.save(filename=directory_path + '/Images/grayscale.png')

    # print(type(img))

    # ########################## Gaussian Filter ##########################
    kernel = np.array([[-1, -1, -1, -1, -1], [-1, 2, 2, 2, -1], [-1, 2, 8, 2, -1],
                        [-2, 2, 2, 2, -1], [-1, -1, -1, -1, -1]]) / 8.0

    image = cv2.imread(directory_path + "/Images/grayscale.png")
    output = cv2.filter2D(image, -1, kernel)
    output = cv2.GaussianBlur(output, (5, 5), 0.0)

    # output = cv2.fastNlMeansDenoising(output, None, 14, 10, 25)
    cv2.imwrite(directory_path + "/Images/kernel.png", output)

    # ########################## OpenCV Threshold ##########################

    retval, threshold = cv2.threshold(output, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite(directory_path + "Images/last.png", threshold)

    result = pytesseract.image_to_string(threshold, config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.-/ --psm 6")
    f = open(directory_path + '/Text file/document.txt', 'w', encoding="utf-8")
    # f = open('Text file/document.txt', 'a+', encoding="utf-8")
    f.write(result)

    # ########################## Getting only date ##########################

    with open(directory_path + "/Text file/document.txt", "r", encoding="utf-8") as f:
        for line in f:
            # if (re.match(r"([A-Za-z0-9_]{1,2}-[A-Za-z0-9_]{3,4}-[\d]{2})", line)):
            if ((re.match(r"([A-Za-z0-9_]{1,2} [A-Za-z0-9_]{3,4} [\d]{2})", line)) or (
                 re.match(r"([A-Za-z0-9_]{1,3}[A-Za-z0-9_]{3,4} [\d]{2})", line)) or (
                 re.match(r"([A-Za-z0-9_]{1,2} [A-Za-z0-9_]{3,4}[\d]{3})", line))):
                f = open(directory_path + '/Text file/dutch.txt', 'a+', encoding="utf-8")
                f.write(line)
    f.close()

    # Finding error

    # Read in the file
    with open(directory_path + "/Text file/dutch.txt", 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('.00', '')
    filedata = filedata.replace('lS', '15')
    filedata = filedata.replace('.', '')
    filedata = filedata.replace(',', '')

    # Write the file out again
    with open(directory_path + '/Text file/dutch.txt', 'w') as file:
      file.write(filedata)

text_path = directory_path + "/Text file/dutch.txt"

Text_To_Excel.Make_Excel(text_path)

print("PDF to text conversation is done!")
