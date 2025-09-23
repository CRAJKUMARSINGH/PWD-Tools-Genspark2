import streamlit as st


TOOLS = [
    {"name": "Excel se EMD", "description": "Excel to EMD Refund Generator", "icon": "📊", "status": "internal"},
    {"name": "Bill Note Sheet", "description": "Generate Bill Note Sheets", "icon": "📝", "status": "internal"},
    {"name": "Bill Deviation", "description": "Infrastructure Billing System with deviation tracking", "icon": "💰", "status": "external", "url": "https://raj-bill-generator-v01.streamlit.app/"},
    {"name": "Tender Processing", "description": "Comprehensive tender management system", "icon": "📋", "status": "external", "url": "https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/"},
    {"name": "Deductions Table", "description": "Manage Deductions in Contracts", "icon": "➖", "status": "internal"},
    {"name": "Delay Calculator", "description": "Calculate Work Delays and Penalties", "icon": "⏱️", "status": "internal"},
    {"name": "EMD Refund", "description": "EMD Refund Calculator and Tracker", "icon": "💸", "status": "internal"},
    {"name": "Financial Progress", "description": "Track Financial Progress of Projects", "icon": "📈", "status": "internal"},
    {"name": "Security Refund", "description": "Security Deposit Refund Calculator", "icon": "🔒", "status": "internal"},
    {"name": "Stamp Duty", "description": "Calculate Stamp Duty for Documents", "icon": "🧾", "status": "internal"},
    {"name": "Excel se EMD Web", "description": "Excel to EMD web interface", "icon": "🌐", "status": "external", "url": "https://marudharhr.onrender.com/"},
]


def _tool_card(tool: dict):
    status_text = "🔗 External" if tool.get("status") == "external" else "🏠 Internal"
    status_color = "var(--primary-green)" if tool.get("status") != "external" else "#DC143C"

    st.markdown(
        f"""
        <div class="pwd-card">
          <div style="text-align:center; font-size: 28px;">{tool.get('icon','')}</div>
          <div style="text-align:center; font-weight: 800; color: var(--primary-green);">{tool.get('name','')}</div>
          <div style="text-align:center; color: #666; font-size: 13px; margin: 6px 0 10px;">{tool.get('description','')}</div>
          <div style="text-align:center; margin-bottom: 12px;"><span class="pwd-badge" style="color:{status_color};">{status_text}</span></div>
        """,
        unsafe_allow_html=True,
    )

    if tool.get("status") == "external" and tool.get("url"):
        st.markdown(
            f"<div style='text-align:center;'><a class='btn-link' href='{tool['url']}' target='_blank'>Open External Tool ↗</a></div>",
            unsafe_allow_html=True,
        )
    else:
        st.button("Open Tool", key=f"open_{tool.get('name','').lower().replace(' ','_')}")


def create_tool_grid():
    cols = st.columns(3)
    col_index = 0
    for tool in TOOLS:
        with cols[col_index]:
            _tool_card(tool)
        col_index += 1
        if col_index >= 3:
            col_index = 0
