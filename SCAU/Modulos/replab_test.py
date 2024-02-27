from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

canv = canvas.Canvas("example_flowable.pdf")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='DOCS',
                          alignment=TA_JUSTIFY,
                          fontName='Helvetica',
                          fontSize=12,
                          textColor=colors.black,
                          leading=14,
                          wordWrap='LTR',
                          splitLongWords=False,
                          spaceShrinkage=0.05,
                          ))

styles.add(ParagraphStyle(name='TITLES',
                          alignment=TA_CENTER,
                          fontName='Helvetica',
                          fontSize=12,
                          textColor=colors.black,
                          leading=14,
                          wordWrap='LTR',
                          splitLongWords=False,
                          spaceShrinkage=0.05,
                          ))

name = "Carlos"
surname = "Escalona"
nation = 'V'
idc = 31608879
carreer = 'Informática'
course = 2
sem = 4

content = []

header = Image("cintillo_unexca.png", 19*cm, 1.5*cm)
titles = "<br /><br /><b>CONSTANCIA DE ESTUDIOS</b><br /><br /><b>Núcleo Altagracia</b><br /><br />"

my_text = f"<font size=12>Quien suscribe, ; , hace constar que el(la) ciudadano(a) <b>{name} {surname}</b>, titular de la cédula de identidad N° <b>{nation}-{idc}</b> está inscrito en el <b>Plan Nacional de Formación en {carreer} cursando el Trayecto {course}, Semestre {sem} en el periodo academico 2024-1</b>\n\nConstancia que se expide a petición de la parte interesada en Caracas, 25 de febrero de 2024.</font>"

doc = SimpleDocTemplate("example_flowable.pdf",pagesize=A4,
                        rightMargin=2*cm,leftMargin=2*cm,
                        topMargin=0.1*cm,bottomMargin=2*cm)

doc.build([header, Paragraph(titles, styles['TITLES']), Paragraph(my_text.replace("\n", "<br />"), styles['DOCS']),])