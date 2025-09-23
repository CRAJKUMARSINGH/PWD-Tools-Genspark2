"""
Main PWD Tools application using CustomTkinter
"""

import customtkinter as ctk
import sys
import os

# Add the components directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'components'))

from components.custom_tool_buttons import CustomToolGrid

class PWDToolsCustomApp:
    def __init__(self):
        # Initialize CustomTkinter
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("PWD Tools Hub | Infrastructure Management Suite")
        self.root.geometry("1400x900")
        self.root.minsize(800, 600)
        
        # Create main interface
        self.create_main_interface()
        
    def create_main_interface(self):
        """Create the main application interface"""
        # Header Frame - matching reference_app styling
        header_frame = ctk.CTkFrame(self.root, height=120, fg_color="#2E8B57")
        header_frame.pack(fill="x", padx=10, pady=5)
        header_frame.pack_propagate(False)

        title_label = ctk.CTkLabel(
            header_frame,
            text="🏗️ PWD Tools Dashboard",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        )
        title_label.pack(pady=(15, 5))

        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Infrastructure Management Suite for Lower Divisional Clerks",
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

        # Welcome section - aligned to green palette used across landing pages
        welcome_frame = ctk.CTkFrame(self.root, fg_color=["#f0f8f5", "#e8f5e8"])
        welcome_frame.pack(fill="x", padx=10, pady=5)

        welcome_label = ctk.CTkLabel(
            welcome_frame,
            text="🎉 Welcome to PWD Tools - Simple & Efficient!",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#2E8B57"
        )
        welcome_label.pack(pady=15)

        # Stats section - matching reference_app layout
        self.create_stats_section()

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

        # Main Content Frame for tools
        content_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Create tool grid using CustomTkinter with CTkButton
        self.tool_grid = CustomToolGrid(content_frame)
        self.tool_grid.create_tool_grid()

        # Footer - matching reference_app styling
        self.create_footer()

    def create_stats_section(self):
        """Create stats cards section matching reference_app"""
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
            text="🔧 12",
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
            text="🏢 3",
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

    def create_footer(self):
        """Create colorful footer matching reference_app"""
        footer_frame = ctk.CTkFrame(self.root, height=60, fg_color="#2E8B57")
        footer_frame.pack(fill="x", pady=(20, 0))
        footer_frame.pack_propagate(False)

        # Footer content
        footer_content = ctk.CTkFrame(footer_frame, fg_color="#2E8B57")
        footer_content.pack(expand=True)

        # Left side - Version info
        version_label = ctk.CTkLabel(
            footer_content,
            text="Version 1.0.0 | Simple & Efficient",
            font=ctk.CTkFont(size=10),
            text_color="white"
        )
        version_label.pack(side="left", padx=20, pady=20)

        # Right side - Quick actions
        quick_frame = ctk.CTkFrame(footer_content, fg_color="#2E8B57")
        quick_frame.pack(side="right", padx=20, pady=20)

        help_btn = ctk.CTkButton(
            quick_frame,
            text="Help",
            command=self.show_help,
            width=60,
            height=30,
            font=ctk.CTkFont(size=9),
            fg_color=["#2E8B57", "#3CB371"],
            hover_color=["#228B22", "#2E8B57"]
        )
        help_btn.pack(side="left", padx=5)

        about_btn = ctk.CTkButton(
            quick_frame,
            text="About",
            command=self.show_about,
            width=60,
            height=30,
            font=ctk.CTkFont(size=9),
            fg_color=["#2E8B57", "#3CB371"],
            hover_color=["#228B22", "#2E8B57"]
        )
        about_btn.pack(side="left", padx=5)

    def run(self):
        """Run the application"""
        self.root.mainloop()

    def show_help(self):
        # Add help functionality here
        pass

    def show_about(self):
        # Add about functionality here
        pass

if __name__ == "__main__":
    app = PWDToolsCustomApp()
    app.run()