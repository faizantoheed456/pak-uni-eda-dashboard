import streamlit as st
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="EDA of Pakistan Universities",
    page_icon="🎓",
    layout="wide"
)

# --- ADVANCED HIGH-CONTRAST DARK THEME STYLING ---
st.markdown(
    """
    <style>
    /* Dark Theme Workspace Base */
    .stApp {
        background-color: #1A1D24;
    }
    
    /* Global Typography Controls - Ensuring No Accidental Bleeding */
    p, span, label {
        color: #E2E8F0 !important;
    }
    
    /* Clean Sidebar Separation */
    section[data-testid="stSidebar"] {
        background-color: #111318 !important;
        border-right: 1px solid #2D3139;
    }
    
    /* Heading Level Overrides */
    .custom-main-title {
        color: #4FD1C5 !important;
        font-weight: 700;
        text-align: center;
        margin-bottom: 30px;
    }
    .custom-section-title {
        color: #4FD1C5 !important;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    /* FORCED CONTRAST METRIC CARD FIXED RULES */
    div[data-testid="stMetricLabel"] > div {
        color: #4FD1C5 !important;  /* Labels forced to Mint Green */
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    div[data-testid="stMetricValue"] > div {
        color: #FFFFFF !important;  /* Main metric values forced to PURE WHITE */
        font-weight: 700 !important;
        font-size: 2rem !important;
    }

    /* Structured Panel Container for Insights */
    .insight-box {
        background-color: #222630;
        border: 1px solid #2D3139;
        border-radius: 8px;
        padding: 20px;
    }
    .insight-line {
        margin: 10px 0;
        font-size: 1rem;
        color: #E2E8F0 !important;
    }
    .insight-label {
        color: #4FD1C5 !important;
        font-weight: 600;
    }
    .insight-value {
        font-family: monospace;
        background-color: #1A1D24;
        padding: 3px 8px;
        border-radius: 4px;
        color: #FFFFFF !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SECURE DATA LOADING ---
@st.cache_data
def load_data():
    return pd.read_csv('pakistan_universities_dataset.csv')

try:
    uni_data = load_data()

    # --- SIDEBAR INTERFACE ---
    with st.sidebar:
        st.markdown("<h2 style='color: #4FD1C5; font-weight: 600; margin-bottom: 20px;'>Analytics Hub</h2>", unsafe_allow_html=True)
        app_mode = st.selectbox(
            "Select Pipeline Phase:",
            ["Welcome Panel", "Loading and Inspection"],
            label_visibility="collapsed"
        )

    # --- MAIN VIEW DISPLAY ---
    if app_mode == "Welcome Panel":
        st.markdown(
            """
            <div style='text-align: center; margin-top: 12%; padding: 0 10%;'>
                <h1 style='color: #4FD1C5; font-size: 2.8rem; font-weight: 700;'>
                    Pakistan Universities Dataset Analyzer
                </h1>
                <p style='color: #94A3B8; font-size: 1.15rem; margin-bottom: 30px;'>
                    An automated system for processing structural parameters, capacity metrics, and longitudinal tracking data.
                </p>
                <div style='background-color: #222630; padding: 15px 25px; display: inline-block; border-radius: 30px; border: 1px solid #2D3139; color: #4FD1C5;'>
                    💡 Open the sidebar and select <b>Loading and Inspection</b> to run the pipeline analysis.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif app_mode == "Loading and Inspection":
        st.markdown("<h1 class='custom-main-title'>🔍 Dataset Loading & Inspection Pipeline</h1>", unsafe_allow_html=True)

        # 1. First 10 Rows
        st.markdown("<h3 class='custom-section-title'>1. Initial Dataset Slice (First 10 Rows)</h3>", unsafe_allow_html=True)
        st.dataframe(uni_data.head(10), use_container_width=True)

        # 2. Structural Matrix Dimensions (Fully Targeted Explicit Contrast Colors)
        st.markdown("<h3 class='custom-section-title'>2. Structural Matrix Dimensions</h3>", unsafe_allow_html=True)
        
        num_cols = uni_data.select_dtypes(include=['number']).shape[1]
        obj_cols = uni_data.select_dtypes(include=['object']).shape[1]

        grid1, grid2, grid3, grid4 = st.columns(4)
        grid1.metric(label="Total Dataset Rows", value=f"{uni_data.shape[0]:,}")
        grid2.metric(label="Total Feature Columns", value=f"{uni_data.shape[1]}")
        grid3.metric(label="Numerical Features", value=f"{num_cols}")
        grid4.metric(label="Categorical Features", value=f"{obj_cols}")
        
        st.markdown("<br>", unsafe_allow_html=True)

        # 3. Column Data Types
        st.markdown("<h3 class='custom-section-title'>3. Features & Data Type Layout</h3>", unsafe_allow_html=True)
        dtype_df = pd.DataFrame(uni_data.dtypes, columns=['Data Type']).reset_index().rename(columns={'index': 'Column Name'})
        st.dataframe(dtype_df, use_container_width=True, height=280)

        # 4. Concise Summary Dataframe
        st.markdown("<h3 class='custom-section-title'>4. Completeness & Structural Profile</h3>", unsafe_allow_html=True)
        info_df = pd.DataFrame({
            'Column Name': uni_data.columns,
            'Populated Rows': uni_data.notnull().sum().values,
            'Missing Rows': uni_data.isnull().sum().values,
            'Data Type': uni_data.dtypes.values
        }).reset_index(drop=True)
        st.dataframe(info_df, use_container_width=True, height=300)

        # 5. Descriptive Statistics
        st.markdown("<h3 class='custom-section-title'>5. Descriptive Statistical Distributions</h3>", unsafe_allow_html=True)
        st.dataframe(uni_data.describe(), use_container_width=True)

        # 6. Mean of total_enrollment
        st.markdown("<h3 class='custom-section-title'>6. Core Enrollment Metric</h3>", unsafe_allow_html=True)
        st.metric(label="Mean Total Enrollment (All Pakistan)", value=f"{uni_data['Total_Enrollment'].mean():,.2f}")
        st.markdown("<br>", unsafe_allow_html=True)

        # 7. Last 15 Rows
        st.markdown("<h3 class='custom-section-title'>7. Terminal Dataset Slice (Last 15 Rows)</h3>", unsafe_allow_html=True)
        st.dataframe(uni_data.tail(15), use_container_width=True)

        # --- EXTENDED INSIGHTS ---
        st.markdown("<h3 class='custom-section-title'>💡 High-Fidelity Extended Structural Insights</h3>", unsafe_allow_html=True)
        
        null_cols_list = list(uni_data.columns[uni_data.isnull().any()])
        most_unique_col = uni_data.nunique().idxmax()
        mem_usage_mb = uni_data.memory_usage(deep=True).sum() / (1024**2)
        idx_range = f"RangeIndex(start={uni_data.index.start}, stop={uni_data.index.stop}, step={uni_data.index.step})"

        st.markdown(
            f"""
            <div class='insight-box'>
                <div class='insight-line'><span class='insight-label'>• Memory Footprint:</span> Dataset consumes exactly <span class='insight-value'>{mem_usage_mb:.2f} MB</span> inside environment memory pool.</div>
                <div class='insight-line'><span class='insight-label'>• Dataframe Index Allocation:</span> System index range parsed as <span class='insight-value'>{idx_range}</span> with data type <span class='insight-value'>{uni_data.index.dtype}</span>.</div>
                <div class='insight-line'><span class='insight-label'>• Maximum Value Diversity:</span> Element containing the absolute highest specific unique cardinality variation is <span class='insight-value'>'{most_unique_col}'</span>.</div>
                <div class='insight-line'><span class='insight-label'>• Null Feature Detections:</span> Incomplete missing entry metrics observed within <span class='insight-value'>{len(null_cols_list)}</span> feature columns.</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Display list of null features neatly as a clean sub-component table
        null_summary_df = pd.DataFrame({
            'Columns with Missing Values': null_cols_list,
            'Missing Value Count': [uni_data[c].isnull().sum() for c in null_cols_list]
        })
        st.dataframe(null_summary_df, use_container_width=True, height=200)

        st.markdown("<br><b>First 3 rows and trailing 3 columns matrix slice:</b>", unsafe_allow_html=True)
        st.dataframe(uni_data.iloc[:3, -3:], use_container_width=True)

except FileNotFoundError:
    st.error("❌ Resource Error: Missing 'pakistan_universities_dataset.csv'. Verify your current environment pathway.")