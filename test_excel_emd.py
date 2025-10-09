import os

# Test that the required files exist
def test_files_exist():
    files_to_check = [
        "static/html/EmdRefund.html",
        "pages/01_Excel_se_EMD.py",
        "pages/07_EMD_Refund.py"
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            print(f"✓ {file_path} exists")
        else:
            print(f"✗ {file_path} does not exist")

# Test the EMD Refund HTML file
def test_emd_refund_html():
    try:
        with open("static/html/EmdRefund.html", "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check for key elements
        checks = [
            ("<title>Hand Receipt (RPWA 28)</title>", "HTML title"),
            ("id=\"payee\"", "Payee input field"),
            ("id=\"amount\"", "Amount input field"),
            ("id=\"work\"", "Work input field"),
            ("id=\"generate-button\"", "Generate button"),
            ("convertNumberToWords", "Number to words function"),
            ("generateReceiptHTML", "Receipt generation function"),
            ("@page", "Print CSS with page size"),
            ("size: A4 portrait", "A4 page size specification"),
            ("Ar.", "Circular seal - Ar."),
            ("D.A.", "Circular seal - D.A."),
            ("E.E.", "Circular seal - E.E.")
        ]
        
        for check, description in checks:
            if check in content:
                print(f"✓ {description}")
            else:
                print(f"✗ {description}")
                
        print(f"EMD Refund HTML file validation completed. File size: {len(content)} characters")
        
    except Exception as e:
        print(f"Error reading EMD Refund HTML file: {e}")

if __name__ == "__main__":
    print("=== Testing File Existence ===")
    test_files_exist()
    
    print("\n=== Testing EMD Refund HTML File ===")
    test_emd_refund_html()
    
    print("\nValidation complete!")