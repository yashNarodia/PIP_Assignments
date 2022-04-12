from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 10)
f = open('C:\College_pdf\SEM_4\PIP\Assignments\marksheet.txt','r')
for line in f:
    pdf.cell(200,10,txt=line,ln=1 ,align='C')
pdf.output('mark-sheet.pdf')