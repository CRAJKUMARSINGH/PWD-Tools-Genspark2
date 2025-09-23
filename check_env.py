import sys
print("Python version:", sys.version)
print("Python executable:", sys.executable)

try:
    import customtkinter as ctk
    print("CustomTkinter imported successfully")
    print("CustomTkinter version:", ctk.__version__)
except ImportError as e:
    print("Failed to import CustomTkinter:", e)

try:
    import tkinter
    print("Tkinter imported successfully")
except ImportError as e:
    print("Failed to import Tkinter:", e)