from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm

def StudyCert(std_name, std_surname, std_nation, std_idc, std_carreer, std_course, std_sem):
    canv = canvas.Canvas("example_flowable.pdf", A4)

    doc_style = ParagraphStyle(name='DOCS',
                            alignment=TA_JUSTIFY,
                            fontName='Helvetica',
                            fontSize=12,
                            textColor=colors.black,
                            leading=16,
                            wordWrap='LTR',
                            splitLongWords=False,
                            spaceShrinkage=0.05
                            )

    name = std_name
    surname = std_surname
    nation = std_nation
    idc = std_idc
    carreer = std_carreer
    course = std_course
    sem = std_sem

    header = Image("cintillo_unexca.png", 19*cm, 1.5*cm)

    canv.setFont('Helvetica-Bold', 12)
    canv.drawCentredString(290, 700, 'CONSTANCIA DE ESTUDIOS')
    canv.drawCentredString(290, 675, 'Núcleo Altagracia')

    p1 = Paragraph(f"<font size=12>Quien suscribe, ; , hace constar que el(la) ciudadano(a) <b>{name} {surname}</b>, titular de la cédula de identidad N° <b>{nation}-{idc}</b> está inscrito en el <b>Plan Nacional de Formación en {carreer} cursando el Trayecto {course}, Semestre {sem} en el periodo academico 2024-1</b><br /><br />Constancia que se expide a petición de la parte interesada en Caracas, 25 de febrero de 2024.</font>", doc_style)

    canv.setFont('Helvetica', 12)
    canv.drawCentredString(290, 475, 'Atentamente,')

    header.drawOn(canv, 25, 790)
    p1.wrapOn(canv, 550, 125)
    p1.drawOn(canv, 25, 575)

    page_number = canv.getPageNumber()
    p_num = 'Página %s' % page_number

    canv.setFont('Helvetica', 8)
    canv.drawString(25, 10, p_num)

    canv.save()
  
