from PyPDF2 import PdfFileReader,PdfFileWriter

pdf1 = PdfFileReader('2.合并后.pdf')
pdf_write = PdfFileWriter()

for page in range(pdf1.getNumPages()):
    pdf_write.addPage(pdf1.getPage(page))

# 设置密码
pdf_write.encrypt('fxw1234')

# 保存PDF
with open('5.给PDF加密码之后.pdf','wb') as file:
    pdf_write.write(file)