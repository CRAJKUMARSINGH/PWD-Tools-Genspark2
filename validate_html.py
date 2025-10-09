import os
import re

def validate_html_file():
    # Check if the HTML file exists
    html_file_path = "static/html/EmdRefund.html"
    if os.path.exists(html_file_path):
        print(f"✓ HTML file exists at {html_file_path}")
        
        # Try to read the file
        try:
            with open(html_file_path, "r", encoding="utf-8") as f:
                content = f.read()
                print(f"✓ HTML file read successfully, {len(content)} characters")
                
                # Check for key elements
                if "<title>Hand Receipt (RPWA 28)</title>" in content:
                    print("✓ Title found")
                else:
                    print("✗ Title not found")
                    
                if "generateReceiptHTML" in content:
                    print("✓ JavaScript function found")
                else:
                    print("✗ JavaScript function not found")
                    
                # Check for CSS syntax error fixes
                if "@page {" in content and "size: A4 portrait;" in content:
                    print("✓ CSS syntax error fixed (@page rule)")
                else:
                    print("✗ CSS syntax error may still exist")
                    
                # Check for form elements
                required_elements = [
                    'id="payee"',
                    'id="amount"',
                    'id="work"',
                    'id="generate-button"'
                ]
                
                missing_elements = []
                for element in required_elements:
                    if element in content:
                        print(f"✓ {element} found")
                    else:
                        missing_elements.append(element)
                        
                if missing_elements:
                    print(f"✗ Missing elements: {missing_elements}")
                else:
                    print("✓ All required form elements found")
                    
        except Exception as e:
            print(f"✗ Error reading HTML file: {e}")
    else:
        print(f"✗ HTML file does not exist at {html_file_path}")

if __name__ == "__main__":
    validate_html_file()