try:
    import customtkinter as ctk
    print("CustomTkinter is available")
    print(f"Version: {ctk.__version__}")
except ImportError as e:
    print(f"CustomTkinter is not available: {e}")
    
try:
    import tkinter as tk
    print("Tkinter is available")
except ImportError as e:
    print(f"Tkinter is not available: {e}")