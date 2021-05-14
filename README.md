# Hindi_News_OCR
Recruitment project for 1st year
Installation Process:
OpenCV
OpenCV (Open source Computer vision library) is a library of programming functions mainly aimed at real-time computer vision.
Installation
pip install opencv-python

NumPy
NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
Installation
pip install numpy

PyTesseract
Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images. Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine.
Installation
pip install pytesseract

Tesseract-OCR
Tesseract is an optical character recognition engine for various operating systems. Tesseract can process right-to-left text such as Arabic or Hebrew, many Indic scripts as well as CJK quite well.
Installation
https://github.com/UB-Mannheim/tesseract/wiki

 Select devnagari script under additional script data.

 
Select hindi under additional language data .

Googletrans
Googletrans is a free and unlimited python library that implemented Google Translate API. This uses the Google Translate Ajax API to make calls to such methods as detect and translate.
Installation
pip install googletrans==3.1.0a0

Nltk
The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language.
Installation
pip install nltk
import nltk
nltk.download()
s Install packages from the window.




Explanation of Files:

ocr.py – This file contains the OCR tool tesseract that inputs the image provided and give the recognized text as string in “original_text.txt” file. This also contains the function call statements of the summarizer and translator.
translate.py – This file uses the googletrans API and has two functions: translate_en2hi() that translates English text to Hindi and translate_hi2en() that translates Hindi to English. This file gives the final summary output as “summary_text.txt” file.
summary.py - Two NLTK libraries will be required to make an efficient summarizer.
                               nltk.corpus
                               nltk.tokenizer
 Stop words such as is, an, a, the that doesn’t add value to the meaning of the sentence are removed. A python dictionary stores the record of how many times a word appears in the given text after removing the stop words. Scores are assigned to each sentence depending on the words it contains and the frequency table and stored in a separate dictionary. The scores are compared based on average score of a sentence and after applying threshold value the sentences are stored in order in summary.  
 





