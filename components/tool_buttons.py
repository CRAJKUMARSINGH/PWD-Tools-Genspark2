import streamlit as st
from utils.branding import get_tool_colors

def create_tool_grid():
    """Create the main grid of tool buttons with enhanced CTkButton styling using a 3-column layout"""
    
    # Tool definitions with categories and external links
    # Updated to match actual available pages
    tools = [
        {
            "name": "Excel se EMD",
            "description": "Excel to EMD Refund Generator",
            "icon": "📊",
            "category": "financial",
            "status": "internal",
            "page": "pages/01_Excel_se_EMD.py"
        },
        {
            "name": "Bill & Deviation",
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
            "name": "Bill Note Sheet",
            "description": "Generate Bill Note Sheets",
            "icon": "📝",
            "category": "financial",
            "status": "internal",
            "page": "pages/04_Bill_Note_Sheet.py"
        },
        {
            "name": "Deductions Table",
            "description": "Manage Deductions in Contracts",
            "icon": "➖",
            "category": "financial",
            "status": "internal",
            "page": "pages/05_Deductions_Table.py"
        },
        {
            "name": "EMD Refund",
            "description": "EMD Refund Calculator and Tracker",
            "icon": "💸",
            "category": "financial",
            "status": "internal",
            "page": "pages/07_EMD_Refund.py"
        },
        {
            "name": "Financial Progress",
            "description": "Track Financial Progress of Projects",
            "icon": "📈",
            "category": "monitoring",
            "status": "internal",
            "page": "pages/08_Financial_Progress.py"
        },
        {
            "name": "Security Refund",
            "description": "Security Deposit Refund Calculator",
            "icon": "🔒",
            "category": "financial",
            "status": "internal",
            "page": "pages/09_Security_Refund.py"
        },
        {
            "name": "Stamp Duty",
            "description": "Calculate Stamp Duty for Documents",
            "icon": "⚖️",
            "category": "calculations",
            "status": "internal",
            "page": "pages/10_Stamp_Duty.py"
        },
        {
            "name": "Excel to EMD Web",
            "description": "Web-based EMD conversion tool",
            "icon": "🌐",
            "category": "financial",
            "status": "internal",
            "page": "pages/12_Excel_to_EMD_Web.py"
        }
    ]
    
    # Use existing color scheme from branding
    colors = get_tool_colors()
    
    # Create header with tool count
    st.markdown(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <div class="header-container" style="padding: 10px 20px; border-radius: 50px; font-weight: bold;">
            🏗️ {len(tools)} Essential Tools Available
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create 3-column grid layout for tools
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    
    # Create CTkButton styled buttons with magenta color emphasis
    for i, tool in enumerate(tools):
        with columns[i % 3]:
            # Create a CTkButton styled button for the tool with magenta emphasis
            button_label = f"""
            <div style="
                background: linear-gradient(135deg, #f8f0fa 0%, #fce4ec 100%);
                border: 2px solid #FF00FF;
                border-radius: 12px;
                padding: 20px;
                margin: 10px 0;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                min-height: 180px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            ">
                <div style="font-size: 2.5rem; margin-bottom: 10px;">{tool['icon']}</div>
                <div style="font-weight: bold; font-size: 1.1rem; margin-bottom: 8px; color: #C71585;">{tool['name']}</div>
                <div style="font-size: 0.9rem; color: #666; margin-bottom: 10px;">{tool['description']}</div>
                <div style="font-size: 0.8rem; padding: 3px 8px; border-radius: 10px; display: inline-block; 
                    background-color: {'#C71585' if tool['status'] == 'internal' else '#9B0E66'}; 
                    color: white;">
                    {tool['status'].capitalize()}
                </div>
            </div>
            """
            
            # Create navigation buttons
            if tool['status'] == 'internal':
                # For internal tools, use switch_page
                if st.button(f"{tool['name']} Tool", key=f"tool-button-{i}", use_container_width=True):
                    st.switch_page(tool['page'])
                # Display the styled button as static content below the actual button
                st.markdown(button_label, unsafe_allow_html=True)
            else:
                # For external tools, use link_button if URL exists
                if 'url' in tool and tool['url']:
                    st.link_button(f"Open {tool['name']}", tool['url'], use_container_width=True)
                    # Display the styled button as static content
                    st.markdown(button_label, unsafe_allow_html=True)
                else:
                    # Fallback for external tools without URL
                    if st.button(f"{tool['name']} Tool", key=f"tool-button-{i}", use_container_width=True):
                        st.switch_page(tool['page'])
                    # Display the styled button as static content
                    st.markdown(button_label, unsafe_allow_html=True)


def create_category_filter():
    """Create category filter for tools"""
    st.sidebar.markdown("### 🎯 Filter by Category")
    
    categories = ["All", "Financial", "Processing", "Operations", "Monitoring"]
    selected_category = st.sidebar.selectbox("Select Category:", categories)
    
    return selected_category.lower() if selected_category != "All" else None

def show_tool_stats():
    """Display statistics about available tools"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🔗 External Tools", "2", "Connected")
    with col2:
        st.metric("🏠 Internal Tools", "8", "Available")
    with col3:
        st.metric("📊 Total Categories", "5", "Organized")