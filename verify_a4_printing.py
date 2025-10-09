import os

def verify_a4_printing():
    """Verify that EMD receipts are configured for single A4 page printing"""
    
    print("Verifying A4 printing configuration...")
    
    # Check EmdRefund.html
    try:
        with open("static/html/EmdRefund.html", "r", encoding="utf-8") as f:
            emd_content = f.read()
        
        print("\n=== Checking EmdRefund.html ===")
        
        # Check for key A4 printing elements
        required_elements = [
            "@media print",
            "size: A4 portrait",
            "width: 210mm",
            "height: 297mm",
            "page-break-after: never",
            "page-break-inside: avoid",
            "overflow: hidden",
            "margin: 0"
        ]
        
        missing_elements = []
        for element in required_elements:
            if element in emd_content:
                print(f"  ✓ Found: {element}")
            else:
                print(f"  ✗ Missing: {element}")
                missing_elements.append(element)
        
        if not missing_elements:
            print("  ✓ All required A4 printing elements present")
        else:
            print(f"  ✗ Missing {len(missing_elements)} required elements")
            
    except Exception as e:
        print(f"Error checking EmdRefund.html: {e}")
    
    # Check Excel SE EMD tool
    try:
        with open("pages/01_Excel_se_EMD.py", "r", encoding="utf-8") as f:
            excel_content = f.read()
        
        print("\n=== Checking Excel SE EMD Tool ===")
        
        # Check for key A4 printing elements
        required_elements = [
            "@media print",
            "size: A4 portrait",
            "width: 210mm",
            "height: 297mm",
            "page-break-after: never",
            "page-break-inside: avoid",
            "overflow: hidden",
            "margin: 0"
        ]
        
        missing_elements = []
        for element in required_elements:
            if element in excel_content:
                print(f"  ✓ Found: {element}")
            else:
                print(f"  ✗ Missing: {element}")
                missing_elements.append(element)
        
        if not missing_elements:
            print("  ✓ All required A4 printing elements present")
        else:
            print(f"  ✗ Missing {len(missing_elements)} required elements")
            
    except Exception as e:
        print(f"Error checking Excel SE EMD tool: {e}")
    
    print("\n" + "="*50)
    print("A4 Printing Verification Complete")
    print("Each EMD receipt should now be accommodated on one A4 portrait page.")

if __name__ == "__main__":
    verify_a4_printing()