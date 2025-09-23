# Check the number of tools in the main application
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and check tool count
from pwd_tools_desktop import PWDToolsDesktopApp

app = PWDToolsDesktopApp()
print(f"Number of tools defined: {len(app.tools)}")

print("\nTool list:")
for i, tool in enumerate(app.tools, 1):
    print(f"{i:2d}. {tool['name']} ({tool['status']})")