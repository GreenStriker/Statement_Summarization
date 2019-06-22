import cv2
import numpy as np
import pytesseract
from wand.image import Image
import re
import PyPDF2
import pdf_page_to_png
import Text_To_Excel
import os
bank_name = input("Enter Bank Name: ")

if(bank_name == "DBBL"):
    import DBBL