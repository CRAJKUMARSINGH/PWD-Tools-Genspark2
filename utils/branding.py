import streamlit as st


def apply_custom_css():
    st.markdown(
        """
        <style>
        :root {
          --primary-green: #2E8B57;
          --primary-green-dark: #228B22;
          --primary-green-alt: #3CB371;
        }
        .pwd-card {
          background: #ffffff;
          border: 2px solid var(--primary-green);
          border-radius: 15px;
          padding: 16px;
        }
        .pwd-card:hover {
          border-color: var(--primary-green-dark);
          background: #f0f8f5;
        }
        .pwd-badge {
          display: inline-block;
          padding: 4px 10px;
          border-radius: 10px;
          background: #f0f8f5;
          color: var(--primary-green);
          font-weight: 700;
          font-size: 12px;
        }
        .pwd-header {
          background: linear-gradient(180deg, #1a5d38 0%, var(--primary-green) 100%);
          color: #fff;
          border-radius: 12px;
          padding: 16px 20px;
          margin-bottom: 10px;
          text-align: center;
        }
        .pwd-welcome {
          background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%);
          border-radius: 15px;
          padding: 20px;
          text-align: center;
        }
        .pwd-footer {
          background: var(--primary-green);
          color: #fff;
          border-radius: 12px;
          padding: 12px 16px;
          margin-top: 20px;
        }
        .btn-link {
          display: inline-block;
          background: var(--primary-green);
          color: #fff !important;
          padding: 10px 14px;
          border-radius: 10px;
          font-weight: 700;
          text-decoration: none;
        }
        .btn-link:hover {
          background: var(--primary-green-dark);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_header():
    st.markdown(
        """
        <div class="pwd-header">
          <h2 style="margin: 0 0 6px 0;">🏗️ PWD Tools Hub</h2>
          <div style="opacity: .95">Infrastructure Management Suite</div>
          <div style="opacity: .8; font-size: 12px; margin-top: 6px;">Empowering Public Works Department with digital tools for efficient infrastructure management</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_credits():
    st.markdown(
        """
        <div class="pwd-footer">
          <div style="text-align: center; font-weight: 700;">🏆 Initiative Credit</div>
          <div style="text-align: center; margin-top: 4px;">Mrs. Premlata Jain</div>
          <div style="text-align: center; opacity: .9; font-size: 12px;">Additional Administrative Officer, PWD Udaipur</div>
          <div style="text-align: center; opacity: .8; font-size: 11px; margin-top: 4px;">Version 2.0 | Last Updated: September 2025</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_balloons():
    try:
        st.balloons()
    except Exception:
        pass

