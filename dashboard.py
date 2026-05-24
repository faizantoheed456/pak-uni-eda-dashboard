import streamlit as st
import pandas as pd
import numpy as np
 
# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Pakistani Universities EDA",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
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
 
raw_df   = load_raw()
clean_df = load_clean()
 
# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎓 EDA Dashboard")
    st.markdown("**Pakistani Universities**")
    st.markdown("---")
 
    st.markdown('<div class="sidebar-section-label">Navigate</div>', unsafe_allow_html=True)
    page = st.radio(
        "",
        ["🏠  Home", "📂  Dataset Viewer", "🔍  Inspection", "🧹  Cleaning"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown('<div class="sidebar-section-label">Dataset Info</div>', unsafe_allow_html=True)
    st.markdown(f"**Raw rows:** {raw_df.shape[0]:,}")
    st.markdown(f"**Raw cols:** {raw_df.shape[1]}")
    st.markdown(f"**Clean cols:** {clean_df.shape[1]}")
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