import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Pakistan Higher Education Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
  /* Hide sidebar completely */
  [data-testid="collapsedControl"] { display: none !important; }
  [data-testid="stSidebar"]        { display: none !important; }

  /* Hide black top toolbar/header */
  [data-testid="stHeader"]         { display: none !important; }
  [data-testid="stToolbar"]        { display: none !important; }
  #MainMenu                        { display: none !important; }
  header                           { display: none !important; }

  /* Page background */
  .stApp { background-color: #F4F2EE; }

  /* Constrain and pad main content */
  .block-container {
      max-width: 1240px;
      padding: 2.5rem 2rem 4rem 2rem !important;
  }

  /* ── Typography ─────────────────────────── */
  h1 {
      color: #1A1A18 !important;
      text-align: center;
      font-size: 2rem !important;
      margin-bottom: 0.25rem !important;
  }
  h2 {
      color: #1A1A18 !important;
      font-size: 1.15rem !important;
      border-left: 4px solid #1D9E75;
      padding: 6px 0 6px 12px;
      margin-top: 0 !important;
      margin-bottom: 0 !important;
      line-height: 1.4;
  }
  p, li, span, label { color: #1A1A18; }

  /* ── KPI metric cards ────────────────────── */
  [data-testid="stMetric"] {
      background: #FFFFFF;
      border: 1px solid #DDD9D0;
      border-radius: 12px;
      padding: 20px 18px 16px 18px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.055);
  }
  [data-testid="stMetricLabel"] { color: #4A4845 !important; font-size: 0.82rem !important; font-weight: 600; }
  [data-testid="stMetricValue"] { color: #1A1A18 !important; font-size: 1.45rem !important; }

  /* ── Chart cards ─────────────────────────── */
  .chart-card {
      background: #FFFFFF;
      border-radius: 14px;
      padding: 4px 4px 0 4px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      margin-bottom: 0;
  }

  /* ── Insight box ─────────────────────────── */
  .insight-box {
      background: #FFFFFF;
      border-left: 4px solid #1D9E75;
      border-radius: 0 10px 10px 0;
      padding: 12px 16px;
      margin-top: 6px;
      margin-bottom: 32px;
      font-size: 13.5px;
      color: #2E2D2B;
      line-height: 1.75;
      box-shadow: 0 1px 5px rgba(0,0,0,0.05);
  }
  .insight-box strong { color: #1A1A18; }

  /* ── Section header wrapper ──────────────── */
  .section-header {
      margin-top: 48px;
      margin-bottom: 20px;
  }

  /* ── Full-width chart spacer ─────────────── */
  .chart-below {
      margin-bottom: 32px;
  }

  /* Kill streamlit's own element gaps so we control them */
  .element-container { margin-bottom: 0 !important; }
  div[data-testid="stVerticalBlock"] > div { gap: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# COLOUR CONSTANTS
# ─────────────────────────────────────────────
CARD_BG  = "#FFFFFF"
GRID_CLR = "#E2DDD5"
FONT_CLR = "#1A1A18"
FONT_SEC = "#4A4845"

HEC_CLR  = {"W1":"#1D9E75","W2":"#378ADD","W3":"#BA7517","W4":"#D85A30"}
PROV_CLR = {"Punjab":"#1D9E75","Sindh":"#378ADD","KPK":"#BA7517",
             "Islamabad":"#7F77DD","Balochistan":"#D85A30",
             "AJK":"#D4537E","Gilgit-Baltistan":"#639922"}
TYPE_CLR = {"Public":"#378ADD","Private":"#D85A30"}
DEPT_CLR = {"STEM":"#1D9E75","Business":"#378ADD","Arts & Social Sciences":"#D85A30"}
BAND_CLR = {"Low":"#1D9E75","Mid":"#BA7517","High":"#D85A30"}
GB_CLR   = {"Male Dominated":"#378ADD","Balanced":"#1D9E75","Female Dominated":"#D4537E"}

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def base_layout(title, xlab="", ylab="", legend_title="", height=380):
    """Single source of truth for all Plotly layouts."""
    return dict(
        plot_bgcolor  = CARD_BG,
        paper_bgcolor = CARD_BG,
        height        = height,
        font=dict(family="Segoe UI, Arial, sans-serif", color=FONT_CLR, size=13),
        title=dict(
            text=f"<b>{title}</b>",
            font=dict(size=15, color=FONT_CLR),
            x=0.5, xanchor="center"
        ),
        margin=dict(l=60, r=30, t=58, b=60),
        legend=dict(
            title_text  = legend_title,
            bgcolor     = CARD_BG,
            bordercolor = GRID_CLR,
            borderwidth = 1,
            font=dict(color=FONT_CLR, size=12),
            title_font=dict(color=FONT_SEC, size=12),
        ),
        xaxis=dict(
            title          = xlab,
            gridcolor      = GRID_CLR,
            linecolor      = GRID_CLR,
            zerolinecolor  = GRID_CLR,
            tickfont       = dict(size=11, color=FONT_CLR),
            title_font     = dict(size=12, color=FONT_SEC),
        ),
        yaxis=dict(
            title          = ylab,
            gridcolor      = GRID_CLR,
            linecolor      = GRID_CLR,
            zerolinecolor  = GRID_CLR,
            tickfont       = dict(size=11, color=FONT_CLR),
            title_font     = dict(size=12, color=FONT_SEC),
        ),
    )


def section(label: str):
    """Render a section header with proper vertical spacing."""
    st.markdown(f'<div class="section-header"><h2>{label}</h2></div>',
                unsafe_allow_html=True)


def insight(text: str):
    """Render the insight box directly below a chart."""
    st.markdown(f'<div class="insight-box">💡 &nbsp;{text}</div>',
                unsafe_allow_html=True)


# ─────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("pakistan_universities_dataset_enhanced.csv")
    df['scholarship_pct'] = (
        df['Scholarship_Students'] / df['Total_Enrollment'] * 100
    ).round(1)
    return df

df = load_data()


# ═══════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════
st.title("🎓 Pakistan Higher Education Landscape")
st.markdown(
    "<p style='text-align:center; color:#4A4845; font-size:14.5px; "
    "margin-top:2px; margin-bottom:24px;'>"
    "Enrollment · Outcomes · Institutional Quality &nbsp;|&nbsp; "
    "7 Provinces &nbsp;|&nbsp; 2022–2025</p>",
    unsafe_allow_html=True
)

# ── KPI Row ──────────────────────────────────────
k1, k2, k3, k4, k5 = st.columns(5, gap="medium")
k1.metric("🏛️ Total Universities",  df['UNI_Name'].nunique())
k2.metric("👥 Total Enrolled",       f"{df['Total_Enrollment'].sum():,}")
k3.metric("💼 Avg Employment Rate",  f"{df['Employment_Ratio_Pct'].mean():.1f}%")
k4.metric("📉 Avg Dropout Rate",     f"{df['Dropout_Rate_Pct'].mean():.1f}%")
k5.metric("💰 Avg Fee / Semester",   f"PKR {df['Fee_Per_Semester_PKR'].mean():,.0f}")

st.markdown("<div style='margin-top:8px'></div>", unsafe_allow_html=True)
st.divider()


# ═══════════════════════════════════════════════════
# A — MARKET OVERVIEW
# ═══════════════════════════════════════════════════
section("A — Market Overview")

col1, col2 = st.columns(2, gap="large")

with col1:
    prov_type = (
        df.drop_duplicates(subset=['UNI_Name','Province','Type'])
        .groupby(['Province','Type'])['UNI_Name'].count()
        .reset_index(name='Count')
    )
    prov_order = (
        prov_type.groupby('Province')['Count'].sum()
        .sort_values(ascending=False).index.tolist()
    )
    fig1 = px.bar(
        prov_type, x='Province', y='Count', color='Type',
        color_discrete_map=TYPE_CLR, text='Count',
        category_orders={"Province": prov_order}
    )
    fig1.update_traces(textposition='inside', textfont_color='white')
    fig1.update_layout(**base_layout(
        "Universities per Province",
        xlab="Province", ylab="Count", legend_title="Type"
    ))
    st.plotly_chart(fig1, use_container_width=True)
    insight(
        "<strong>Punjab dominates</strong> with the most universities of both types. "
        "Balochistan and Gilgit-Baltistan rely almost entirely on public institutions, "
        "highlighting a sharp access divide across the country."
    )

with col2:
    type_counts = (
        df.drop_duplicates(subset=['UNI_Name','Type'])
        .groupby('Type')['UNI_Name'].count()
        .reset_index(name='Count')
    )
    fig2 = go.Figure(go.Pie(
        labels=type_counts['Type'],
        values=type_counts['Count'],
        hole=0.52,
        marker_colors=[TYPE_CLR.get(t, "#999") for t in type_counts['Type']],
        textinfo='label+percent',
        textfont=dict(color=FONT_CLR, size=13),
        insidetextorientation='radial',
    ))
    fig2.add_annotation(
        text="Universities", x=0.5, y=0.5,
        font=dict(size=13, color=FONT_CLR), showarrow=False
    )
    fig2.update_layout(**base_layout("Public vs Private Share", legend_title="Type"))
    st.plotly_chart(fig2, use_container_width=True)
    insight(
        "The sector splits roughly <strong>60 % public / 40 % private</strong>. "
        "Private universities are growing fast, reflecting demand that public "
        "capacity alone can no longer absorb."
    )


# ═══════════════════════════════════════════════════
# B — QUALITY & RANKINGS
# ═══════════════════════════════════════════════════
section("B — Quality & Rankings")

uni_agg = (
    df.groupby('UNI_Name')
    .agg(
        University_Score=('University_Score','mean'),
        Fee_Value_Score =('Fee_Value_Score','mean'),
        Total_Enrollment=('Total_Enrollment','mean'),
        HEC_Category    =('HEC_Category','first'),
    )
    .reset_index()
)
med_x = uni_agg['University_Score'].median()
med_y = uni_agg['Fee_Value_Score'].median()

fig3 = px.scatter(
    uni_agg, x='University_Score', y='Fee_Value_Score',
    color='HEC_Category', size='Total_Enrollment', size_max=30,
    color_discrete_map=HEC_CLR, opacity=0.82, hover_name='UNI_Name'
)
fig3.add_vline(x=med_x, line_dash="dash", line_color=GRID_CLR)
fig3.add_hline(y=med_y, line_dash="dash", line_color=GRID_CLR)
for txt, ax, ay in [
    ("Premium Value",           med_x * 1.01, med_y * 1.02),
    ("Expensive & Low Quality", med_x * 0.60, med_y * 1.02),
    ("Quality, Low Value",      med_x * 1.01, med_y * 0.85),
    ("Low Quality & Low Value", med_x * 0.60, med_y * 0.85),
]:
    fig3.add_annotation(
        text=txt, x=ax, y=ay,
        font=dict(size=10, color=FONT_SEC), showarrow=False
    )
fig3.update_layout(**base_layout(
    "Value-for-Money Quadrant",
    xlab="University Score", ylab="Fee Value Score",
    legend_title="HEC Category", height=420
))
st.plotly_chart(fig3, use_container_width=True)
insight(
    "<strong>W1 universities cluster in the Premium Value quadrant</strong> — delivering "
    "high quality at justified fees. Several W3/W4 private institutions sit in "
    "'Expensive & Low Quality', charging premium fees without matching outcomes. "
    "Bubble size reflects enrollment scale."
)

hec_prov = (
    df.drop_duplicates(subset=['UNI_Name','Province','HEC_Category'])
    .groupby(['Province','HEC_Category'])['UNI_Name'].count()
    .reset_index(name='Count')
)
fig4 = px.bar(
    hec_prov, x='Province', y='Count', color='HEC_Category',
    color_discrete_map=HEC_CLR, barmode='group'
)
fig4.update_layout(**base_layout(
    "HEC Category Distribution by Province",
    xlab="Province", ylab="Count", legend_title="HEC Category"
))
st.plotly_chart(fig4, use_container_width=True)
insight(
    "<strong>Punjab and Islamabad hold the most W1 and W2 universities.</strong> "
    "KPK and Balochistan have very few top-ranked institutions, meaning students "
    "in those provinces must relocate to access elite higher education."
)


# ═══════════════════════════════════════════════════
# C — ENROLLMENT & CAPACITY
# ═══════════════════════════════════════════════════
section("C — Enrollment & Capacity")

col1, col2 = st.columns(2, gap="large")

with col1:
    enroll_trend = (
        df.groupby(['Year','Province'])['Total_Enrollment'].sum().reset_index()
    )
    fig5 = px.line(
        enroll_trend, x='Year', y='Total_Enrollment', color='Province',
        color_discrete_map=PROV_CLR, markers=True
    )
    fig5.update_layout(**base_layout(
        "Enrollment Trend by Province",
        xlab="Year", ylab="Total Enrollment", legend_title="Province"
    ))
    fig5.update_yaxes(tickformat=",")
    st.plotly_chart(fig5, use_container_width=True)
    insight(
        "<strong>Enrollment has grown across all provinces from 2022 to 2025.</strong> "
        "Punjab leads by a large margin. Gilgit-Baltistan and AJK show the flattest "
        "trajectories, signalling persistent capacity gaps in remote regions."
    )

with col2:
    sfr = df.groupby(['Province','Type'])['Student_Faculty_Ratio'].mean().reset_index()
    fig6 = px.bar(
        sfr, x='Province', y='Student_Faculty_Ratio', color='Type',
        color_discrete_map=TYPE_CLR, barmode='group'
    )
    fig6.add_hline(
        y=25, line_dash="dash", line_color="#D85A30",
        annotation_text="HEC Benchmark (25:1)",
        annotation_position="top right",
        annotation_font_color=FONT_CLR
    )
    fig6.update_layout(**base_layout(
        "Student-Faculty Ratio by Province",
        xlab="Province", ylab="Avg S:F Ratio", legend_title="Type"
    ))
    st.plotly_chart(fig6, use_container_width=True)
    insight(
        "Several provinces <strong>breach the HEC benchmark of 25:1</strong>, "
        "indicating faculty shortages. Public universities in Balochistan and Sindh "
        "are the most overstretched — directly threatening teaching quality."
    )


# ═══════════════════════════════════════════════════
# D — GRADUATE OUTCOMES
# ═══════════════════════════════════════════════════
section("D — Graduate Outcomes")

emp_trend = df.groupby(['Year','HEC_Category'])['Employment_Ratio_Pct'].mean().reset_index()
fig7 = px.line(
    emp_trend, x='Year', y='Employment_Ratio_Pct', color='HEC_Category',
    color_discrete_map=HEC_CLR, markers=True
)
fig7.update_layout(**base_layout(
    "Employment Rate Trend by HEC Category",
    xlab="Year", ylab="Employment Rate (%)", legend_title="HEC Category"
))
fig7.update_yaxes(range=[40, 100], ticksuffix="%")
st.plotly_chart(fig7, use_container_width=True)
insight(
    "<strong>W1 universities consistently outperform all other categories</strong> on graduate "
    "employment. The gap between W1 and W4 has widened year-on-year, making HEC ranking "
    "an increasingly reliable signal of job-market outcomes."
)

col1, col2 = st.columns(2, gap="large")

with col1:
    fig8 = px.scatter(
        df, x='Avg_CGPA', y='Employment_Ratio_Pct',
        color='HEC_Category', color_discrete_map=HEC_CLR,
        opacity=0.55, trendline='ols',
        trendline_scope='overall', trendline_color_override=FONT_CLR
    )
    fig8.update_traces(marker_size=5)
    fig8.update_layout(**base_layout(
        "Employment vs CGPA",
        xlab="Avg CGPA", ylab="Employment Rate (%)", legend_title="HEC Category"
    ))
    st.plotly_chart(fig8, use_container_width=True)
    insight(
        "There is a <strong>positive but moderate correlation</strong> between CGPA and employment. "
        "W1 graduates sit above the trendline at equal CGPA levels, pointing to the added "
        "advantage of institutional reputation and industry networks."
    )

with col2:
    dropout = df.groupby(['Province','Type'])['Dropout_Rate_Pct'].mean().reset_index()
    fig9 = px.bar(
        dropout, x='Province', y='Dropout_Rate_Pct', color='Type',
        color_discrete_map=TYPE_CLR, barmode='group',
        text=dropout['Dropout_Rate_Pct'].round(1).astype(str) + "%"
    )
    fig9.update_traces(textposition='outside', textfont_color=FONT_CLR)
    fig9.update_layout(**base_layout(
        "Dropout Rate by Province",
        xlab="Province", ylab="Dropout Rate (%)", legend_title="Type"
    ))
    st.plotly_chart(fig9, use_container_width=True)
    insight(
        "<strong>Balochistan records the highest dropout rates</strong>, driven by financial hardship, "
        "distance to campuses, and limited student support. Punjab private universities "
        "show the lowest rates, underlining the impact of resources and infrastructure."
    )


# ═══════════════════════════════════════════════════
# E — FEES & AFFORDABILITY
# ═══════════════════════════════════════════════════
section("E — Fees & Affordability")

col1, col2 = st.columns(2, gap="large")

with col1:
    fee_trend = df.groupby(['Year','Fee_Band'])['Annual_Fee_PKR'].mean().reset_index()
    fig10 = px.line(
        fee_trend, x='Year', y='Annual_Fee_PKR', color='Fee_Band',
        color_discrete_map=BAND_CLR, markers=True
    )
    fig10.update_layout(**base_layout(
        "Fee Inflation Trend by Band",
        xlab="Year", ylab="Annual Fee (PKR)", legend_title="Fee Band"
    ))
    fig10.update_yaxes(tickformat=",")
    st.plotly_chart(fig10, use_container_width=True)
    insight(
        "Fees have <strong>risen across all bands since 2022</strong>. High-band institutions "
        "show the steepest absolute increase. Even low-band public universities have seen "
        "hikes, squeezing low-income students who depend on them most."
    )

with col2:
    fig11 = px.box(
        df, x='Type', y='Fee_Per_Semester_PKR', color='Type',
        color_discrete_map=TYPE_CLR, points='outliers'
    )
    fig11.update_layout(**base_layout(
        "Fee Distribution by University Type",
        xlab="Type", ylab="Fee per Semester (PKR)", legend_title="Type"
    ))
    st.plotly_chart(fig11, use_container_width=True)
    insight(
        "<strong>Private fees vary far more widely than public ones.</strong> "
        "The public median is substantially lower, yet a long upper whisker shows "
        "some public universities charge near-private rates — blurring the affordability boundary."
    )


# ═══════════════════════════════════════════════════
# F — RESEARCH OUTPUT
# ═══════════════════════════════════════════════════
section("F — Research Output")

col1, col2 = st.columns(2, gap="large")

with col1:
    res_trend = (
        df.groupby(['Year','Department_Category'])['Research_Papers_Published']
        .mean().reset_index()
    )
    fig13 = px.line(
        res_trend, x='Year', y='Research_Papers_Published',
        color='Department_Category', color_discrete_map=DEPT_CLR, markers=True
    )
    fig13.update_layout(**base_layout(
        "Research Papers Trend by Department",
        xlab="Year", ylab="Avg Papers Published", legend_title="Department"
    ))
    st.plotly_chart(fig13, use_container_width=True)
    insight(
        "<strong>STEM leads research output and is the only category with consistent growth.</strong> "
        "Business and Arts & Social Sciences lag significantly, pointing to "
        "under-investment in non-STEM research infrastructure and incentives."
    )

with col2:
    fig14 = px.histogram(
        df, x='Research_Per_Faculty', color='HEC_Category',
        color_discrete_map=HEC_CLR, barmode='overlay', opacity=0.75, nbins=30
    )
    fig14.update_layout(**base_layout(
        "Research per Faculty Distribution",
        xlab="Research per Faculty", ylab="Count", legend_title="HEC Category"
    ))
    st.plotly_chart(fig14, use_container_width=True)
    insight(
        "Most faculty publish under 5 papers per cycle. <strong>W1 institutions have a longer "
        "right tail</strong> — a concentrated group of highly productive researchers driving "
        "outsized output. W3/W4 distributions cluster near zero."
    )

res_uni = (
    df.groupby(['UNI_Name','Department_Category'])
    .agg(
        Industry_Tie_Ups    =('Industry_Tie_Ups','mean'),
        Employment_Ratio_Pct=('Employment_Ratio_Pct','mean'),
        Total_Enrollment    =('Total_Enrollment','mean'),
    )
    .reset_index()
)
fig15 = px.scatter(
    res_uni, x='Industry_Tie_Ups', y='Employment_Ratio_Pct',
    color='Department_Category', size='Total_Enrollment', size_max=25,
    color_discrete_map=DEPT_CLR, hover_name='UNI_Name',
    trendline='ols', trendline_scope='overall', trendline_color_override=FONT_CLR
)
fig15.update_layout(**base_layout(
    "Industry Tie-ups vs Employment Rate",
    xlab="Industry Tie-Ups", ylab="Employment Rate (%)",
    legend_title="Department", height=420
))
st.plotly_chart(fig15, use_container_width=True)
insight(
    "<strong>More industry partnerships correlate strongly with higher employment rates</strong>, "
    "especially for STEM. Universities with 15+ active tie-ups consistently exceed 70 % employment, "
    "making industry linkage one of the strongest levers for improving graduate outcomes."
)


# ═══════════════════════════════════════════════════
# G — EQUITY & GENDER
# ═══════════════════════════════════════════════════
section("G — Equity & Gender")

col1, col2 = st.columns(2, gap="large")

with col1:
    fem_trend = df.groupby(['Year','Province'])['Female_Share_Pct'].mean().reset_index()
    fig16 = px.line(
        fem_trend, x='Year', y='Female_Share_Pct',
        color='Province', color_discrete_map=PROV_CLR, markers=True
    )
    fig16.add_hline(
        y=50, line_dash="dash", line_color="#D4537E",
        annotation_text="Gender Parity (50%)",
        annotation_position="top right",
        annotation_font_color=FONT_CLR
    )
    fig16.update_layout(**base_layout(
        "Female Enrollment Share by Province",
        xlab="Year", ylab="Female Share (%)", legend_title="Province"
    ))
    fig16.update_yaxes(range=[20, 70], ticksuffix="%")
    st.plotly_chart(fig16, use_container_width=True)
    insight(
        "<strong>Islamabad and Punjab are closest to gender parity</strong>, with female share "
        "crossing 50 % in recent years. Balochistan and KPK stagnate around 30–35 %, "
        "reflecting deep socio-cultural and infrastructure barriers."
    )

with col2:
    gb_prov = (
        df.drop_duplicates(subset=['UNI_Name','Province','Gender_Balance_Category'])
        .groupby(['Province','Gender_Balance_Category'])['UNI_Name'].count()
        .reset_index(name='Count')
    )
    fig17 = px.bar(
        gb_prov, x='Province', y='Count', color='Gender_Balance_Category',
        color_discrete_map=GB_CLR, barmode='stack'
    )
    fig17.update_layout(**base_layout(
        "Gender Balance Category by Province",
        xlab="Province", ylab="University Count", legend_title="Gender Balance"
    ))
    st.plotly_chart(fig17, use_container_width=True)
    insight(
        "The majority of Pakistani universities remain <strong>Male Dominated</strong>. "
        "Female-dominated institutions are rare outside Islamabad and Punjab. "
        "Truly balanced campuses are the exception — not the norm — nationally."
    )


# ═══════════════════════════════════════════════════
# H — RISK & INSTITUTIONAL HEALTH
# ═══════════════════════════════════════════════════
section("H — Risk & Institutional Health")

col1, col2 = st.columns(2, gap="large")

with col1:
    risk_prov = df.groupby(['Province','Type'])['Risk_Index'].mean().reset_index()
    fig18 = px.bar(
        risk_prov, x='Province', y='Risk_Index', color='Type',
        color_discrete_map=TYPE_CLR, barmode='group',
        text=risk_prov['Risk_Index'].round(3).astype(str)
    )
    fig18.update_traces(textposition='outside', textfont_color=FONT_CLR)
    fig18.update_layout(**base_layout(
        "Avg Risk Index by Province",
        xlab="Province", ylab="Risk Index", legend_title="Type"
    ))
    st.plotly_chart(fig18, use_container_width=True)
    insight(
        "<strong>Balochistan private universities carry the highest institutional risk</strong> — "
        "a combination of high dropouts, weak employment, and thin financial buffers. "
        "Islamabad public universities score the lowest, backed by stable federal funding."
    )

with col2:
    risk_uni = (
        df.groupby(['UNI_Name','Type'])
        .agg(
            Risk_Index          =('Risk_Index','mean'),
            Employment_Ratio_Pct=('Employment_Ratio_Pct','mean'),
            Total_Enrollment    =('Total_Enrollment','mean'),
        )
        .reset_index()
    )
    fig19 = px.scatter(
        risk_uni, x='Risk_Index', y='Employment_Ratio_Pct',
        color='Type', size='Total_Enrollment', size_max=30,
        color_discrete_map=TYPE_CLR, hover_name='UNI_Name', opacity=0.8
    )
    fig19.update_layout(**base_layout(
        "Risk Index vs Employment Rate",
        xlab="Risk Index", ylab="Employment Rate (%)", legend_title="Type"
    ))
    st.plotly_chart(fig19, use_container_width=True)
    insight(
        "A <strong>clear negative relationship</strong> exists between risk and employment. "
        "High-risk institutions cluster at the bottom — poor outcomes compound instability. "
        "Large, low-risk public universities achieve the highest employment rates."
    )


# ═══════════════════════════════════════════════════
# I — INTERNATIONAL PRESENCE
# ═══════════════════════════════════════════════════
section("I — International Presence")

intl = df.groupby(['Province','HEC_Category'])['International_Students'].sum().reset_index()
fig20 = px.bar(
    intl, x='Province', y='International_Students', color='HEC_Category',
    color_discrete_map=HEC_CLR, barmode='stack'
)
fig20.update_layout(**base_layout(
    "International Students by Province & HEC Category",
    xlab="Province", ylab="International Students",
    legend_title="HEC Category", height=400
))
st.plotly_chart(fig20, use_container_width=True)
insight(
    "<strong>Punjab and Islamabad attract almost all international students</strong>, "
    "primarily through W1 and W2 institutions. Other provinces draw negligible numbers, "
    "limiting their research collaboration potential and global exposure."
)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.divider()
st.markdown(
    "<p style='text-align:center; color:#4A4845; font-size:12px; margin-top:8px;'>"
    "Data: pakistan_universities_dataset_enhanced.csv &nbsp;|&nbsp; "
    "Built with Streamlit + Plotly</p>",
    unsafe_allow_html=True
)