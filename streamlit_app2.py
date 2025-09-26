import streamlit as st

from utils.branding import apply_custom_css, show_header, show_credits
from components.tool_buttons import TOOLS, _tool_card


def create_filtered_tool_grid(tools):
    cols = st.columns(3)
    col_index = 0
    for tool in tools:
        with cols[col_index]:
            _tool_card(tool)
        col_index += 1
        if col_index >= 3:
            col_index = 0


def main():
    st.set_page_config(
        page_title="PWD Tools Hub | Sophisticated Tools",
        page_icon="🧪",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    apply_custom_css()
    show_header()

    st.markdown(
        """
        <div class="pwd-welcome">
          <h3 style="color:#2E8B57; margin: 0 0 8px 0;">🧪 Sophisticated Tools</h3>
          <div style="color:#333; font-size: 16px; font-weight: 700;">Advanced and external tools for specialized workflows</div>
          <div style="color:#666; font-size: 14px; margin-top: 8px;">Includes integrations and feature-rich modules</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 20px;">
          <h2 style="color: #2E8B57;">🧰 Available Sophisticated Tools</h2>
          <p style="color: #666; font-size: 1.1rem;">External and advanced tools</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    sophisticated_tools = [tool for tool in TOOLS if tool.get("status") == "external"]
    create_filtered_tool_grid(sophisticated_tools)

    st.markdown("---")
    show_credits()


if __name__ == "__main__":
    main()

