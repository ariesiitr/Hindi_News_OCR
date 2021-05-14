from cv2 import cv2
import numpy as np
import pytesseract


from translate import *
from summary import *


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("news1.jpg")
text = pytesseract.image_to_string(img , lang='hin')
file1 = open("original_text.txt","w")
file1.writelines(text)
file1.close()


etext = translate_hi2en(text)
summary = summarizer(etext)
translate_en2hi(summary)

