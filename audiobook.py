import PyPDF2
import pyttsx3

book=open("cn.pdf",'rb')
pdfReader=PyPDF2.PdfReader(book)
pages=len(pdfReader.pages)
speaker=pyttsx3.init()

for page_num in range(pages):
                    page=pdfReader.pages[page_num]
                    text=page.extract_text()
                    if text:
                                        speaker.say(text)
speaker.runAndWait()
book.close()
