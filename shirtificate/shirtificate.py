from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 30, 50, 150)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 70)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)

name = input("Name: ")

# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=40)
pdf.set_text_color(255, 255, 255)
pdf.cell(190, 150, f"{name} took CS50", border=0, align="C")
pdf.output("shirtificate.pdf")
