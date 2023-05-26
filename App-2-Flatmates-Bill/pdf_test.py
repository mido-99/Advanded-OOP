from fpdf import FPDF

pdf = FPDF( orientation='p', unit='pt')
pdf.add_page()
pdf.set_font('Helvetica', 'IB', 24)
pdf.cell(w=0, h=30, txt="Flatmate's Bill", border=True, align='C', ln=1)

pdf.set_font('Helvetica', 'IB', 18)
pdf.cell(150, 40, "Period:", border=True)
pdf.cell(120, 40, "May 2023", border=True, ln=1)
pdf.cell(150, 40, "Bill Amount:", border=True)
pdf.cell(120, 40, "100$", border=True)
pdf.ln(100)
pdf.cell(260, 40, "Tom", border=True, align='C')
pdf.cell(260, 40, "Jerry", border=True, align='C', ln=1)
pdf.cell(260, 40, "60$", border=True, align='C')
pdf.cell(260, 40, "40$", border=True, align='C', ln=1)


pdf.output('test.pdf')

