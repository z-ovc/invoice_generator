import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for file in filepaths:
    pdf = FPDF(orientation= "P", unit='mm', format="A4" )
    pdf.add_page()
    pdf.set_font(family="Times", size=18, style="B")
    invoice_name,invoice_date = Path(file).stem.split("-")
    pdf.cell(w=30, h=10, txt=f"Invoice No.{invoice_name} ", ln=1)

    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=20, h=10, txt=f" Date: {invoice_date} ",ln=1)

    df = pd.read_excel(file, sheet_name= "Sheet 1")
    
    columns = df.columns
    columns = [item.replace("_"," ").title() for item in columns]
    pdf.set_font(family="Times", size=15)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=10, txt=str(columns[0]),border=1)
    pdf.cell(w=60, h=10, txt=str(columns[1]),border=1)
    pdf.cell(w=45, h=10, txt=str(columns[2]),border=1)
    pdf.cell(w=35, h=10, txt=str(columns[3]),border=1)
    pdf.cell(w=25, h=10, txt=str(columns[4]),border=1,ln=1)


    for index,row in df.iterrows():
        pdf.set_font(family="Times", size=15)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=10, txt=str(row['product_id']),border=1)
        pdf.cell(w=60, h=10, txt=str(row['product_name']),border=1)
        pdf.cell(w=45, h=10, txt=str(row['amount_purchased']),border=1)
        pdf.cell(w=35, h=10, txt=str(row['price_per_unit']),border=1)
        pdf.cell(w=25, h=10, txt=str(row['total_price']),border=1,ln=1)
    total_sum = df['total_price'].sum()
    pdf.set_font(family="Times", size=15)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=10, txt=str("total price"),border=1)
    pdf.cell(w=60, h=10, txt=str(" "),border=1)
    pdf.cell(w=45, h=10, txt=str(" "),border=1)
    pdf.cell(w=35, h=10, txt=str(" "),border=1)
    pdf.cell(w=25, h=10, txt=str(total_sum),border=1,ln=1)

    pdf.set_font(family="Times", size=15)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=20, h=10, txt=f"The total price is {total_sum}",ln=1)

    pdf.set_font(family="Times", size=15)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=10, txt="My-invoice")
    pdf.image("logo.jpg", w=10)


    pdf.output(f"PDFs/{invoice_name}.pdf")
     


