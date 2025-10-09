import os

def validate_emd_refund_html():
    """Validate that EmdRefund.html has all required features"""
    try:
        with open("static/html/EmdRefund.html", "r", encoding="utf-8") as f:
            content = f.read()
        
        print("=== Validating EmdRefund.html ===")
        
        # Check for required elements
        checks = [
            ("<!DOCTYPE html>", "HTML5 doctype"),
            ("<title>Hand Receipt (RPWA 28)</title>", "Correct title"),
            ("html2pdf.js", "PDF generation library"),
            ("@page {", "Print CSS with page size"),
            ("size: A4 portrait", "A4 page size specification"),
            ("page-break-after: never", "Page break prevention"),
            ("page-break-inside: avoid", "Page break prevention"),
            ("max-width: 210mm", "Width constraint for overflow prevention"),
            ("overflow-x: hidden", "Horizontal overflow prevention"),
            ("word-wrap: break-word", "Text overflow prevention"),
            ("overflow-wrap: break-word", "Text overflow prevention"),
            ("id=\"payee\"", "Payee input field"),
            ("id=\"amount\"", "Amount input field"),
            ("id=\"work\"", "Work input field"),
            ("id=\"generate-button\"", "Generate button"),
            ("id=\"download-button\"", "Download button"),
            ("id=\"print-button\"", "Print button"),
            ("convertNumberToWords", "Number to words function"),
            ("generateReceiptHTML", "Receipt generation function"),
            ("downloadPDF", "PDF download function"),
            ("Ar.", "Circular seal - Ar."),
            ("D.A.", "Circular seal - D.A."),
            ("E.E.", "Circular seal - E.E."),
        ]
        
        passed = 0
        failed = 0
        
        for check, description in checks:
            if check in content:
                print(f"✓ {description}")
                passed += 1
            else:
                print(f"✗ {description}")
                failed += 1
        
        print(f"\nValidation Results: {passed} passed, {failed} failed")
        return failed == 0
        
    except Exception as e:
        print(f"Error validating EmdRefund.html: {e}")
        return False

def validate_excel_se_emd():
    """Validate that Excel SE EMD tool uses the updated HTML structure"""
    try:
        with open("pages/01_Excel_se_EMD.py", "r", encoding="utf-8") as f:
            content = f.read()
        
        print("\n=== Validating Excel SE EMD Tool ===")
        
        # Check for required elements
        checks = [
            ("build_receipt_html", "Receipt generation function"),
            ("static/html/EmdRefund.html", "Uses EmdRefund.html template"),
            ("page-break-after: never", "Page break prevention"),
            ("page-break-inside: avoid", "Page break prevention"),
            ("max-width: 210mm", "Width constraint for overflow prevention"),
            ("overflow-x: hidden", "Horizontal overflow prevention"),
            ("word-wrap: break-word", "Text overflow prevention"),
            ("overflow-wrap: break-word", "Text overflow prevention"),
        ]
        
        passed = 0
        failed = 0
        
        for check, description in checks:
            if check in content:
                print(f"✓ {description}")
                passed += 1
            else:
                print(f"✗ {description}")
                failed += 1
        
        print(f"\nValidation Results: {passed} passed, {failed} failed")
        return failed == 0
        
    except Exception as e:
        print(f"Error validating Excel SE EMD tool: {e}")
        return False

def validate_emd_refund_page():
    """Validate that EMD Refund page is properly configured"""
    try:
        with open("pages/07_EMD_Refund.py", "r", encoding="utf-8") as f:
            content = f.read()
        
        print("\n=== Validating EMD Refund Page ===")
        
        # Check for required elements
        checks = [
            ("static/html/EmdRefund.html", "Uses EmdRefund.html template"),
            ("components.html", "Uses Streamlit HTML component"),
            ("PDF will be automatically downloaded", "Mentions PDF download"),
        ]
        
        passed = 0
        failed = 0
        
        for check, description in checks:
            if check in content:
                print(f"✓ {description}")
                passed += 1
            else:
                print(f"✗ {description}")
                failed += 1
        
        print(f"\nValidation Results: {passed} passed, {failed} failed")
        return failed == 0
        
    except Exception as e:
        print(f"Error validating EMD Refund page: {e}")
        return False

if __name__ == "__main__":
    print("Validating EMD tools updates...\n")
    
    emd_refund_html_valid = validate_emd_refund_html()
    excel_se_emd_valid = validate_excel_se_emd()
    emd_refund_page_valid = validate_emd_refund_page()
    
    print(f"\n{'='*50}")
    print("FINAL VALIDATION RESULTS:")
    print(f"{'='*50}")
    print(f"EmdRefund.html: {'✓ PASS' if emd_refund_html_valid else '✗ FAIL'}")
    print(f"Excel SE EMD Tool: {'✓ PASS' if excel_se_emd_valid else '✗ FAIL'}")
    print(f"EMD Refund Page: {'✓ PASS' if emd_refund_page_valid else '✗ FAIL'}")
    
    overall_success = emd_refund_html_valid and excel_se_emd_valid and emd_refund_page_valid
    print(f"\nOverall: {'✓ ALL CHECKS PASSED' if overall_success else '✗ SOME CHECKS FAILED'}")