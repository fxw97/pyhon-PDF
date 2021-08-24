from PyPDF2 import PdfFileReader,PdfFileWriter
pdf_input = PdfFileReader('1.拆分1.pdf')
pdf_write = PdfFileWriter()

# 选中第一页进行顺时针旋转90度；逆时针旋转用rotateCounterClockwise(90)
page = pdf_input.getPage(0).rotateClockwise(90)
pdf_write.addPage(page)

with open('3.旋转后.pdf','wb') as file:
    pdf_write.write(file)