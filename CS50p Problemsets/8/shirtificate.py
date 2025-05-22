from fpdf import FPDF
from fpdf import Align

# class FPDF(orientation='portrait', unit='mm', format='A4', font_cache_dir='DEPRECATED')
# pdf.set_margin(set_auto_page_break)
name = input("What's your name? ")
pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font("Times", size=45, style="B")
pdf.text(x=50, y=30, text="CS50 Shirtificate")
# pdf.cell(text= "CS50 Shirtificate", align=Align.C)
pdf.image("./shirtificate.png", x=Align.C, y=70)
pdf.set_font("Times", size=30, style="B")
pdf.set_text_color(255, 255, 255)
pdf.text(x=45, y=150, text=f"{name} took CS50p")
pdf.output("shirtificate.pdf")
