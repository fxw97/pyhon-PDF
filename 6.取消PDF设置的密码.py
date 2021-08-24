from PyPDF2 import PdfFileReader,PdfFileWriter

pdf1 = PdfFileReader('5.给PDF加密码之后.pdf')
pdf1.decrypt('fxw1234')
pdf_write = PdfFileWriter()

for page in range(pdf1.getNumPages()):
    pdf_write.addPage(pdf1.getPage(page))

with open('6.取消PDF设置的密码.pdf','wb') as file:
    pdf_write.write(file)