from PyPDF2 import PdfFileReader,PdfFileWriter

PDF_input = PdfFileReader('ESTL-2018-LTY.pdf')

for page in range(0,PDF_input.getNumPages()):
    pdf_write = PdfFileWriter()
    pdf_write.addPage(PDF_input.getPage(page)) # 将各页pdf内容存入到pdf_write中
    with open(f'1.拆分{page+1}.pdf','wb') as file:
        pdf_write.write(file)