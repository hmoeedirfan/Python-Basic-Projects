# First run this command in terminal, 'pip install PyPDF2'
from PyPDF2 import PdfFileReader, PdfFileMerger
# Read files
pdf1 = PdfFileReader('pdf1.pdf')
pdf2 = PdfFileReader('pdf2.pdf')

output = PdfFileMerger()
# Add files
output.append(pdf1)
output.append(pdf2)
# Giving name to file after merging file
output.write('merged.pdf')
output.close
print('Merged Complete!')