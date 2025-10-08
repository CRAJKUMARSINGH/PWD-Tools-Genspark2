import streamlit as st
import time
import sys
import os

# Ensure the current directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import branding and tool components
from utils.branding import apply_custom_css, show_header, show_credits, get_tool_colors
from components.tool_buttons import create_tool_grid

# Page configuration with improved settings
st.set_page_config(
    page_title="PWD Tools Hub | Infrastructure Management Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/CRAJKUMARSINGH/PWD-Tools-Genspark',
        'Report a bug': 'https://github.com/CRAJKUMARSINGH/PWD-Tools-Genspark/issues',
        'About': "# PWD Tools Hub\nInfrastructure Management Suite for Public Works Department"
    }
)

# Apply custom styling and branding
apply_custom_css()

def main():
    """Main application function that renders the dashboard"""
    # Show header with branding
    show_header()
    
    # Welcome section with improved styling
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### 🎯 PWD Tools Hub")
        st.markdown("**Infrastructure Management Tools** - Streamlining PWD operations with digital solutions")
    
    with col2:
        # Display a small stats card
        colors = get_tool_colors()
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, {colors['background']} 0%, #f8f9fa 100%); 
                        padding: 10px; border-radius: 10px; 
                        border-left: 4px solid {colors['primary']};">
                <h4 style="margin:0;">Tools Available</h4>
                <p style="font-size: 1.5rem; font-weight: bold; margin:0;">12+</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    
    # Tools grid section with enhanced styling
    st.markdown("### 🔧 Available Tools")
    st.markdown("Click on any tool to get started:")
    
    # Create the main tool grid with CTkButton styling
    create_tool_grid()
    
    # Removed JavaScript for better performance
    
    # Show credits at bottom
    st.markdown("---")
    show_credits()

# Main app execution - only run when this file is executed directly
if __name__ == "__main__":
    main()