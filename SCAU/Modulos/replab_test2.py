from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import cm

pdf = canvas.Canvas("test2.pdf", letter)
pdf.translate(cm, cm)
pdf.setFont('Helvetica-Bold', 12)
pdf.drawImage("cintillo_unexca.png", 0.05, 24.8*cm, 19*cm, 1.5*cm)
pdf.drawCentredString(10*cm, 21*cm, 'CONSTANCIA DE ESTUDIOS')
pdf.drawCentredString(10*cm, 20*cm, 'Núcleo Altagracia')
pdf.setFont('Helvetica', 12)
pdf.drawString(1*cm, 18*cm, 'HolaHolaHolaHolaHolaHolaHolaHolaHolaHolaHolaHolaHolaHolaHolaHolaHolaHolaHolaHo\nhola')
pdf.showPage()
pdf.save()