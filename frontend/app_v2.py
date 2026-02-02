import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_by_category_tab
from analytics_by_month import analytics_by_month_tab
from analytics_by_day_of_week import analytics_by_day_of_week_tab
from expenses_by_note import expenses_by_note_tab

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Spend Sensei - Expense Management System",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# Custom CSS for modern finance-themed styling
# -------------------------------------------------
custom_css = """
<style>
    /* Main background and text colors */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
    }

    /* Title styling */
    .title-container {
        text-align: center;
        padding: 1rem 0 0.5rem 0;
    }

    .main-title {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: #f8fafc !important;
        margin-bottom: 0.3rem !important;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 1rem;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(30, 41, 59, 0.6);
        padding: 10px 15px 0 15px;
        border-radius: 15px 15px 0 0;
        border-bottom: 2px solid #334155;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: #94a3b8;
        border-radius: 10px 10px 0 0;
        padding: 12px 24px;
        font-weight: 500;
        transition: all 0.3s ease;
        border: none;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(51, 65, 85, 0.5);
        color: #e2e8f0;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #10b981, #059669) !important;
        color: white !important;
        font-weight: 600 !important;
    }

    /* Tab panel background */
    .stTabs [data-baseweb="tab-panel"] {
        background-color: rgba(30, 41, 59, 0.4);
        border-radius: 0 0 15px 15px;
        padding: 20px;
        border: 1px solid rgba(51, 65, 85, 0.5);
        border-top: none;
    }

    /* Hide default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #1e293b;
    }

    ::-webkit-scrollbar-thumb {
        background: #475569;
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #64748b;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------------------------------
# Header Section with Branding
# -------------------------------------------------
st.markdown("""
<div class="title-container">
    <h1 class="main-title">💰 Spend Sensei</h1>
    <p class="subtitle">Master Your Money with Smart Expense Management</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #334155; margin: 1rem 0;'>", unsafe_allow_html=True)

# -------------------------------------------------
# Define 5 tabs with icons - preserving original functionality
# -------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📝 Add/Update",
    "📊 Analytics by Category",
    "📅 Analytics by Month",
    "📆 Analytics by Day of Week",
    "🔍 Expenses by Note"
])

# -------------------------------------------------
# Tab Contents - All original function calls preserved
# -------------------------------------------------
with tab1:
    add_update_tab()

with tab2:
    analytics_by_category_tab()

with tab3:
    analytics_by_month_tab()

with tab4:
    analytics_by_day_of_week_tab()

with tab5:
    expenses_by_note_tab()
