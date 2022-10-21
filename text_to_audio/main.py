import pyttsx3
import PyPDF2

book = open('Freelancing Notes.pdf','rb')
pdfReader = PyPDF2.PdfReader(book)
pages = pdfReader.numPages
num = int(input('Enter page number: '))

speaker = pyttsx3.init()
for i in range(num,pages):
    # for extracting page of book
    page = pdfReader.getPage(num)
    text = page.extract_text()
    # for speaking
    speaker.say(text)
    speaker.runAndWait()