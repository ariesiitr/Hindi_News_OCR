
from googletrans import Translator
def translate_hi2en(text):
    trans = Translator()
    t1 = trans.translate(
        text, src= 'hi', dest='en'
    )
    
    etext = t1.text 
    return etext
    
def translate_en2hi(text):
    trans = Translator()
    t2 = trans.translate(
        text, src= 'en', dest='hi'
    )
    
    file1 = open("summary_text.txt","w")
    file1.writelines(t2.text)
    file1.close()