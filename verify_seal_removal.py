import os

def verify_seal_removal():
    """Verify that the circular seal has been removed from all relevant files"""
    
    print("Verifying circular seal removal...")
    
    # Check EmdRefund.html
    try:
        with open("static/html/EmdRefund.html", "r", encoding="utf-8") as f:
            emd_content = f.read()
        
        seal_indicators = [
            ".seal-container",
            ".seal {",
            "Ar.",
            "D.A.",
            "E.E.",
            "circular seal"
        ]
        
        print("\n=== Checking EmdRefund.html ===")
        seal_found = False
        for indicator in seal_indicators:
            if indicator in emd_content:
                # Check if it's in a comment or actual code
                lines = emd_content.split('\n')
                for i, line in enumerate(lines):
                    if indicator in line and not line.strip().startswith('<!--') and not line.strip().startswith('*'):
                        print(f"  ⚠️  Found potential seal indicator: '{indicator}' at line {i+1}")
                        print(f"      Context: {line.strip()}")
                        seal_found = True
        
        if not seal_found:
            print("  ✓ No circular seal elements found")
        else:
            print("  ✗ Circular seal elements may still be present")
            
    except Exception as e:
        print(f"Error checking EmdRefund.html: {e}")
    
    # Check Excel SE EMD tool
    try:
        with open("pages/01_Excel_se_EMD.py", "r", encoding="utf-8") as f:
            excel_content = f.read()
        
        seal_indicators = [
            ".seal-container",
            ".seal {",
            "Ar.",
            "D.A.",
            "E.E.",
            "circular seal"
        ]
        
        print("\n=== Checking Excel SE EMD Tool ===")
        seal_found = False
        for indicator in seal_indicators:
            if indicator in excel_content:
                # Check if it's in a comment or actual code
                lines = excel_content.split('\n')
                for i, line in enumerate(lines):
                    if indicator in line and not line.strip().startswith('#') and not line.strip().startswith('<!--'):
                        print(f"  ⚠️  Found potential seal indicator: '{indicator}' at line {i+1}")
                        print(f"      Context: {line.strip()}")
                        seal_found = True
        
        if not seal_found:
            print("  ✓ No circular seal elements found")
        else:
            print("  ✗ Circular seal elements may still be present")
            
    except Exception as e:
        print(f"Error checking Excel SE EMD tool: {e}")
    
    print("\n" + "="*50)
    print("Verification complete. Please review any warnings above.")
    print("The circular seal should now be removed from all EMD tools.")

if __name__ == "__main__":
    verify_seal_removal()