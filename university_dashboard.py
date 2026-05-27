import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Pakistan Universities Analytics",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# COLORS
# =========================================================
GREEN = "#85EFA3"
BLUE = "#00AFFF"
CORAL = "#FF7570"
DARK = "#111827"
CARD = "#1F2937"
TEXT = "#F9FAFB"

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():
    return pd.read_csv("pakistan_universities_dataset_enhanced.csv")

df = load_data()

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown(f"""
<style>

html, body, [class*="css"] {{
    font-family: 'Poppins', sans-serif;
    background-color: {DARK};
    color: white;
}}

section[data-testid="stSidebar"] {{
    background-color: #0B1120;
    border-right: 2px solid {BLUE};
}}

.block-container {{
    padding-top: 1rem;
    padding-bottom: 2rem;
}}

.main-title {{
    font-size: 55px;
    font-weight: bold;
    text-align: center;
    background: linear-gradient(90deg, {GREEN}, {BLUE}, {CORAL});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}}

.sub-title {{
    text-align: center;
    color: #B8C1CC;
    font-size: 18px;
    margin-bottom: 40px;
}}

.metric-card {{
    background: linear-gradient(145deg, #1F2937, #111827);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.1);
}}

.metric-title {{
    font-size: 18px;
    color: #B8C1CC;
}}

.metric-value {{
    font-size: 35px;
    font-weight: bold;
    color: white;
}}

.chart-card {{
    background-color: {CARD};
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}}

.insight-box {{
    background: linear-gradient(135deg, rgba(133,239,163,0.2), rgba(0,175,255,0.2));
    padding: 25px;
    border-radius: 20px;
    border-left: 5px solid {GREEN};
    margin-top: 20px;
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown(
    """
    <div class='main-title'>
        Pakistan Universities Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='sub-title'>
        Modern Business Intelligence & Educational Analytics Platform
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("🎛 Dashboard Controls")

province = st.sidebar.multiselect(
    "Select Province",
    df['Province'].unique(),
    default=df['Province'].unique()
)

uni_type = st.sidebar.multiselect(
    "Select University Type",
    df['Type'].unique(),
    default=df['Type'].unique()
)

filtered_df = df[
    (df['Province'].isin(province)) &
    (df['Type'].isin(uni_type))
]

# =========================================================
# KPI SECTION
# =========================================================
total_uni = filtered_df['UNI_Name'].nunique()
students = filtered_df['Total_Enrollment'].sum()
avg_cgpa = filtered_df['Avg_CGPA'].mean()
employment = filtered_df['Employment_Ratio_Pct'].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>🎓 Universities</div>
        <div class='metric-value'>{total_uni}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>👨‍🎓 Students</div>
        <div class='metric-value'>{students:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>📚 Avg CGPA</div>
        <div class='metric-value'>{avg_cgpa:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>💼 Employment %</div>
        <div class='metric-value'>{employment:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# SECTION 1
# =========================================================
st.subheader("📍 Province Wise Enrollment Analysis")

province_table = filtered_df.groupby('Province').agg({
    'Total_Enrollment':'sum'
}).sort_values(by='Total_Enrollment', ascending=False)

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.dataframe(province_table, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    fig = px.bar(
        province_table,
        x='Total_Enrollment',
        y=province_table.index,
        orientation='h',
        color='Total_Enrollment',
        color_continuous_scale=['#85EFA3','#00AFFF','#FF7570']
    )

    fig.update_layout(
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        font_color='white',
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# SECTION 2
# =========================================================
st.subheader("🔬 Research Productivity")

research_table = filtered_df.groupby('Type').agg({
    'Research_Papers_Published':'mean',
    'Research_Per_Faculty':'mean'
}).round(2)

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.dataframe(research_table, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    fig = px.pie(
        research_table,
        values='Research_Papers_Published',
        names=research_table.index,
        hole=0.5,
        color_discrete_sequence=[GREEN, BLUE, CORAL]
    )

    fig.update_layout(
        paper_bgcolor=CARD,
        font_color='white',
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# SECTION 3
# =========================================================
st.subheader("💰 Fee Structure Analysis")

fee_table = filtered_df.groupby('Department_Category').agg({
    'Fee_Per_Semester_PKR':'mean'
}).round(0)

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.dataframe(fee_table, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    fig = px.treemap(
        fee_table.reset_index(),
        path=['Department_Category'],
        values='Fee_Per_Semester_PKR',
        color='Fee_Per_Semester_PKR',
        color_continuous_scale=['#85EFA3','#00AFFF','#FF7570']
    )

    fig.update_layout(
        paper_bgcolor=CARD,
        font_color='white',
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# SECTION 4
# =========================================================
st.subheader("👩 Female Participation Analysis")

female_table = filtered_df.groupby('Province').agg({
    'Female_Share_Pct':'mean'
}).round(2)

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.dataframe(female_table, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    fig = px.area(
        female_table,
        x=female_table.index,
        y='Female_Share_Pct'
    )

    fig.update_traces(
        line_color=CORAL
    )

    fig.update_layout(
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        font_color='white',
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# SECTION 5
# =========================================================
st.subheader("⚠ Risk & Dropout Analysis")

risk_table = filtered_df.groupby('Province').agg({
    'Risk_Index':'mean',
    'Dropout_Rate_Pct':'mean'
}).round(2)

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.dataframe(risk_table, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    fig = px.scatter(
        filtered_df,
        x='Dropout_Rate_Pct',
        y='Risk_Index',
        size='Total_Enrollment',
        color='Province',
        hover_name='UNI_Name'
    )

    fig.update_layout(
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        font_color='white',
        height=550
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# BUSINESS INSIGHTS
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='insight-box'>

<h2>📈 Business Insights</h2>

<ul>
<li>Punjab and Sindh dominate educational infrastructure and student enrollment.</li>

<li>Public universities show higher research productivity because of larger faculty size and funding.</li>

<li>Technical and engineering departments charge significantly higher semester fees.</li>

<li>Higher dropout rates directly increase institutional risk levels.</li>

<li>Female participation is improving in multiple provinces, reflecting stronger educational inclusion.</li>

<li>Universities with better employment ratios have stronger market reputation.</li>

<li>Research-focused institutions can attract international collaborations and grants.</li>

<li>Institutions with lower research output should increase faculty development programs.</li>

</ul>

</div>
""", unsafe_allow_html=True)

# =========================================================
# COMPLETE DATASET
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)

with st.expander("📂 View Full Dataset"):
    st.dataframe(filtered_df, use_container_width=True)