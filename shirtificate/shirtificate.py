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


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=40)
pdf.cell(150, 100, f"Name took CS50")
pdf.output("shirtificate.pdf")
