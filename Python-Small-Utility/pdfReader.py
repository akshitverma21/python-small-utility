import PyPDF2
a=PyPDF2.PdfFileReader('samplePdf.pdf')
# print(a.getDocumentInfo())
# print(a.getNumPages())
# print(a.getPage(2))
str=""
for i in range(1,a.getNumPages()):
    str+=a.getPage(i).extractText()
with open('text.txt','w',encoding='utf-8') as w:
    w.write(str)