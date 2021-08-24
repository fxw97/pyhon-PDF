from PyPDF2 import PdfFileReader,PdfFileWriter
pdf_writer = PdfFileWriter()
for i in range(0,6):
    pdf_input = PdfFileReader(f'1.拆分{i+1}.pdf')
    for page in range(pdf_input.getNumPages()):
        pdf_writer.addPage(pdf_input.getPage(page))

with open('2.合并后.pdf','wb') as file:
    pdf_writer.write(file)