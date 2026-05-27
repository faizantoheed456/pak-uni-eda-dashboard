import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
 
# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Pakistani Universities EDA",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Pakistani Universities EDA",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── FIX STREAMLIT TOP WHITE STRIP ───────────────────────────────────────────
st.markdown("""
<style>

/* Remove top padding */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}

/* Remove Streamlit header white bar */
header[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
    height: 0rem;
}

/* Remove top decoration line */
[data-testid="stDecoration"] {
    display: none;
}

/* Adjust toolbar position */
[data-testid="stToolbar"] {
    right: 1rem;
}

/* Remove extra gap above app */
main > div {
    padding-top: 0rem !important;
}

</style>
""", unsafe_allow_html=True)
 
# ── Custom CSS — white + blue theme ────────────────────────────────────────
st.markdown("""
<style>
/* ── Global ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #ffffff !important;
    font-family: 'Segoe UI', sans-serif;
    color: #1a1a1a;
}
 
/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a3c6e 0%, #1e56a0 50%, #2980b9 100%) !important;
    color: #fff !important;
}
[data-testid="stSidebar"] * { color: #fff !important; }
[data-testid="stSidebar"] .stRadio label { color: #fff !important; font-weight: 500; }
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.4) !important; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 { color: #fff !important; }
[data-testid="stSidebar"] .sidebar-section-label {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    opacity: 0.75;
    margin-top: 1.2rem;
    margin-bottom: 0.2rem;
    font-weight: 700;
}
 
/* ── Main title block ── */
.hero {
    background: linear-gradient(135deg, #1a3c6e, #2980b9);
    border-radius: 16px;
    padding: 2.5rem 2rem 2rem 2rem;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 6px 24px rgba(26,60,110,0.20);
}
.hero h1 { color: #fff !important; font-size: 2.4rem; margin: 0; font-weight: 800; }
.hero p  { color: rgba(255,255,255,0.88); font-size: 1.05rem; margin-top: 0.5rem; }
 
/* ── Section headings ── */
.section-title {
    font-size: 1.55rem;
    font-weight: 700;
    color: #1a3c6e;
    border-left: 5px solid #1a3c6e;
    padding-left: 0.75rem;
    margin-bottom: 1.25rem;
}
.sub-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #1e56a0;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
}
 
/* ── Metric cards ── */
.metric-row { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
.metric-card {
    flex: 1; min-width: 160px;
    background: #f0f5ff;
    border: 1px solid #b3cde8;
    border-top: 4px solid #1a3c6e;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(255,107,0,0.08);
}
.metric-card .val { font-size: 1.9rem; font-weight: 800; color: #1a3c6e; }
.metric-card .lbl { font-size: 0.78rem; color: #888; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 0.2rem; }
 
/* ── Info boxes ── */
.info-box {
    background: #f0f5ff;
    border: 1px solid #b3cde8;
    border-radius: 10px;
    padding: 1rem 1.3rem;
    margin-bottom: 1rem;
    font-size: 0.95rem;
    line-height: 1.65;
    color: #2a2a2a;
}
.code-block {
    background: #1e1e1e;
    color: #f8f8f2;
    border-radius: 10px;
    padding: 1.1rem 1.4rem;
    font-family: 'Courier New', monospace;
    font-size: 0.84rem;
    line-height: 1.6;
    margin-bottom: 1rem;
    overflow-x: auto;
    white-space: pre;
}
.keyword   { color: #ff79c6; }
.funcname  { color: #50fa7b; }
.string    { color: #f1fa8c; }
.comment   { color: #6272a4; }
.builtin   { color: #8be9fd; }
 
/* ── Badge ── */
.badge {
    display: inline-block;
    background: #1a3c6e;
    color: #fff;
    border-radius: 6px;
    padding: 0.15rem 0.55rem;
    font-size: 0.72rem;
    font-weight: 700;
    margin-right: 0.3rem;
    margin-bottom: 0.3rem;
    letter-spacing: 0.04em;
}
.badge-grey {
    background: #e8e8e8; color: #555;
}
 
/* ── Dataframe ── */
.stDataFrame { border-radius: 10px; overflow: hidden; }
 
/* ── Expander ── */
details { border: 1px solid #b3cde8 !important; border-radius: 10px !important; }
summary { color: #1a3c6e !important; font-weight: 600 !important; }
 
/* ── Divider ── */
.orange-divider {
    border: none;
    border-top: 2px solid #b3cde8;
    margin: 1.5rem 0;
}
 
/* ── Step list ── */
.step { display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 1rem; }
.step-num {
    min-width: 32px; height: 32px; border-radius: 50%;
    background: #1a3c6e; color: #fff;
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 0.9rem; flex-shrink: 0;
}
.step-body { font-size: 0.93rem; color: #2a2a2a; line-height: 1.6; padding-top: 4px; }
.step-body strong { color: #1e56a0; }
</style>
""", unsafe_allow_html=True)
 
# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_raw():
    return pd.read_csv("pakistan_universities_dataset.csv")
 
@st.cache_data
def load_clean():
    return pd.read_csv("pakistan_universities_dataset_clean.csv")

@st.cache_data
def load_enhanced():
    return pd.read_csv("pakistan_universities_dataset_enhanced.csv")

raw_df      = load_raw()
clean_df    = load_clean()
enhanced_df = load_enhanced()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎓 EDA Dashboard")
    st.markdown("**Pakistani Universities**")
    st.markdown("---")

    st.markdown('<div class="sidebar-section-label">Navigate</div>', unsafe_allow_html=True)
    page = st.radio(
        "",
        ["🏠  Home", "📂  Dataset Viewer", "🔍  Inspection", "🧹  Cleaning",
         "📊  Grouping & Aggregations", "⚙️  Feature Engineering", "📈  Visualizations"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown('<div class="sidebar-section-label">Dataset Info</div>', unsafe_allow_html=True)
    st.markdown(f"**Raw rows:** {raw_df.shape[0]:,}")
    st.markdown(f"**Raw cols:** {raw_df.shape[1]}")
    st.markdown(f"**Clean cols:** {clean_df.shape[1]}")
    st.markdown(f"**Enhanced cols:** {enhanced_df.shape[1]}")
    st.markdown(f"**Universities:** {raw_df['UNI_Name'].nunique()}")
    st.markdown(f"**Provinces:** {raw_df['Province'].nunique()}")
 
# ══════════════════════════════════════════════════════════════════════════════
# PAGE: HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "🏠  Home":
    st.markdown("""
    <div class="hero">
        <h1>🎓 EDA of Pakistani Universities</h1>
        <p>An interactive exploration of higher education landscape across Pakistan —<br>
        covering enrollment, faculty, research, and institutional quality.</p>
    </div>
    """, unsafe_allow_html=True)
 
    # ── KPI row ──
    total_unis   = raw_df["UNI_Name"].nunique()
    total_enroll = int(raw_df["Total_Enrollment"].sum())
    avg_cgpa     = raw_df["Avg_CGPA"].mean()
    total_papers = int(raw_df["Research_Papers_Published"].sum())
 
    st.markdown(f"""
    <div class="metric-row">
        <div class="metric-card"><div class="val">{total_unis}</div><div class="lbl">Universities</div></div>
        <div class="metric-card"><div class="val">{total_enroll:,}</div><div class="lbl">Total Enrollments</div></div>
        <div class="metric-card"><div class="val">{avg_cgpa:.2f}</div><div class="lbl">Avg CGPA</div></div>
        <div class="metric-card"><div class="val">{total_papers:,}</div><div class="lbl">Research Papers</div></div>
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<hr class="orange-divider">', unsafe_allow_html=True)
 
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="sub-title">📌 Project Overview</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="info-box">
        This project performs a comprehensive <strong>Exploratory Data Analysis (EDA)</strong>
        on a dataset of Pakistani universities. The pipeline covers:<br><br>
        • <strong>Loading & Inspection</strong> — shape, dtypes, nulls, memory, statistics<br>
        • <strong>Data Cleaning</strong> — disguised nulls, imputation strategies, type optimisation<br>
        • <strong>Interactive Viewer</strong> — explore raw and cleaned datasets side-by-side
        </div>
        """, unsafe_allow_html=True)
 
    with col2:
        st.markdown('<div class="sub-title">🗂 Dataset Columns</div>', unsafe_allow_html=True)
        col_types = raw_df.dtypes.reset_index()
        col_types.columns = ["Column", "Type"]
        badges = ""
        for _, row in col_types.iterrows():
            cls = "badge" if str(row["Type"]) in ("float64","int64","int32","float32") else "badge badge-grey"
            badges += f'<span class="{cls}">{row["Column"]}</span>'
        st.markdown(f'<div class="info-box">{badges}</div>', unsafe_allow_html=True)
 
    st.markdown('<hr class="orange-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">📊 Quick Data Snapshot (Raw)</div>', unsafe_allow_html=True)
    st.dataframe(raw_df.head(10), use_container_width=True)
 
 
# ══════════════════════════════════════════════════════════════════════════════
# PAGE: DATASET VIEWER
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📂  Dataset Viewer":
    st.markdown('<div class="section-title">📂 Dataset Viewer</div>', unsafe_allow_html=True)
 
    tab_raw, tab_clean, tab_compare = st.tabs(["🗄 Raw Dataset", "✅ Cleaned Dataset", "🔁 Compare"])
 
    with tab_raw:
        st.markdown('<div class="sub-title">Raw Dataset</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="metric-row">
            <div class="metric-card"><div class="val">{raw_df.shape[0]:,}</div><div class="lbl">Rows</div></div>
            <div class="metric-card"><div class="val">{raw_df.shape[1]}</div><div class="lbl">Columns</div></div>
            <div class="metric-card"><div class="val">{int(raw_df.isnull().sum().sum()):,}</div><div class="lbl">Missing Values</div></div>
        </div>""", unsafe_allow_html=True)
 
        # Filter row
        c1, c2, c3 = st.columns([2,2,1])
        with c1:
            province_opts = ["All"] + sorted(raw_df["Province"].dropna().unique().tolist())
            sel_prov = st.selectbox("Filter by Province", province_opts, key="rv_prov")
        with c2:
            type_opts = ["All"] + sorted(raw_df["Type"].dropna().unique().tolist())
            sel_type = st.selectbox("Filter by Type", type_opts, key="rv_type")
        with c3:
            n_rows = st.number_input("Rows to show", 5, 500, 20, key="rv_rows")
 
        filtered = raw_df.copy()
        if sel_prov != "All": filtered = filtered[filtered["Province"] == sel_prov]
        if sel_type != "All": filtered = filtered[filtered["Type"] == sel_type]
        st.dataframe(filtered.head(n_rows), use_container_width=True)
        st.caption(f"Showing {min(n_rows, len(filtered))} of {len(filtered):,} filtered rows")
 
    with tab_clean:
        st.markdown('<div class="sub-title">Cleaned Dataset</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="metric-row">
            <div class="metric-card"><div class="val">{clean_df.shape[0]:,}</div><div class="lbl">Rows</div></div>
            <div class="metric-card"><div class="val">{clean_df.shape[1]}</div><div class="lbl">Columns</div></div>
            <div class="metric-card"><div class="val">{int(clean_df.isnull().sum().sum()):,}</div><div class="lbl">Missing Values</div></div>
        </div>""", unsafe_allow_html=True)
 
        col_sel = st.multiselect("Select columns to display", clean_df.columns.tolist(),
                                  default=clean_df.columns[:10].tolist(), key="cv_cols")
        n_c = st.slider("Rows to show", 5, 100, 20, key="cv_rows")
        if col_sel:
            st.dataframe(clean_df[col_sel].head(n_c), use_container_width=True)
 
    with tab_compare:
        st.markdown('<div class="sub-title">Raw vs Cleaned Comparison</div>', unsafe_allow_html=True)
        comp_col = st.selectbox("Select column to compare",
                                 [c for c in raw_df.columns if c in clean_df.columns])
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Raw**")
            st.write(raw_df[comp_col].describe())
            st.markdown(f"Missing: **{raw_df[comp_col].isnull().sum()}**")
        with c2:
            st.markdown("**Cleaned**")
            st.write(clean_df[comp_col].describe() if comp_col in clean_df.columns else "N/A")
            st.markdown(f"Missing: **{clean_df[comp_col].isnull().sum() if comp_col in clean_df.columns else 'N/A'}**")
 
 
# ══════════════════════════════════════════════════════════════════════════════
# PAGE: INSPECTION
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🔍  Inspection":
    st.markdown('<div class="section-title">🔍 Loading & Inspection</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
    The inspection phase answers 15 structured questions about the dataset —
    from basic shape to memory footprint, column uniqueness, and null coverage.
    </div>
    """, unsafe_allow_html=True)
 
    # Step 1 — Head
    with st.expander("1️⃣  First 10 Rows", expanded=True):
        st.dataframe(raw_df.head(10), use_container_width=True)
 
    # Step 2 — Shape
    with st.expander("2️⃣  Dataset Shape"):
        st.markdown(f"""
        <div class="metric-row">
            <div class="metric-card"><div class="val">{raw_df.shape[0]:,}</div><div class="lbl">Rows</div></div>
            <div class="metric-card"><div class="val">{raw_df.shape[1]}</div><div class="lbl">Columns</div></div>
        </div>""", unsafe_allow_html=True)
 
    # Step 3 — dtypes
    with st.expander("3️⃣  Columns with Data Types"):
        dtype_df = pd.DataFrame(raw_df.dtypes, columns=["dtype"]).reset_index()
        dtype_df.columns = ["Column", "Data Type"]
        dtype_df["Data Type"] = dtype_df["Data Type"].astype(str)
        st.dataframe(dtype_df, use_container_width=True, height=300)
 
    # Step 4 — Info summary
    with st.expander("4️⃣  Concise Summary (.info() equivalent)"):
        info_data = pd.DataFrame({
            "Column": raw_df.columns,
            "Non-Null Count": raw_df.notnull().sum().values,
            "Null Count": raw_df.isnull().sum().values,
            "Dtype": raw_df.dtypes.astype(str).values,
        })
        st.dataframe(info_data, use_container_width=True)
 
    # Step 5 — Describe
    with st.expander("5️⃣  Statistical Summary (.describe())"):
        st.dataframe(raw_df.describe().T.style.format("{:.2f}"), use_container_width=True)
 
    # Step 6 — Mean enrollment
    with st.expander("6️⃣  Mean Total Enrollment"):
        mean_enroll = raw_df["Total_Enrollment"].mean()
        st.markdown(f"""
        <div class="metric-card" style="max-width:280px">
            <div class="val">{mean_enroll:,.2f}</div>
            <div class="lbl">Mean Total Enrollment across all Pakistani universities</div>
        </div>""", unsafe_allow_html=True)
 
    # Step 7 — Tail
    with st.expander("7️⃣  Last 15 Rows"):
        st.dataframe(raw_df.tail(15), use_container_width=True)
 
    # Step 8 — Column names
    with st.expander("8️⃣  All Column Names"):
        cols_list = raw_df.columns.tolist()
        badges = "".join([f'<span class="badge">{c}</span>' for c in cols_list])
        st.markdown(f'<div class="info-box">{badges}</div>', unsafe_allow_html=True)
 
    # Step 9 — Random sample
    with st.expander("9️⃣  10 Random Rows (seed=42)"):
        st.dataframe(raw_df.sample(10, random_state=42), use_container_width=True)
 
    # Step 10 — Numeric vs object
    with st.expander("🔟  Numeric vs Non-Numeric Column Count"):
        num_cols   = raw_df.select_dtypes(include=["int64","float64"]).shape[1]
        obj_cols   = raw_df.select_dtypes(include=["object"]).shape[1]
        st.markdown(f"""
        <div class="metric-row">
            <div class="metric-card"><div class="val">{num_cols}</div><div class="lbl">Numeric Columns</div></div>
            <div class="metric-card"><div class="val">{obj_cols}</div><div class="lbl">Non-Numeric Columns</div></div>
        </div>""", unsafe_allow_html=True)
 
    # Step 11 — Null columns
    with st.expander("1️⃣1️⃣  Columns with Null Values"):
        null_cols = raw_df.columns[raw_df.isna().any()].tolist()
        null_counts = raw_df[null_cols].isnull().sum().reset_index()
        null_counts.columns = ["Column", "Null Count"]
        null_counts["Null %"] = (null_counts["Null Count"] / len(raw_df) * 100).round(2)
        st.dataframe(null_counts, use_container_width=True)
 
    # Step 12 — Memory
    with st.expander("1️⃣2️⃣  Memory Usage"):
        mem_mb = raw_df.memory_usage(deep=True).sum() / (1024**2)
        st.markdown(f"""
        <div class="metric-card" style="max-width:240px">
            <div class="val">{mem_mb:.4f} MB</div>
            <div class="lbl">Memory Usage (deep=True)</div>
        </div>""", unsafe_allow_html=True)
        col_mem = raw_df.memory_usage(deep=True).reset_index()
        col_mem.columns = ["Column", "Bytes"]
        col_mem = col_mem[col_mem["Column"] != "Index"]
        st.dataframe(col_mem.sort_values("Bytes", ascending=False), use_container_width=True)
 
    # Step 13 — Most unique
    with st.expander("1️⃣3️⃣  Column with Most Unique Values"):
        most_unique = raw_df.nunique().sort_values(ascending=False)
        most_col = most_unique.index[0]
        st.markdown(f"""
        <div class="info-box">
        The column with the most unique values is <strong style="color:#1a3c6e">{most_col}</strong>
        with <strong style="color:#1a3c6e">{most_unique.iloc[0]:,}</strong> unique values.
        </div>""", unsafe_allow_html=True)
        uniq_df = most_unique.reset_index()
        uniq_df.columns = ["Column", "Unique Values"]
        st.dataframe(uniq_df, use_container_width=True, height=280)
 
    # Step 14 — First 3 rows last 3 cols
    with st.expander("1️⃣4️⃣  First 3 Rows × Last 3 Columns"):
        st.dataframe(raw_df.iloc[:3, -3:], use_container_width=True)
 
    # Step 15 — Index range
    with st.expander("1️⃣5️⃣  DataFrame Index Range & Type"):
        idx = raw_df.index
        st.markdown(f"""
        <div class="info-box">
        <strong>Range:</strong> {idx.min()} → {idx.max()} &nbsp;|&nbsp;
        <strong>Length:</strong> {len(idx):,} &nbsp;|&nbsp;
        <strong>Dtype:</strong> {idx.dtype}
        </div>""", unsafe_allow_html=True)
 
 
 
 
# ══════════════════════════════════════════════════════════════════════════════
# PAGE: CLEANING
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🧹  Cleaning":
    st.markdown('<div class="section-title">🧹 Data Cleaning Pipeline</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
    An advanced 8-step cleaning pipeline designed for the Pakistan Universities Dataset.
    Every imputation is logged via boolean flag columns. The pipeline resolves regional
    urban biases, cleans categorical quirks, and optimizes memory formats.
    </div>
    """, unsafe_allow_html=True)
 
    # ── Before/After metrics ──
    missing_before = int(raw_df.isnull().sum().sum())
    missing_after  = int(clean_df[raw_df.columns].isnull().sum().sum())
    flag_cols      = [c for c in clean_df.columns if c.endswith("_is_imputed")]
 
    st.markdown(f"""
    <div class="metric-row">
        <div class="metric-card"><div class="val">{missing_before:,}</div><div class="lbl">Missing Before</div></div>
        <div class="metric-card"><div class="val">{missing_after:,}</div><div class="lbl">Missing After</div></div>
        <div class="metric-card"><div class="val">{len(flag_cols)}</div><div class="lbl">Imputation Flags</div></div>
        <div class="metric-card"><div class="val">{clean_df.shape[1] - raw_df.shape[1]}</div><div class="lbl">New Columns Added</div></div>
    </div>""", unsafe_allow_html=True)
 
    st.markdown('<hr class="orange-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">🔧 Pipeline Steps</div>', unsafe_allow_html=True)
 
    steps = [
        ("Handle Disguised Missing Values",
         "Replaced <code>'N/A'</code>, <code>'na'</code>, <code>'unknown'</code>, and empty strings with <code>pd.NA</code> to ensure uniform null representation."),
        ("Create Imputation Flag Columns",
         "For each of the 16 target columns, a boolean flag column (<code>col_is_imputed</code>) was added before any filling — creating an audit trail of every imputation."),
        ("Clean HEC_Ranking",
         "Stripped <code>.0</code> decimal suffixes, coerced to integer, and mapped zero/missing values to the string <code>'None'</code>."),
        ("Numeric Imputation via University-Specific Medians",
         "9 numeric columns (fees, labs, CGPA, etc.) were filled with per-university medians first; remaining NaNs fell back to global column medians."),
        ("Logical Enrollment Reconstruction",
         "<code>BS_Students</code>, <code>PhD_Students</code>, and <code>MS_MPhil_Students</code> were recalculated from <code>Total_Enrollment</code> using arithmetic constraints — preserving internal consistency."),
        ("Categorical Imputation via Regional Mode",
         "<code>Avg_Student_Background</code> was imputed using province-level mode to reduce urban bias. Entry test fields were conditionally filled based on whether a test is required."),
        ("Whitespace Cleaning",
         "All object-type columns were stripped of leading/trailing whitespace using <code>.str.strip()</code>."),
        ("Type Optimisation",
         "Numeric columns were downcast to smaller int/float types. 12 categorical text columns were cast to <code>category</code> dtype — reducing memory footprint significantly."),
    ]
 
    for i, (title, desc) in enumerate(steps, 1):
        with st.expander(f"Step {i}: {title}"):
            st.markdown(f'<div class="info-box">{desc}</div>', unsafe_allow_html=True)
 
    # ── Imputation flag explorer ──
    st.markdown('<hr class="orange-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">🏷 Imputation Flag Explorer</div>', unsafe_allow_html=True)
    if flag_cols:
        flag_summary = pd.DataFrame({
            "Column": flag_cols,
            "Imputed Rows": [clean_df[c].sum() for c in flag_cols],
            "Imputed %": [(clean_df[c].sum() / len(clean_df) * 100).round(2) for c in flag_cols],
        })
        flag_summary["Original Column"] = flag_summary["Column"].str.replace("_is_imputed","")
        flag_summary = flag_summary[["Original Column","Imputed Rows","Imputed %"]]
        flag_summary = flag_summary.sort_values("Imputed Rows", ascending=False)
        st.dataframe(flag_summary, use_container_width=True)
    else:
        st.info("Flag columns not found in the cleaned dataset.")
 
    # ── Cleaned data preview ──
    st.markdown('<hr class="orange-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">✅ Cleaned Dataset Preview</div>', unsafe_allow_html=True)
    n_preview = st.slider("Rows to preview", 5, 50, 10, key="clean_prev")
    st.dataframe(clean_df.head(n_preview), use_container_width=True)
 
# ══════════════════════════════════════════════════════════════════════════════
# PAGE: GROUPING & AGGREGATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📊  Grouping & Aggregations":
    st.markdown('<div class="section-title">📊 Grouping & Aggregations</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
    10 analytical questions answered on the cleaned dataset — covering HEC rankings,
    provincial patterns, research output, fees, employment, dropout rates, and gender equity.
    </div>
    """, unsafe_allow_html=True)
 
    c_uni_data = clean_df.copy()
 
    # ── Q1 ────────────────────────────────────────────────────────────────────
    with st.expander("Q1 — HEC Category Ranking by Avg CGPA", expanded=True):
        q1 = (
            c_uni_data.groupby("HEC_Category", observed=False)["Avg_CGPA"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )
        q1.columns = ["HEC Category", "Avg CGPA"]
        q1["Avg CGPA"] = q1["Avg CGPA"].round(3)
        st.dataframe(q1, use_container_width=True, hide_index=True)
 
    # ── Q2 ────────────────────────────────────────────────────────────────────
    with st.expander("Q2 — Number of Universities by Province"):
        q2 = (
            c_uni_data.groupby("Province", observed=False)["UNI_Name"]
            .nunique()
            .sort_values(ascending=False)
            .reset_index()
        )
        q2.columns = ["Province", "Universities"]
        st.dataframe(q2, use_container_width=True, hide_index=True)
 
    # ── Q3 ────────────────────────────────────────────────────────────────────
    with st.expander("Q3 — Total Research Papers by Department Category"):
        q3 = (
            c_uni_data.groupby("Department_Category", observed=False)["Research_Papers_Published"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
        q3.columns = ["Department Category", "Total Research Papers"]
        st.dataframe(q3, use_container_width=True, hide_index=True)
 
    # ── Q4 ────────────────────────────────────────────────────────────────────
    with st.expander("Q4 — Median Fee Per Semester by University Type"):
        q4 = (
            c_uni_data.groupby("Type", observed=False)["Fee_Per_Semester_PKR"]
            .median()
            .reset_index()
        )
        q4.columns = ["University Type", "Median Fee (PKR)"]
        q4["Median Fee (PKR)"] = q4["Median Fee (PKR)"].apply(lambda x: f"{x:,.0f}")
        st.dataframe(q4, use_container_width=True, hide_index=True)
 
    # ── Q5 ────────────────────────────────────────────────────────────────────
    with st.expander("Q5 — Top 5 Cities by Avg Employment Ratio (Min 3 Universities)"):
        city_counts = c_uni_data.groupby("City", observed=False)["UNI_Name"].nunique()
        eligible_cities = city_counts[city_counts >= 3].index
        q5 = (
            c_uni_data[c_uni_data["City"].isin(eligible_cities)]
            .groupby("City", observed=False)["Employment_Ratio_Pct"]
            .mean()
            .nlargest(5)
            .reset_index()
        )
        q5.columns = ["City", "Avg Employment Ratio (%)"]
        q5["Avg Employment Ratio (%)"] = q5["Avg Employment Ratio (%)"].round(2)
        st.dataframe(q5, use_container_width=True, hide_index=True)
 
    # ── Q6 ────────────────────────────────────────────────────────────────────
    with st.expander("Q6 — Dropout Rates by Province (Overall & Sector Breakdown)"):
        q6_overall = (
            c_uni_data.groupby("Province", observed=True)["Dropout_Rate_Pct"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )
        q6_overall.columns = ["Province", "Avg Dropout Rate (%)"]
        q6_overall["Avg Dropout Rate (%)"] = q6_overall["Avg Dropout Rate (%)"].round(2)
 
        q6_breakdown = (
            c_uni_data.groupby(["Province", "Type"], observed=True)["Dropout_Rate_Pct"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )
        q6_breakdown.columns = ["Province", "Type", "Avg Dropout Rate (%)"]
        q6_breakdown["Avg Dropout Rate (%)"] = q6_breakdown["Avg Dropout Rate (%)"].round(2)
 
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("**Overall by Province**")
            st.dataframe(q6_overall, use_container_width=True, hide_index=True)
        with col_b:
            st.markdown("**By Province & Type**")
            st.dataframe(q6_breakdown, use_container_width=True, hide_index=True)
 
    # ── Q7 ────────────────────────────────────────────────────────────────────
    with st.expander("Q7 — Avg CGPA & Employment by Entry Test Tier"):
        q7 = (
            c_uni_data.groupby("Entry_Test_Tier", observed=False)[["Avg_CGPA", "Employment_Ratio_Pct"]]
            .mean()
            .round(2)
            .reset_index()
        )
        q7.columns = ["Entry Test Tier", "Avg CGPA", "Avg Employment Ratio (%)"]
        st.dataframe(q7, use_container_width=True, hide_index=True)
        st.markdown("""
        <div class="info-box" style="margin-top:0.75rem">
        📌 Higher entrance difficulty is associated with stronger CGPAs and better employment outcomes.
        </div>
        """, unsafe_allow_html=True)
 
    # ── Q8 ────────────────────────────────────────────────────────────────────
    with st.expander("Q8 — Province × Department Summary (Enrollment > 50,000)"):
        q8 = (
            c_uni_data.groupby(["Province", "Department_Category"], observed=True)
            .agg(
                Total_Enrollment=("Total_Enrollment", "sum"),
                Avg_Student_Faculty_Ratio=("Student_Faculty_Ratio", "mean"),
                Number_of_Departments=("Department_Name", "nunique"),
            )
            .reset_index()
        )
        q8 = q8[q8["Total_Enrollment"] > 50000].copy()
        q8["Avg_Student_Faculty_Ratio"] = q8["Avg_Student_Faculty_Ratio"].round(2)
        q8.columns = ["Province", "Department Category", "Total Enrollment", "Avg S:F Ratio", "# Departments"]
        st.dataframe(q8, use_container_width=True, hide_index=True)
 
    # ── Q9 ────────────────────────────────────────────────────────────────────
    with st.expander("Q9 — Universities Exceeding Provincial Female Share Baseline"):
        uni_level = (
            c_uni_data.groupby(["Province", "UNI_Name"], observed=True)
            .agg(Total_Female=("Female_Enrollment", "sum"), Total_Students=("Total_Enrollment", "sum"))
            .reset_index()
        )
        uni_level["Female_Share"] = uni_level["Total_Female"] / uni_level["Total_Students"]
        uni_level["Provincial_Avg"] = uni_level.groupby("Province", observed=True)["Female_Share"].transform("mean")
        q9 = (
            uni_level[uni_level["Female_Share"] > uni_level["Provincial_Avg"]]
            .groupby("Province", observed=True)["UNI_Name"]
            .nunique()
            .sort_values(ascending=False)
            .reset_index()
        )
        q9.columns = ["Province", "Universities Above Provincial Avg Female Share"]
        st.dataframe(q9, use_container_width=True, hide_index=True)
 
    # ── Q10 ───────────────────────────────────────────────────────────────────
    with st.expander("Q10 — Top Research Department Category per Year"):
        q10 = (
            c_uni_data.groupby(["Year", "Department_Category"], observed=True)["Research_Papers_Published"]
            .mean()
            .reset_index()
            .sort_values("Research_Papers_Published", ascending=False)
            .drop_duplicates(subset=["Year"], keep="first")
            .sort_values("Year")
            .reset_index(drop=True)
        )
        q10.columns = ["Year", "Top Department Category", "Avg Research Papers"]
        q10["Avg Research Papers"] = q10["Avg Research Papers"].round(2)
        st.dataframe(q10, use_container_width=True, hide_index=True)
 
# ══════════════════════════════════════════════════════════════════════════════
# PAGE: FEATURE ENGINEERING
# ══════════════════════════════════════════════════════════════════════════════
elif page == "⚙️  Feature Engineering":
    st.markdown('<div class="section-title">⚙️ Feature Engineering</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
    11 new features engineered from the cleaned dataset — covering gender equity, fees,
    research productivity, campus density, selectivity, institutional scoring, and risk profiling.
    The enhanced dataset has <strong>64 columns</strong> (50 cleaned + 14 engineered).
    </div>
    """, unsafe_allow_html=True)
 
    enh = enhanced_df.copy()
    new_cols = [
        "Female_Share_Pct", "Gender_Balance_Category", "Annual_Fee_PKR", "Fee_Band",
        "Research_Per_Faculty", "Campus_Density", "Is_Overcrowded", "PG_Ratio",
        "Is_Research_Focused", "Selectivity_Score", "University_Score",
        "Fee_Value_Score", "Peer_CGPA_Gap", "Risk_Index",
    ]
 
    # ── KPI row ──
    overcrowded_pct = (enh["Is_Overcrowded"].sum() / len(enh) * 100)
    research_focused_pct = (enh["Is_Research_Focused"].sum() / len(enh) * 100)
    avg_selectivity = enh["Selectivity_Score"].mean()
    avg_risk = enh["Risk_Index"].mean()
 
    st.markdown(f"""
    <div class="metric-row">
        <div class="metric-card"><div class="val">14</div><div class="lbl">New Features</div></div>
        <div class="metric-card"><div class="val">{overcrowded_pct:.1f}%</div><div class="lbl">Overcrowded Campuses</div></div>
        <div class="metric-card"><div class="val">{research_focused_pct:.1f}%</div><div class="lbl">Research Focused</div></div>
        <div class="metric-card"><div class="val">{avg_selectivity:.2f}</div><div class="lbl">Avg Selectivity Score</div></div>
        <div class="metric-card"><div class="val">{avg_risk:.2f}</div><div class="lbl">Avg Risk Index</div></div>
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<hr class="orange-divider">', unsafe_allow_html=True)
 
    # ── Feature 1 & 2: Gender ─────────────────────────────────────────────────
    with st.expander("F1 & F2 — Female Share % & Gender Balance Category", expanded=True):
        st.markdown("""
        <div class="info-box">
        <strong>Female_Share_Pct</strong>: Female enrollment as a % of total enrollment.<br>
        <strong>Gender_Balance_Category</strong>: Binned into <em>Male Dominated</em> (&lt;30%), 
        <em>Balanced</em> (30–60%), or <em>Female Dominated</em> (&gt;60%).
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Distribution by Gender Balance Category**")
            gb = enh["Gender_Balance_Category"].value_counts().reset_index()
            gb.columns = ["Category", "Count"]
            gb["Share %"] = (gb["Count"] / len(enh) * 100).round(1)
            st.dataframe(gb, use_container_width=True, hide_index=True)
        with col2:
            st.markdown("**Female Share % — Summary**")
            st.dataframe(
                enh["Female_Share_Pct"].describe().round(2).reset_index().rename(
                    columns={"index": "Stat", "Female_Share_Pct": "Value"}
                ), use_container_width=True, hide_index=True
            )
 
    # ── Feature 3 & 4: Fee ────────────────────────────────────────────────────
    with st.expander("F3 & F4 — Annual Fee & Fee Band"):
        st.markdown("""
        <div class="info-box">
        <strong>Annual_Fee_PKR</strong>: Semester fee × 2.<br>
        <strong>Fee_Band</strong>: Percentile-based bands — <em>Low</em> (bottom 33%), 
        <em>Mid</em> (33–66%), <em>High</em> (top 33%).
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Fee Band Distribution**")
            fb = enh["Fee_Band"].value_counts().reset_index()
            fb.columns = ["Fee Band", "Count"]
            st.dataframe(fb, use_container_width=True, hide_index=True)
        with col2:
            st.markdown("**Avg Annual Fee by University Type (PKR)**")
            fee_type = enh.groupby("Type", observed=True)["Annual_Fee_PKR"].mean().round(0).reset_index()
            fee_type.columns = ["Type", "Avg Annual Fee (PKR)"]
            fee_type["Avg Annual Fee (PKR)"] = fee_type["Avg Annual Fee (PKR)"].apply(lambda x: f"{x:,.0f}")
            st.dataframe(fee_type, use_container_width=True, hide_index=True)
 
    # ── Feature 5: Research Per Faculty ───────────────────────────────────────
    with st.expander("F5 — Research Productivity Per Faculty"):
        st.markdown("""
        <div class="info-box">
        <strong>Research_Per_Faculty</strong>: Research papers published ÷ faculty count.
        Measures research output efficiency per faculty member.
        </div>
        """, unsafe_allow_html=True)
        rpf = enh.groupby("Province", observed=True)["Research_Per_Faculty"].mean().round(3).sort_values(ascending=False).reset_index()
        rpf.columns = ["Province", "Avg Research Per Faculty"]
        st.dataframe(rpf, use_container_width=True, hide_index=True)
 
    # ── Feature 6 & 7: Campus Density ─────────────────────────────────────────
    with st.expander("F6 & F7 — Campus Density & Overcrowding Flag"):
        st.markdown("""
        <div class="info-box">
        <strong>Campus_Density</strong>: Total enrollment ÷ number of buildings.<br>
        <strong>Is_Overcrowded</strong>: 1 if campus density exceeds 1.5× the national median.
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Overcrowded vs Normal by Province**")
            oc = enh.groupby("Province", observed=True)["Is_Overcrowded"].mean().mul(100).round(1).reset_index()
            oc.columns = ["Province", "Overcrowded %"]
            st.dataframe(oc, use_container_width=True, hide_index=True)
        with col2:
            st.markdown("**Campus Density — Summary**")
            st.dataframe(
                enh["Campus_Density"].describe().round(2).reset_index().rename(
                    columns={"index": "Stat", "Campus_Density": "Value"}
                ), use_container_width=True, hide_index=True
            )
 
    # ── Feature 8 & 9: PG Ratio & Research Focus ──────────────────────────────
    with st.expander("F8 & F9 — PG Ratio & Research Focus Flag"):
        st.markdown("""
        <div class="info-box">
        <strong>PG_Ratio</strong>: % of students enrolled in MS/MPhil or PhD programs.<br>
        <strong>Is_Research_Focused</strong>: 1 if PG Ratio &gt; 30% <em>and</em> research per faculty 
        exceeds the national median — both conditions must hold.
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Avg PG Ratio by HEC Category**")
            pg = enh.groupby("HEC_Category", observed=True)["PG_Ratio"].mean().round(2).sort_values(ascending=False).reset_index()
            pg.columns = ["HEC Category", "Avg PG Ratio (%)"]
            st.dataframe(pg, use_container_width=True, hide_index=True)
        with col2:
            st.markdown("**Research Focused Universities by Province**")
            rf = enh.groupby("Province", observed=True)["Is_Research_Focused"].sum().sort_values(ascending=False).reset_index()
            rf.columns = ["Province", "Research Focused Count"]
            st.dataframe(rf, use_container_width=True, hide_index=True)
 
    # ── Feature 10: Selectivity Score ─────────────────────────────────────────
    with st.expander("F10 — Selectivity Score"):
        st.markdown("""
        <div class="info-box">
        <strong>Selectivity_Score</strong>: Composite of entry test difficulty tier (50%) 
        and normalised average CGPA (50%). Range: 0–3.
        </div>
        """, unsafe_allow_html=True)
        sel = enh.groupby("Entry_Test_Tier", observed=True)["Selectivity_Score"].mean().round(3).sort_values(ascending=False).reset_index()
        sel.columns = ["Entry Test Tier", "Avg Selectivity Score"]
        st.dataframe(sel, use_container_width=True, hide_index=True)
 
    # ── Feature 11: University Score ──────────────────────────────────────────
    with st.expander("F11 — Composite University Score"):
        st.markdown("""
        <div class="info-box">
        <strong>University_Score</strong>: Weighted composite —
        Employment (35%) + Research Per Faculty (25%) + Avg CGPA (25%) + Industry Tie-Ups (15%).
        All metrics normalised to [0, 1] before weighting.
        </div>
        """, unsafe_allow_html=True)
        top_unis = (
            enh.groupby("UNI_Name", observed=True)["University_Score"]
            .mean()
            .round(4)
            .sort_values(ascending=False)
            .head(15)
            .reset_index()
        )
        top_unis.columns = ["University", "Avg University Score"]
        top_unis.index = top_unis.index + 1
        st.markdown("**Top 15 Universities by Score**")
        st.dataframe(top_unis, use_container_width=True)
 
    # ── Feature 12: Fee Value Score ───────────────────────────────────────────
    with st.expander("F12 — Fee Value Score"):
        st.markdown("""
        <div class="info-box">
        <strong>Fee_Value_Score</strong>: Employment ratio ÷ annual fee × 100,000.
        Higher score = more employment outcome per rupee spent.
        </div>
        """, unsafe_allow_html=True)
        fvs = enh.groupby("Type", observed=True)["Fee_Value_Score"].mean().round(4).reset_index()
        fvs.columns = ["University Type", "Avg Fee Value Score"]
        st.dataframe(fvs, use_container_width=True, hide_index=True)
 
    # ── Feature 13: Peer CGPA Gap ─────────────────────────────────────────────
    with st.expander("F13 — Peer CGPA Gap (Regional Tier Benchmarking)"):
        st.markdown("""
        <div class="info-box">
        <strong>Peer_CGPA_Gap</strong>: Each university's avg CGPA minus the mean CGPA 
        of all universities in the same Province × HEC Category group.
        Positive = above peers; negative = below peers.
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Top 10 — Above Their Peers**")
            above = (
                enh.groupby("UNI_Name", observed=True)["Peer_CGPA_Gap"]
                .mean().round(3).sort_values(ascending=False).head(10).reset_index()
            )
            above.columns = ["University", "Peer CGPA Gap"]
            st.dataframe(above, use_container_width=True, hide_index=True)
        with col2:
            st.markdown("**Bottom 10 — Below Their Peers**")
            below = (
                enh.groupby("UNI_Name", observed=True)["Peer_CGPA_Gap"]
                .mean().round(3).sort_values(ascending=True).head(10).reset_index()
            )
            below.columns = ["University", "Peer CGPA Gap"]
            st.dataframe(below, use_container_width=True, hide_index=True)
 
    # ── Feature 14: Risk Index ────────────────────────────────────────────────
    with st.expander("F14 — Institutional Risk Index"):
        st.markdown("""
        <div class="info-box">
        <strong>Risk_Index</strong>: Equal-weighted average of normalised dropout rate, 
        student-faculty ratio, and inverted female share percentage.
        Range: 0 (low risk) → 1 (high risk).
        </div>
        """, unsafe_allow_html=True)
        risk = enh.groupby("Province", observed=True)["Risk_Index"].mean().round(3).sort_values(ascending=False).reset_index()
        risk.columns = ["Province", "Avg Risk Index"]
        st.dataframe(risk, use_container_width=True, hide_index=True)
 
    # ── Enhanced dataset preview ──────────────────────────────────────────────
    st.markdown('<hr class="orange-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">📋 Enhanced Dataset Preview</div>', unsafe_allow_html=True)
    col_opts = st.multiselect(
        "Select columns to display",
        options=enh.columns.tolist(),
        default=["UNI_Name", "Province", "Type"] + new_cols[:6],
        key="fe_cols"
    )
    n_fe = st.slider("Rows to show", 5, 50, 10, key="fe_rows")
    if col_opts:
        st.dataframe(enh[col_opts].head(n_fe), use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: VISUALIZATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📈  Visualizations":
    st.markdown('<div class="section-title">📈 Advanced Visualizations</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    Interactive visual analytics for Pakistani universities dataset —
    exploring enrollment trends, research productivity, fee distributions,
    employment outcomes, and institutional performance across provinces.
    </div>
    """, unsafe_allow_html=True)

    c_uni_data = clean_df.copy()
    enhanced_uni_data = enhanced_df.copy()

    # ── Visualization Art Header ─────────────────────────────────────────────
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1a3c6e, #2980b9);
        border-radius: 18px;
        padding: 2rem;
        margin-bottom: 2rem;
        text-align:center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    ">
        <h1 style="color:white; margin-bottom:0.5rem;">
            🎨 University Intelligence Visualization Hub
        </h1>
        <p style="color:rgba(255,255,255,0.9); font-size:1rem;">
            Transforming educational data into meaningful visual stories
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Chart 1 ──────────────────────────────────────────────────────────────
    st.markdown('<div class="sub-title">🏛 Universities Per Province</div>', unsafe_allow_html=True)

    total_uni_pro = (
        c_uni_data.groupby('Province', observed=False)['UNI_Name']
        .nunique()
        .sort_values(ascending=False)
    )

    fig1 = px.bar(
        total_uni_pro,
        x=total_uni_pro.index,
        y=total_uni_pro.values,
        color=total_uni_pro.index,
        text_auto=True,
        title='Number of Universities Per Province',
        color_discrete_sequence=px.colors.qualitative.Plotly
    )

    fig1.update_layout(
        title_x=0.5,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=500
    )

    st.plotly_chart(fig1, use_container_width=True)

    # ── Chart 2 ──────────────────────────────────────────────────────────────
    st.markdown('<div class="sub-title">🥧 Public vs Private Universities</div>', unsafe_allow_html=True)

    share_type = (
        c_uni_data.groupby('Type', observed=False)['UNI_Name']
        .nunique()
        .reset_index(name='University_Count')
    )

    fig2 = px.pie(
        share_type,
        names='Type',
        values='University_Count',
        title='Share of Universities by Type',
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    fig2.update_traces(
        textinfo="label+percent",
        marker=dict(line=dict(color="#ffffff", width=2))
    )

    fig2.update_layout(title_x=0.5)

    st.plotly_chart(fig2, use_container_width=True)

    # ── Chart 3 ──────────────────────────────────────────────────────────────
    st.markdown('<div class="sub-title">📚 Research Papers by Department</div>', unsafe_allow_html=True)

    research_dept = (
        c_uni_data.groupby('Department_Category', observed=False)['Research_Papers_Published']
        .sum()
        .reset_index()
        .sort_values(by='Research_Papers_Published', ascending=False)
        .head(10)
    )

    fig3 = px.bar(
        research_dept,
        x='Research_Papers_Published',
        y='Department_Category',
        orientation='h',
        color='Department_Category',
        text_auto=True,
        title='Top Department Categories by Research Output',
        color_discrete_sequence=px.colors.qualitative.Plotly
    )

    fig3.update_layout(
        title_x=0.5,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=600
    )

    st.plotly_chart(fig3, use_container_width=True)

    # ── Chart 4 ──────────────────────────────────────────────────────────────
    st.markdown('<div class="sub-title">💰 Fee Distribution by University Type</div>', unsafe_allow_html=True)

    fig4 = px.box(
        c_uni_data,
        x='Type',
        y='Fee_Per_Semester_PKR',
        color='Type',
        title='Distribution of Semester Fee by University Type',
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    fig4.update_layout(
        title_x=0.5,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig4, use_container_width=True)

    # ── Chart 5 ──────────────────────────────────────────────────────────────
    st.markdown('<div class="sub-title">🎯 Employment Ratio vs CGPA</div>', unsafe_allow_html=True)

    fig5 = px.scatter(
        c_uni_data,
        x='Avg_CGPA',
        y='Employment_Ratio_Pct',
        color='HEC_Category',
        hover_data=['UNI_Name', 'City'],
        title='Employment Ratio vs Average CGPA',
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    fig5.update_layout(
        title_x=0.5,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=600
    )

    st.plotly_chart(fig5, use_container_width=True)

    # ── Chart 6 ──────────────────────────────────────────────────────────────
    st.markdown('<div class="sub-title">📉 Dropout Rate Analysis</div>', unsafe_allow_html=True)

    drop_uni = (
        c_uni_data.groupby(['Province', 'Type'], observed=False)['Dropout_Rate_Pct']
        .mean()
        .reset_index()
    )

    fig6 = px.bar(
        drop_uni,
        x='Province',
        y='Dropout_Rate_Pct',
        color='Type',
        barmode='group',
        text_auto='.1f',
        title='Average Dropout Rate by Province and University Type',
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    fig6.update_layout(
        title_x=0.5,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=550
    )

    st.plotly_chart(fig6, use_container_width=True)

    # ── Chart 7 ──────────────────────────────────────────────────────────────
    st.markdown('<div class="sub-title">🔬 Research Productivity Distribution</div>', unsafe_allow_html=True)

    fig7 = px.histogram(
        enhanced_uni_data,
        x='Research_Per_Faculty',
        color='HEC_Category',
        nbins=30,
        opacity=0.7,
        barmode='overlay',
        title='Distribution of Research Output Per Faculty',
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    fig7.update_layout(
        title_x=0.5,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=550
    )

    st.plotly_chart(fig7, use_container_width=True)

    # ── Chart 8 ──────────────────────────────────────────────────────────────
    st.markdown('<div class="sub-title">💼 Fee vs Employment Ratio</div>', unsafe_allow_html=True)

    fig8 = px.scatter(
        c_uni_data,
        x='Fee_Per_Semester_PKR',
        y='Employment_Ratio_Pct',
        color='Province',
        size='Total_Enrollment',
        hover_data=['UNI_Name'],
        title='Employment Ratio vs Fee Per Semester',
        color_discrete_sequence=px.colors.qualitative.Safe,
        size_max=30
    )

    fig8.update_layout(
        title_x=0.5,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=650
    )

    st.plotly_chart(fig8, use_container_width=True)

    # ── Chart 9 ──────────────────────────────────────────────────────────────
    st.markdown('<div class="sub-title">🏆 University Score Across Provinces</div>', unsafe_allow_html=True)

    facet_data = (
        enhanced_uni_data.groupby(['Province', 'HEC_Category'], observed=False)['University_Score']
        .mean()
        .reset_index()
    )

    fig9 = px.bar(
        facet_data,
        x='HEC_Category',
        y='University_Score',
        color='HEC_Category',
        facet_col='Province',
        facet_col_wrap=3,
        text_auto='.1f',
        title='Average University Score by HEC Category Across Provinces',
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    fig9.update_layout(
        title_x=0.5,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=900
    )

    st.plotly_chart(fig9, use_container_width=True)

    # ── Chart 10 ─────────────────────────────────────────────────────────────
    st.markdown('<div class="sub-title">📈 Research Trends Over Time</div>', unsafe_allow_html=True)

    line_data = (
        c_uni_data.groupby(['Year', 'Department_Category'], observed=False)['Research_Papers_Published']
        .mean()
        .reset_index()
    )

    fig10 = px.line(
        line_data,
        x='Year',
        y='Research_Papers_Published',
        color='Department_Category',
        markers=True,
        title='Average Research Papers Published Over Time',
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    fig10.update_layout(
        title_x=0.5,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=650
    )

    st.plotly_chart(fig10, use_container_width=True)

    st.markdown("""
    <div style="
        margin-top:2rem;
        padding:1.5rem;
        border-radius:14px;
        background:#f0f5ff;
        border-left:6px solid #1a3c6e;
    ">
        <h3 style="color:#1a3c6e;">📌 Visualization Insights</h3>
        <ul style="line-height:1.9;">
            <li>Punjab dominates in the number of universities.</li>
            <li>Research-intensive departments consistently outperform others.</li>
            <li>Higher CGPA trends generally correlate with better employment ratios.</li>
            <li>Private universities typically have higher semester fee distributions.</li>
            <li>Research productivity varies significantly across HEC categories.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
