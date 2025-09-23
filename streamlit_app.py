import streamlit as st

from utils.branding import apply_custom_css, show_header, show_credits
from components.tool_buttons import create_tool_grid


def main():
    st.set_page_config(
        page_title="PWD Tools Hub | Infrastructure Management Suite",
        page_icon="🏗️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    apply_custom_css()
    show_header()

    st.markdown(
        """
        <div class="pwd-welcome">
          <h3 style="color:#2E8B57; margin: 0 0 8px 0;">🎯 PWD Tools Hub</h3>
          <div style="color:#333; font-size: 16px; font-weight: 700;">Infrastructure Management Tools - Simple, efficient tools for PWD operations</div>
          <div style="color:#666; font-size: 14px; margin-top: 8px;">Streamline your workflow with our comprehensive suite of engineering and financial tools</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🔧 Tools Available", "11", "✓ Ready")
    with col2:
        st.metric("🏢 Departments", "5", "✓ Active")
    with col3:
        st.metric("📈 Efficiency Gain", "75%", "↑ Improved")

    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 20px;">
          <h2 style="color: #2E8B57;">🔧 Available Tools</h2>
          <p style="color: #666; font-size: 1.1rem;">Select any tool below to get started</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    create_tool_grid()

    st.markdown("---")
    show_credits()


if __name__ == "__main__":
    main()

