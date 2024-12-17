from fpdf import FPDF
import sys

name = input("Name: ")
text = f"{name} took CS50"

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 30)
pdf.cell(210, 20, "CS50 Shirtificate", align= "C", center= True)
pdf.image("shirtificate.png", x = "C", y = 50, w = 190)
pdf.set_font("helvetica", "B", 20)
pdf.set_text_color(r=255, g=255, b=255)
pdf.cell(210, 200, text, align= "C", center= True)
pdf.output("shirtificate.pdf")
sys.exit
