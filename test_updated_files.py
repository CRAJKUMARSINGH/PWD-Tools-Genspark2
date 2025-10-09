import os
import sys

def test_emd_refund_html():
    """Test that EmdRefund.html has been updated correctly"""
    try:
        with open("static/html/EmdRefund.html", "r", encoding="utf-8") as f:
            content = f.read()
        
        print("Testing EmdRefund.html...")
        
        # Check for key features we added
        checks = [
            ("html2pdf.js", "PDF generation library included"),
            ("@page {", "Print CSS with page size"),
            ("size: A4 portrait", "A4 page size specification"),
            ("page-break-after: never", "Page break prevention"),
            ("max-width: 210mm", "Width constraint for overflow prevention"),
            ("word-wrap: break-word", "Text overflow prevention"),
            ("id=\"download-button\"", "Download button present"),
            ("downloadPDF", "PDF download function present"),
            ("Ar.", "Circular seal - Ar."),
            ("D.A.", "Circular seal - D.A."),
            ("E.E.", "Circular seal - E.E."),
        ]
        
        all_passed = True
        for check, description in checks:
            if check in content:
                print(f"  ✓ {description}")
            else:
                print(f"  ✗ {description}")
                all_passed = False
        
        return all_passed
    except Exception as e:
        print(f"Error testing EmdRefund.html: {e}")
        return False

def test_excel_se_emd():
    """Test that Excel SE EMD tool uses updated structure"""
    try:
        with open("pages/01_Excel_se_EMD.py", "r", encoding="utf-8") as f:
            content = f.read()
        
        print("\nTesting Excel SE EMD tool...")
        
        # Check for key features
        checks = [
            ("static/html/EmdRefund.html", "Uses EmdRefund.html template"),
            ("page-break-after: never", "Page break prevention"),
            ("max-width: 210mm", "Width constraint for overflow prevention"),
            ("word-wrap: break-word", "Text overflow prevention"),
        ]
        
        all_passed = True
        for check, description in checks:
            if check in content:
                print(f"  ✓ {description}")
            else:
                print(f"  ✗ {description}")
                all_passed = False
        
        return all_passed
    except Exception as e:
        print(f"Error testing Excel SE EMD tool: {e}")
        return False

def test_emd_refund_page():
    """Test that EMD Refund page is properly configured"""
    try:
        with open("pages/07_EMD_Refund.py", "r", encoding="utf-8") as f:
            content = f.read()
        
        print("\nTesting EMD Refund page...")
        
        # Check for key features
        checks = [
            ("static/html/EmdRefund.html", "Uses EmdRefund.html template"),
            ("components.html", "Uses Streamlit HTML component"),
        ]
        
        all_passed = True
        for check, description in checks:
            if check in content:
                print(f"  ✓ {description}")
            else:
                print(f"  ✗ {description}")
                all_passed = False
        
        return all_passed
    except Exception as e:
        print(f"Error testing EMD Refund page: {e}")
        return False

def main():
    print("Testing updated EMD tools...\n")
    
    # Change to the project directory
    os.chdir(r"c:\Users\Rajkumar\PWD-Tools-Genspark2")
    
    # Run all tests
    test1 = test_emd_refund_html()
    test2 = test_excel_se_emd()
    test3 = test_emd_refund_page()
    
    print(f"\n{'='*50}")
    print("FINAL TEST RESULTS:")
    print(f"{'='*50}")
    print(f"EmdRefund.html updates: {'✓ PASS' if test1 else '✗ FAIL'}")
    print(f"Excel SE EMD tool updates: {'✓ PASS' if test2 else '✗ FAIL'}")
    print(f"EMD Refund page configuration: {'✓ PASS' if test3 else '✗ FAIL'}")
    
    overall_success = test1 and test2 and test3
    print(f"\nOverall result: {'✓ ALL TESTS PASSED' if overall_success else '✗ SOME TESTS FAILED'}")
    
    if overall_success:
        print("\n🎉 All changes have been implemented properly!")
        print("Both EMD tools now use the updated EmdRefund.html content")
        print("with all required features including PDF download,")
        print("text overflow prevention, and proper print specifications.")
    else:
        print("\n❌ Some issues were detected. Please review the failed tests above.")

if __name__ == "__main__":
    main()