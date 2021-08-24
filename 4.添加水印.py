from PyPDF2 import PdfFileReader,PdfFileWriter
from copy import copy

# 读取水印文件
pdf1 = PdfFileReader('4.水印文件.pdf')
sy = pdf1.getPage(0)

# 读取要添加水印的文件
pdf2 = PdfFileReader('2.合并后.pdf')
pdf_write = PdfFileWriter()
for page in range(pdf2.getNumPages()):
    page_need_sy = pdf2.getPage(page)
    new_page = copy(sy)
    new_page.mergePage(page_need_sy)
    pdf_write.addPage(new_page)

with open('4.添加水印后.pdf','wb') as file:
    pdf_write.write(file)