#!/usr/bin/env python3
"""
PWD Tools PDF Generator
Generates actual PDF outputs for all 10 components
"""

import os
import pandas as pd
from datetime import datetime
import pdfkit
from num2words import num2words

# Configure wkhtmltopdf path
wkhtmltopdf_path = 'C:/program files/wkhtmltopdf/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

def generate_01_excel_se_emd_pdf():
    """Generate PDF for Excel se EMD Component"""
    print("🔍 Generating PDF for COMPONENT 1: Excel se EMD")
    
    # Sample data
    sample_data = [
        {"Payee Name": "Rajkumar Contractor", "Amount": 50000, "Work": "Electrical Installation"},
        {"Payee Name": "Babulal Electric", "Amount": 75000, "Work": "Transformer Maintenance"},
        {"Payee Name": "Marudhar HR", "Amount": 25000, "Work": "Cable Laying"}
    ]
    
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hand Receipt (RPWA 28)</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .receipt { border: 2px solid #333; padding: 20px; margin: 20px 0; page-break-after: always; }
            .header { text-align: center; margin-bottom: 20px; }
            .details { margin: 15px 0; }
            .signature-table { width: 100%; border-collapse: collapse; margin: 20px 0; }
            .signature-table td, .signature-table th { border: 1px solid #333; padding: 8px; text-align: left; }
            .amount { font-weight: bold; color: #2E8B57; }
        </style>
    </head>
    <body>
    """
    
    for i, receipt in enumerate(sample_data, 1):
        amount_words = num2words(receipt['Amount'], lang='en').title()
        html_content += f"""
        <div class="receipt">
            <div class="header">
                <h2>HAND RECEIPT (RPWA 28)</h2>
                <h3>Payable to: {receipt['Payee Name']} (Electric Contractor)</h3>
                <p>Division - PWD Electric Division, Udaipur</p>
            </div>
            <div class="details">
                <p><strong>Amount:</strong> <span class="amount">Rs. {receipt['Amount']:,}/-</span></p>
                <p><strong>Amount in Words:</strong> {amount_words} Only</p>
                <p><strong>Work:</strong> {receipt['Work']}</p>
                <p><strong>Chargeable to Head:</strong> 8443 [EMD-Refund]</p>
            </div>
            <table class="signature-table">
                <tr><th>Witness</th><th>Stamp</th><th>Signature of Payee</th></tr>
                <tr><td></td><td></td><td></td></tr>
            </table>
        </div>
        """
    
    html_content += "</body></html>"
    
    # Generate PDF
    pdf_file = "01_Excel_se_EMD_Receipts.pdf"
    try:
        pdfkit.from_string(html_content, pdf_file, configuration=config)
        print(f"✅ PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

def generate_02_bill_deviation_pdf():
    """Generate PDF for Bill Deviation Component"""
    print("🔍 Generating PDF for COMPONENT 2: Bill Deviation Calculator")
    
    original_amount = 100000
    revised_amount = 125000
    deviation = ((revised_amount - original_amount) / original_amount) * 100
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Bill Deviation Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .report {{ border: 2px solid #333; padding: 30px; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
            .calculation {{ margin: 20px 0; padding: 20px; background: #f5f5f5; }}
            .result {{ font-size: 18px; font-weight: bold; color: #d32f2f; }}
        </style>
    </head>
    <body>
        <div class="report">
            <div class="header">
                <h1>Bill Deviation Report</h1>
                <p>PWD Electric Division, Udaipur</p>
            </div>
            <div class="calculation">
                <h3>Deviation Calculation:</h3>
                <p><strong>Original Amount:</strong> Rs. {original_amount:,}</p>
                <p><strong>Revised Amount:</strong> Rs. {revised_amount:,}</p>
                <p class="result">Deviation: {deviation:.2f}%</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    pdf_file = "02_Bill_Deviation_Report.pdf"
    try:
        pdfkit.from_string(html_content, pdf_file, configuration=config)
        print(f"✅ PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

def generate_03_tender_processing_pdf():
    """Generate PDF for Tender Processing Component"""
    print("🔍 Generating PDF for COMPONENT 3: Tender Processing")
    
    tenders = [
        {"Tender No": "T001/2024", "Work": "Road Construction", "Estimated Cost": 5000000},
        {"Tender No": "T002/2024", "Work": "Bridge Repair", "Estimated Cost": 2500000},
        {"Tender No": "T003/2024", "Work": "Street Lighting", "Estimated Cost": 1500000}
    ]
    
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Tender Processing Report</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .report { border: 2px solid #333; padding: 30px; }
            .header { text-align: center; margin-bottom: 30px; }
            table { width: 100%; border-collapse: collapse; margin: 20px 0; }
            th, td { border: 1px solid #333; padding: 12px; text-align: left; }
            th { background: #f0f0f0; }
        </style>
    </head>
    <body>
        <div class="report">
            <div class="header">
                <h1>Tender Processing Report</h1>
                <p>PWD Electric Division, Udaipur</p>
            </div>
            <table>
                <tr>
                    <th>Tender No</th>
                    <th>Work Description</th>
                    <th>Estimated Cost</th>
                </tr>
    """
    
    for tender in tenders:
        html_content += f"""
                <tr>
                    <td>{tender['Tender No']}</td>
                    <td>{tender['Work']}</td>
                    <td>Rs. {tender['Estimated Cost']:,}</td>
                </tr>
        """
    
    html_content += """
            </table>
        </div>
    </body>
    </html>
    """
    
    pdf_file = "03_Tender_Processing_Report.pdf"
    try:
        pdfkit.from_string(html_content, pdf_file, configuration=config)
        print(f"✅ PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

def generate_04_bill_note_sheet_pdf():
    """Generate PDF for Bill Note Sheet Component"""
    print("🔍 Generating PDF for COMPONENT 4: Bill Note Sheet")
    
    bill_data = {
        "Bill No": "BN001/2024",
        "Contractor": "Rajkumar Construction",
        "Work": "Electrical Installation",
        "Contract Amount": 500000,
        "Work Done": 75,
        "Amount Claimed": 375000
    }
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Bill Note Sheet</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .sheet {{ border: 2px solid #333; padding: 30px; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
            .info {{ margin: 20px 0; padding: 15px; background: #f9f9f9; }}
            .amount {{ font-weight: bold; color: #2E8B57; }}
        </style>
    </head>
    <body>
        <div class="sheet">
            <div class="header">
                <h1>Bill Note Sheet</h1>
                <p>PWD Electric Division, Udaipur</p>
            </div>
            <div class="info">
                <p><strong>Bill No:</strong> {bill_data['Bill No']}</p>
                <p><strong>Contractor:</strong> {bill_data['Contractor']}</p>
                <p><strong>Work:</strong> {bill_data['Work']}</p>
                <p><strong>Contract Amount:</strong> <span class="amount">Rs. {bill_data['Contract Amount']:,}</span></p>
                <p><strong>Work Completion:</strong> {bill_data['Work Done']}%</p>
                <p><strong>Amount Claimed:</strong> <span class="amount">Rs. {bill_data['Amount Claimed']:,}</span></p>
            </div>
        </div>
    </body>
    </html>
    """
    
    pdf_file = "04_Bill_Note_Sheet.pdf"
    try:
        pdfkit.from_string(html_content, pdf_file, configuration=config)
        print(f"✅ PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

def generate_05_deductions_table_pdf():
    """Generate PDF for Deductions Table Component"""
    print("🔍 Generating PDF for COMPONENT 5: Deductions Table")
    
    deductions = [
        {"Type": "Income Tax", "Rate": "2%", "Amount": 2500},
        {"Type": "Security Deposit", "Rate": "5%", "Amount": 6250},
        {"Type": "Quality Penalty", "Rate": "1%", "Amount": 1250}
    ]
    
    total_deductions = sum(d['Amount'] for d in deductions)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Deductions Table</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .table {{ border: 2px solid #333; padding: 30px; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
            table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
            th, td {{ border: 1px solid #333; padding: 12px; text-align: left; }}
            th {{ background: #f0f0f0; }}
            .total {{ font-weight: bold; color: #d32f2f; }}
        </style>
    </head>
    <body>
        <div class="table">
            <div class="header">
                <h1>Deductions Table</h1>
                <p>PWD Electric Division, Udaipur</p>
            </div>
            <table>
                <tr>
                    <th>Type</th>
                    <th>Rate</th>
                    <th>Amount</th>
                </tr>
    """
    
    for deduction in deductions:
        html_content += f"""
                <tr>
                    <td>{deduction['Type']}</td>
                    <td>{deduction['Rate']}</td>
                    <td>Rs. {deduction['Amount']:,}</td>
                </tr>
        """
    
    html_content += f"""
                <tr class="total">
                    <td colspan="2"><strong>Total Deductions</strong></td>
                    <td><strong>Rs. {total_deductions:,}</strong></td>
                </tr>
            </table>
        </div>
    </body>
    </html>
    """
    
    pdf_file = "05_Deductions_Table.pdf"
    try:
        pdfkit.from_string(html_content, pdf_file, configuration=config)
        print(f"✅ PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

def generate_06_delay_calculator_pdf():
    """Generate PDF for Delay Calculator Component"""
    print("🔍 Generating PDF for COMPONENT 6: Delay Calculator")
    
    original_duration = 150
    actual_duration = 196
    delay_days = actual_duration - original_duration
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Project Delay Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .report {{ border: 2px solid #333; padding: 30px; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
            .calculation {{ margin: 20px 0; padding: 20px; background: #f5f5f5; }}
            .delay {{ font-size: 18px; font-weight: bold; color: #d32f2f; }}
        </style>
    </head>
    <body>
        <div class="report">
            <div class="header">
                <h1>Project Delay Report</h1>
                <p>PWD Electric Division, Udaipur</p>
            </div>
            <div class="calculation">
                <h3>Delay Calculation:</h3>
                <p><strong>Original Duration:</strong> {original_duration} days</p>
                <p><strong>Actual Duration:</strong> {actual_duration} days</p>
                <p class="delay">Project Delay: {delay_days} days</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    pdf_file = "06_Delay_Calculator_Report.pdf"
    try:
        pdfkit.from_string(html_content, pdf_file, configuration=config)
        print(f"✅ PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

def generate_07_emd_refund_pdf():
    """Generate PDF for EMD Refund Component"""
    print("🔍 Generating PDF for COMPONENT 7: EMD Refund Calculator")
    
    emd_data = {
        "Contractor": "Rajkumar Electric",
        "Tender Amount": 1000000,
        "EMD Amount": 20000,
        "EMD Rate": "2%"
    }
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>EMD Refund Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .report {{ border: 2px solid #333; padding: 30px; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
            .info {{ margin: 20px 0; padding: 20px; background: #f9f9f9; }}
            .amount {{ font-weight: bold; color: #2E8B57; }}
        </style>
    </head>
    <body>
        <div class="report">
            <div class="header">
                <h1>EMD Refund Report</h1>
                <p>PWD Electric Division, Udaipur</p>
            </div>
            <div class="info">
                <p><strong>Contractor:</strong> {emd_data['Contractor']}</p>
                <p><strong>Tender Amount:</strong> <span class="amount">Rs. {emd_data['Tender Amount']:,}</span></p>
                <p><strong>EMD Amount:</strong> <span class="amount">Rs. {emd_data['EMD Amount']:,}</span></p>
                <p><strong>EMD Rate:</strong> {emd_data['EMD Rate']}</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    pdf_file = "07_EMD_Refund_Report.pdf"
    try:
        pdfkit.from_string(html_content, pdf_file, configuration=config)
        print(f"✅ PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

def generate_08_financial_progress_pdf():
    """Generate PDF for Financial Progress Component"""
    print("🔍 Generating PDF for COMPONENT 8: Financial Progress Tracker")
    
    progress_data = {
        "Project": "Electrical Infrastructure",
        "Total Budget": 5000000,
        "Expenditure": 3250000,
        "Balance": 1750000
    }
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Financial Progress Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .report {{ border: 2px solid #333; padding: 30px; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
            .info {{ margin: 20px 0; padding: 20px; background: #f9f9f9; }}
            .amount {{ font-weight: bold; color: #2E8B57; }}
        </style>
    </head>
    <body>
        <div class="report">
            <div class="header">
                <h1>Financial Progress Report</h1>
                <p>PWD Electric Division, Udaipur</p>
            </div>
            <div class="info">
                <p><strong>Project:</strong> {progress_data['Project']}</p>
                <p><strong>Total Budget:</strong> <span class="amount">Rs. {progress_data['Total Budget']:,}</span></p>
                <p><strong>Expenditure:</strong> <span class="amount">Rs. {progress_data['Expenditure']:,}</span></p>
                <p><strong>Balance:</strong> <span class="amount">Rs. {progress_data['Balance']:,}</span></p>
            </div>
        </div>
    </body>
    </html>
    """
    
    pdf_file = "08_Financial_Progress_Report.pdf"
    try:
        pdfkit.from_string(html_content, pdf_file, configuration=config)
        print(f"✅ PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

def generate_09_security_refund_pdf():
    """Generate PDF for Security Refund Component"""
    print("🔍 Generating PDF for COMPONENT 9: Security Refund Calculator")
    
    security_data = {
        "Contractor": "Babulal Construction",
        "Contract Value": 2000000,
        "Security Amount": 100000,
        "Security Rate": "5%"
    }
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Security Refund Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .report {{ border: 2px solid #333; padding: 30px; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
            .info {{ margin: 20px 0; padding: 20px; background: #f9f9f9; }}
            .amount {{ font-weight: bold; color: #2E8B57; }}
        </style>
    </head>
    <body>
        <div class="report">
            <div class="header">
                <h1>Security Refund Report</h1>
                <p>PWD Electric Division, Udaipur</p>
            </div>
            <div class="info">
                <p><strong>Contractor:</strong> {security_data['Contractor']}</p>
                <p><strong>Contract Value:</strong> <span class="amount">Rs. {security_data['Contract Value']:,}</span></p>
                <p><strong>Security Amount:</strong> <span class="amount">Rs. {security_data['Security Amount']:,}</span></p>
                <p><strong>Security Rate:</strong> {security_data['Security Rate']}</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    pdf_file = "09_Security_Refund_Report.pdf"
    try:
        pdfkit.from_string(html_content, pdf_file, configuration=config)
        print(f"✅ PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

def generate_10_stamp_duty_pdf():
    """Generate PDF for Stamp Duty Component"""
    print("🔍 Generating PDF for COMPONENT 10: Stamp Duty Calculator")
    
    contract_value = 3000000
    stamp_duty_rate = 0.5
    stamp_duty_amount = (contract_value * stamp_duty_rate) / 100
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Stamp Duty Calculation</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .report {{ border: 2px solid #333; padding: 30px; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
            .calculation {{ margin: 20px 0; padding: 20px; background: #f5f5f5; }}
            .amount {{ font-weight: bold; color: #2E8B57; }}
        </style>
    </head>
    <body>
        <div class="report">
            <div class="header">
                <h1>Stamp Duty Calculation</h1>
                <p>PWD Electric Division, Udaipur</p>
            </div>
            <div class="calculation">
                <h3>Calculation Details:</h3>
                <p><strong>Contract Value:</strong> <span class="amount">Rs. {contract_value:,}</span></p>
                <p><strong>Stamp Duty Rate:</strong> {stamp_duty_rate}%</p>
                <p><strong>Stamp Duty Amount:</strong> <span class="amount">Rs. {stamp_duty_amount:,}</span></p>
            </div>
        </div>
    </body>
    </html>
    """
    
    pdf_file = "10_Stamp_Duty_Calculation.pdf"
    try:
        pdfkit.from_string(html_content, pdf_file, configuration=config)
        print(f"✅ PDF generated: {pdf_file}")
        return pdf_file
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

def main():
    """Generate PDFs for all 10 components"""
    print("🚀 PWD TOOLS PDF GENERATOR")
    print("Generating PDF outputs for all 10 components...")
    print()
    
    # Generate all PDFs
    pdf_functions = [
        generate_01_excel_se_emd_pdf,
        generate_02_bill_deviation_pdf,
        generate_03_tender_processing_pdf,
        generate_04_bill_note_sheet_pdf,
        generate_05_deductions_table_pdf,
        generate_06_delay_calculator_pdf,
        generate_07_emd_refund_pdf,
        generate_08_financial_progress_pdf,
        generate_09_security_refund_pdf,
        generate_10_stamp_duty_pdf
    ]
    
    generated_pdfs = []
    for func in pdf_functions:
        try:
            pdf_file = func()
            if pdf_file:
                generated_pdfs.append(pdf_file)
        except Exception as e:
            print(f"❌ Error in {func.__name__}: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 PDF GENERATION SUMMARY")
    print("=" * 60)
    print(f"  Total Components: {len(pdf_functions)}")
    print(f"  PDFs Generated: {len(generated_pdfs)}")
    print(f"  Failed: {len(pdf_functions) - len(generated_pdfs)}")
    
    if generated_pdfs:
        print("\n📁 Generated PDF Files:")
        for pdf in generated_pdfs:
            print(f"  ✅ {pdf}")
    
    print("\n✨ PDF generation completed!")

if __name__ == "__main__":
    main()
