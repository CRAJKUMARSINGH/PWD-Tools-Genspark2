import streamlit as st
import time
from utils.branding import apply_custom_css, show_header, show_credits, show_balloons
from components.tool_buttons import create_tool_grid

# Page configuration
st.set_page_config(
    page_title="PWD Tools Hub | Infrastructure Management Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling and branding
apply_custom_css()

# Show header with branding
show_header()

# Enhanced welcome section with animation
def main():
    # Welcome section with enhanced styling
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%); border-radius: 15px; margin-bottom: 25px;">
        <h2 style="color: #2E8B57; margin-bottom: 10px;">🎯 PWD Tools Hub</h2>
        <p style="font-size: 1.2rem; color: #333; max-width: 800px; margin: 0 auto;">
            <strong>Infrastructure Management Tools</strong> - Simple, efficient tools for PWD operations
        </p>
        <p style="font-size: 1rem; color: #666; max-width: 800px; margin: 15px auto 0;">
            Streamline your workflow with our comprehensive suite of engineering and financial tools
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats section
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🔧 Tools Available", "6", "✓ Ready")
    with col2:
        st.metric("🏢 Departments", "3", "✓ Active")
    with col3:
        st.metric("📈 Efficiency Gain", "75%", "↑ Improved")
    
    st.markdown("---")
    
    # Tools grid section with enhanced title
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="color: #2E8B57;">🔧 Available Tools</h2>
        <p style="color: #666; font-size: 1.1rem;">Select any tool below to get started</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create the main tool grid
    create_tool_grid()
    
    # Additional information section
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 15px; margin-top: 25px;">
        <h3 style="color: #2E8B57;">💡 Need Help?</h3>
        <p style="font-size: 1rem; color: #555; max-width: 800px; margin: 0 auto;">
            All tools are designed to be intuitive and user-friendly. For any assistance, please contact 
            <strong>Mrs. Premlata Jain, AAO, PWD Udaipur</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Main app execution
if __name__ == "__main__":
    main()
    
    # Show credits at bottom
    st.markdown("---")
    show_credits()