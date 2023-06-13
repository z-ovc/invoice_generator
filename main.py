import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for file in filepaths:
    df = pd.read_excel(file, sheet_name= "Sheet 1")
    pdf = FPDF(orientation= "P", unit='mm', format="A4" )
    pdf.add_page()
    pdf.set_font(family="Times", size=18, style="B")
    invoice_name = Path(file).stem.split("-")[0]
    pdf.cell(w=50, h=20, txt=f"Invoice No.{invoice_name} ")
    pdf.output(f"PDFs/{invoice_name}.pdf")
     


