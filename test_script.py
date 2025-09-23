print("Hello PWD Tools!")
print("This is a test script.")

# List files in pages directory
import os
if os.path.exists("pages"):
    print("\nFiles in 'pages' directory:")
    for file in sorted(os.listdir("pages")):
        if file.endswith(".py"):
            print(f"  - {file}")
else:
    print("\n'pages' directory not found")