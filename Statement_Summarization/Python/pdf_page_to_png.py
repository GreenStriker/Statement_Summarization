"""
This script was used to create the figures for http://jrsmith3.github.io/sample-logs-the-secret-to-managing-multi-person-projects.html from a PDF file containing some old CMU sample logs.
"""

"""
Main Link: https://gist.github.com/jrsmith3/9947838
"""

import PyPDF2
from wand.image import Image
import io
import os
import re

def pdf_page_to_png(src_pdf, pagenum=0, resolution=72):
    """
    Returns specified PDF page as wand.image.Image png.

    :param PyPDF2.PdfFileReader src_pdf: PDF from which to take pages.
    :param int pagenum: Page number to take.
    :param int resolution: Resolution for resulting png in DPI.
    """
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.addPage(src_pdf.getPage(pagenum))

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)

    img = Image(file=pdf_bytes, resolution=resolution)
    img.convert("png")

    return img

def Get_PDF_Length(src_pdf):
    pdf = PyPDF2.PdfFileReader(open(src_pdf, 'rb'))
    number = pdf.getNumPages()

    return number

# Get File Name
def Get_PDF_File_Name(src_filename):
    file = re.search('/(.*).pdf', src_filename)
    pdf_filename = file.group(1)

    return pdf_filename
