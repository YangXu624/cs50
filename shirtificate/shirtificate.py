from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 30, 50, 150)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=50)
pdf.cell(80, 50, f"Name took CS50", ln = True)
pdf.output("shirtificate.pdf")
