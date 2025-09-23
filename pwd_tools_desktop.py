"""
Complete PWD Tools Desktop Application using CustomTkinter
This replaces the Streamlit version with a standalone desktop application
"""

import customtkinter as ctk
import webbrowser
import os
import sys
from tkinter import messagebox

class PWDToolsDesktopApp:
    def __init__(self):
        # Initialize CustomTkinter
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("PWD Tools Hub | Infrastructure Management Suite")
        self.root.geometry("1400x900")
        self.root.minsize(1000, 700)
        
        # Tool definitions with categories and external links
        self.tools = [
            {
                "name": "Excel se EMD",
                "description": "Excel to EMD Refund Generator",
                "icon": "📊",
                "category": "financial",
                "status": "internal",
                "function": self.open_excel_emd_refund
            },
            {
                "name": "Bill Note Sheet",
                "description": "Generate Bill Note Sheets",
                "icon": "📝",
                "category": "financial",
                "status": "internal",
                "function": self.open_bill_note_sheet
            },
            {
                "name": "Bill Deviation",
                "description": "Infrastructure Billing System with deviation tracking",
                "icon": "💰",
                "category": "financial",
                "status": "external",
                "url": "https://raj-bill-generator-v01.streamlit.app/",
                "page": "pages/02_Bill_Deviation.py"
            },
            {
                "name": "Tender Processing",
                "description": "Comprehensive tender management system",
                "icon": "📋",
                "category": "processing",
                "status": "external",
                "url": "https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/",
                "page": "pages/03_Tender_Processing.py"
            },
            {
                "name": "Deductions Table",
                "description": "Manage Deductions in Contracts",
                "icon": "➖",
                "category": "financial",
                "status": "internal",
                "function": self.open_deductions_table
            },
            {
                "name": "Delay Calculator",
                "description": "Calculate Work Delays and Penalties",
                "icon": "⏱️",
                "category": "calculations",
                "status": "internal",
                "function": self.open_delay_calculator
            },
            {
                "name": "EMD Refund",
                "description": "EMD Refund Calculator and Tracker",
                "icon": "💸",
                "category": "financial",
                "status": "internal",
                "function": self.open_emd_refund
            },
            {
                "name": "Financial Progress",
                "description": "Track Financial Progress of Projects",
                "icon": "📈",
                "category": "monitoring",
                "status": "internal",
                "function": self.open_financial_progress
            },
            {
                "name": "Security Refund",
                "description": "Security Deposit Refund Calculator",
                "icon": "🔒",
                "category": "financial",
                "status": "internal",
                "function": self.open_security_refund
            },
            {
                "name": "Stamp Duty",
                "description": "Calculate Stamp Duty for Documents",
                "icon": " Stamp Duty Calculator",
                "category": "calculations",
                "status": "internal",
                "function": self.open_stamp_duty
            },
            {
                "name": "Excel se EMD Web",
                "description": "Excel to EMD web interface",
                "icon": "🌐",
                "category": "financial",
                "status": "external",
                "url": "https://marudharhr.onrender.com/",
                "page": "pages/12_Excel_to_EMD_Web.py"
            }
        ]
        
        # Create main interface
        self.create_main_interface()
        
    def create_main_interface(self):
        """Create the main application interface with CustomTkinter"""
        # Header Frame
        header_frame = ctk.CTkFrame(self.root, height=120, fg_color=["#1a5d38", "#2E8B57"])
        header_frame.pack(fill="x", padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        title_label = ctk.CTkLabel(
            header_frame,
            text="🏗️ PWD Tools Hub",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        )
        title_label.pack(pady=(15, 5))
        
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Infrastructure Management Suite",
            font=ctk.CTkFont(size=18),
            text_color="white"
        )
        subtitle_label.pack(pady=(0, 5))
        
        description_label = ctk.CTkLabel(
            header_frame,
            text="Empowering Public Works Department with digital tools for efficient infrastructure management",
            font=ctk.CTkFont(size=12),
            text_color=["#e0e0e0", "#d0d0d0"],
            wraplength=800
        )
        description_label.pack(pady=(0, 10))
        
        # Welcome section
        welcome_frame = ctk.CTkFrame(self.root, fg_color=["#f0f8f5", "#e8f5e8"])
        welcome_frame.pack(fill="x", padx=10, pady=5)
        
        welcome_title = ctk.CTkLabel(
            welcome_frame,
            text="🎯 PWD Tools Hub",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#2E8B57"
        )
        welcome_title.pack(pady=(15, 5))
        
        welcome_text = ctk.CTkLabel(
            welcome_frame,
            text="Infrastructure Management Tools - Simple, efficient tools for PWD operations",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=["#333333", "#222222"]
        )
        welcome_text.pack(pady=(0, 5))
        
        welcome_desc = ctk.CTkLabel(
            welcome_frame,
            text="Streamline your workflow with our comprehensive suite of engineering and financial tools",
            font=ctk.CTkFont(size=12),
            text_color=["#666666", "#555555"]
        )
        welcome_desc.pack(pady=(0, 15))
        
        # Stats section
        stats_frame = ctk.CTkFrame(self.root)
        stats_frame.pack(fill="x", padx=10, pady=5)
        
        # Create stats in a grid
        stats_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Tools available stat
        tools_frame = ctk.CTkFrame(stats_frame, fg_color=["#f8f9fa", "#e9ecef"])
        tools_frame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        tools_frame.grid_columnconfigure(0, weight=1)
        
        tools_value = ctk.CTkLabel(
            tools_frame,
            text="🔧 11",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=["#2E8B57", "#228B22"]
        )
        tools_value.grid(row=0, column=0, pady=(10, 0))
        
        tools_label = ctk.CTkLabel(
            tools_frame,
            text="Tools Available",
            font=ctk.CTkFont(size=12),
            text_color=["#333333", "#222222"]
        )
        tools_label.grid(row=1, column=0, pady=(0, 10))
        
        # Departments stat
        dept_frame = ctk.CTkFrame(stats_frame, fg_color=["#f8f9fa", "#e9ecef"])
        dept_frame.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        dept_frame.grid_columnconfigure(0, weight=1)
        
        dept_value = ctk.CTkLabel(
            dept_frame,
            text="🏢 5",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=["#2E8B57", "#228B22"]
        )
        dept_value.grid(row=0, column=0, pady=(10, 0))
        
        dept_label = ctk.CTkLabel(
            dept_frame,
            text="Departments",
            font=ctk.CTkFont(size=12),
            text_color=["#333333", "#222222"]
        )
        dept_label.grid(row=1, column=0, pady=(0, 10))
        
        # Efficiency stat
        eff_frame = ctk.CTkFrame(stats_frame, fg_color=["#f8f9fa", "#e9ecef"])
        eff_frame.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        eff_frame.grid_columnconfigure(0, weight=1)
        
        eff_value = ctk.CTkLabel(
            eff_frame,
            text="📈 75%",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=["#2E8B57", "#228B22"]
        )
        eff_value.grid(row=0, column=0, pady=(10, 0))
        
        eff_label = ctk.CTkLabel(
            eff_frame,
            text="Efficiency Gain",
            font=ctk.CTkFont(size=12),
            text_color=["#333333", "#222222"]
        )
        eff_label.grid(row=1, column=0, pady=(0, 10))
        
        # Tools section title
        tools_title_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        tools_title_frame.pack(fill="x", padx=10, pady=(20, 5))
        
        tools_title = ctk.CTkLabel(
            tools_title_frame,
            text="🔧 Available Tools",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#2E8B57"
        )
        tools_title.pack(pady=5)
        
        tools_desc = ctk.CTkLabel(
            tools_title_frame,
            text="Select any tool below to get started",
            font=ctk.CTkFont(size=12),
            text_color=["#666666", "#555555"]
        )
        tools_desc.pack(pady=(0, 5))
        
        # Main Content Frame for tools
        content_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Create tool grid using CustomTkinter with CTkButton
        self.create_tool_grid(content_frame)
        
        # Help section
        help_frame = ctk.CTkFrame(self.root, fg_color=["#f8f9fa", "#e9ecef"])
        help_frame.pack(fill="x", padx=10, pady=5)
        
        help_title = ctk.CTkLabel(
            help_frame,
            text="💡 Need Help?",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#2E8B57"
        )
        help_title.pack(pady=(15, 5))
        
        help_text = ctk.CTkLabel(
            help_frame,
            text="All tools are designed to be intuitive and user-friendly. For any assistance, please contact Mrs. Premlata Jain, AAO, PWD Udaipur",
            font=ctk.CTkFont(size=12),
            text_color=["#555555", "#444444"],
            wraplength=800
        )
        help_text.pack(pady=(0, 15))
        
        # Credits section
        credits_frame = ctk.CTkFrame(self.root, height=150, fg_color=["#1a5d38", "#2E8B57"])
        credits_frame.pack(fill="x", padx=10, pady=5)
        credits_frame.pack_propagate(False)
        
        credits_title = ctk.CTkLabel(
            credits_frame,
            text="🏆 Initiative Credit",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="white"
        )
        credits_title.pack(pady=(15, 5))
        
        credits_name = ctk.CTkLabel(
            credits_frame,
            text="Mrs. Premlata Jain",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="white"
        )
        credits_name.pack(pady=(0, 2))
        
        credits_position = ctk.CTkLabel(
            credits_frame,
            text="Additional Administrative Officer\nPublic Works Department (PWD), Udaipur",
            font=ctk.CTkFont(size=12),
            text_color=["#f0f0f0", "#e0e0e0"],
            justify="center"
        )
        credits_position.pack(pady=(0, 5))
        
        credits_quote = ctk.CTkLabel(
            credits_frame,
            text='"Empowering Infrastructure Excellence Through Digital Innovation"',
            font=ctk.CTkFont(size=12, slant="italic"),
            text_color="white"
        )
        credits_quote.pack(pady=(0, 5))
        
        credits_version = ctk.CTkLabel(
            credits_frame,
            text="Version 2.0 | Last Updated: September 2025",
            font=ctk.CTkFont(size=10),
            text_color=["#e0e0e0", "#d0d0d0"]
        )
        credits_version.pack(pady=(0, 10))
        
    def create_tool_grid(self, parent):
        """Create the main grid of tool buttons with CustomTkinter (CTkButton)"""
        # Header with tool count
        header_frame = ctk.CTkFrame(parent, height=60, fg_color="#2E8B57")
        header_frame.pack(fill="x", padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        header_label = ctk.CTkLabel(
            header_frame,
            text="🏗️ 11 Essential Tools Available",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="white"
        )
        header_label.pack(pady=10)
        
        # Tools grid frame
        grid_frame = ctk.CTkFrame(parent, fg_color="transparent")
        grid_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Create grid layout with 3 columns per row (as requested)
        row, col = 0, 0
        for tool in self.tools:
            # Create tool button
            self.create_tool_button(grid_frame, tool, row, col)
            
            # Update grid position
            col += 1
            if col > 2:  # 3 columns per row
                col = 0
                row += 1
                
        # Configure grid weights
        for i in range(3):
            grid_frame.grid_columnconfigure(i, weight=1)
            
    def create_tool_button(self, parent, tool, row, col):
        """Create individual tool button with CustomTkinter CTkButton"""
        # Tool button frame
        button_frame = ctk.CTkFrame(
            parent, 
            corner_radius=15,
            fg_color=["#ffffff", "#f8f9fa"],
            border_width=2,
            border_color=["#2E8B57", "#2E8B57"]
        )
        button_frame.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
        
        # Bind hover effects to the entire button frame
        button_frame.bind("<Enter>", lambda e: self.on_enter(button_frame))
        button_frame.bind("<Leave>", lambda e: self.on_leave(button_frame))
        
        # Icon label
        icon_label = ctk.CTkLabel(
            button_frame,
            text=tool["icon"],
            font=ctk.CTkFont(size=32)
        )
        icon_label.pack(pady=(20, 10))
        
        # Tool name
        name_label = ctk.CTkLabel(
            button_frame,
            text=tool["name"],
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#2E8B57"
        )
        name_label.pack(pady=(0, 5))
        
        # Tool description
        desc_label = ctk.CTkLabel(
            button_frame,
            text=tool["description"],
            font=ctk.CTkFont(size=12),
            text_color=["#555555", "#AAAAAA"],
            wraplength=200
        )
        desc_label.pack(pady=(0, 15))
        
        # Status indicator
        status_text = "🔗 External" if tool["status"] == "external" else "🏠 Internal"
        status_color = "#DC143C" if tool["status"] == "external" else "#2E8B57"
        
        status_label = ctk.CTkLabel(
            button_frame,
            text=status_text,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=status_color,
            fg_color=["#f0f8f5", "#e8f5e8"],
            corner_radius=10
        )
        status_label.pack(pady=(0, 15))
        
        # Action button using CTkButton with specific styling (as requested)
        if tool["status"] == "external" and tool["url"]:
            action_button = ctk.CTkButton(
                button_frame,
                text="Open External Tool ↗",
                command=lambda url=tool["url"]: self.open_external_tool(url),
                fg_color=["#2E8B57", "#3CB371"],  # Specific colors
                hover_color=["#228B22", "#2E8B57"],  # Hover effects
                corner_radius=12,
                height=40,
                font=ctk.CTkFont(weight="bold")
            )
        else:
            action_button = ctk.CTkButton(
                button_frame,
                text="Open Tool",
                command=lambda func=tool.get("function"): self.open_internal_tool(func),
                fg_color=["#2E8B57", "#3CB371"],  # Specific colors
                hover_color=["#228B22", "#2E8B57"],  # Hover effects
                corner_radius=12,
                height=40,
                font=ctk.CTkFont(weight="bold")
            )
            
        action_button.pack(pady=(0, 20), padx=20, fill="x")
        
        # Bind hover effects to all child widgets
        for child in button_frame.winfo_children():
            child.bind("<Enter>", lambda e, frame=button_frame: self.on_enter(frame))
            child.bind("<Leave>", lambda e, frame=button_frame: self.on_leave(frame))
            
    def on_enter(self, button_frame):
        """Hover enter effect"""
        button_frame.configure(fg_color=["#f0f8f5", "#e8f5e8"])
        button_frame.configure(border_color=["#228B22", "#228B22"])
        
    def on_leave(self, button_frame):
        """Hover leave effect"""
        button_frame.configure(fg_color=["#ffffff", "#f8f9fa"])
        button_frame.configure(border_color=["#2E8B57", "#2E8B57"])
        
    def open_external_tool(self, url):
        """Open external tool in browser"""
        try:
            webbrowser.open(url)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open URL: {str(e)}")
            
    def open_internal_tool(self, function):
        """Open internal tool by calling its function"""
        if function:
            function()
        else:
            messagebox.showinfo("Tool", "Tool not implemented yet")
    
    # Tool opening methods
    def open_excel_emd_refund(self):
        """Open Excel se EMD tool"""
        messagebox.showinfo("Excel se EMD", "Excel se EMD tool would open here")
    
    def open_bill_note_sheet(self):
        """Open Bill Note Sheet tool"""
        messagebox.showinfo("Bill Note Sheet", "Bill Note Sheet tool would open here")
    
    def open_deductions_table(self):
        """Open Deductions Table tool"""
        messagebox.showinfo("Deductions Table", "Deductions Table tool would open here")
    
    def open_delay_calculator(self):
        """Open Delay Calculator tool"""
        messagebox.showinfo("Delay Calculator", "Delay Calculator tool would open here")
    
    def open_emd_refund(self):
        """Open EMD Refund tool"""
        messagebox.showinfo("EMD Refund", "EMD Refund tool would open here")
    
    def open_financial_progress(self):
        """Open Financial Progress tool"""
        messagebox.showinfo("Financial Progress", "Financial Progress tool would open here")
    
    def open_security_refund(self):
        """Open Security Refund tool"""
        messagebox.showinfo("Security Refund", "Security Refund tool would open here")
    
    def open_stamp_duty(self):
        """Open Stamp Duty tool"""
        messagebox.showinfo("Stamp Duty", "Stamp Duty tool would open here")
    
    def open_hand_receipt(self):
        """Open Hand Receipt tool"""
        messagebox.showinfo("Hand Receipt", "Hand Receipt tool would open here")
        
    def run(self):
        """Run the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = PWDToolsDesktopApp()
    app.run()