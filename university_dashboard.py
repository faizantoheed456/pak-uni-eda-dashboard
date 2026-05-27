# =========================================================
# ADVANCED INTERACTIVE ANALYTICS SECTIONS
# REPLACE OLD SECTIONS WITH THESE
# =========================================================

# =========================================================
# SECTION 1
# TOP 10 UNIVERSITIES BY EMPLOYMENT RATE
# =========================================================
st.subheader("🏆 Top Universities By Employment Rate")

employment_table = (
    filtered_df.groupby("UNI_Name")
    .agg({
        "Employment_Ratio_Pct":"mean",
        "Avg_CGPA":"mean",
        "Total_Enrollment":"sum"
    })
    .sort_values(by="Employment_Ratio_Pct", ascending=False)
    .head(10)
    .round(2)
)

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

    st.dataframe(
        employment_table,
        use_container_width=True,
        height=420
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    fig = px.funnel(
        employment_table.reset_index(),
        x="Employment_Ratio_Pct",
        y="UNI_Name",
        color="Employment_Ratio_Pct",
        color_continuous_scale=[
            "#85EFA3",
            "#00AFFF",
            "#FF7570"
        ]
    )

    fig.update_layout(
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        font_color="white",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# SECTION 2
# UNIVERSITY TYPE PERFORMANCE
# =========================================================
st.subheader("🎯 University Type Performance Comparison")

type_table = (
    filtered_df.groupby("Type")
    .agg({
        "Avg_CGPA":"mean",
        "Employment_Ratio_Pct":"mean",
        "Research_Papers_Published":"mean"
    })
    .round(2)
)

col1, col2 = st.columns([1,2])

with col1:

    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

    st.dataframe(
        type_table,
        use_container_width=True,
        height=350
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=type_table.iloc[0].values,
        theta=type_table.columns,
        fill='toself',
        name=type_table.index[0]
    ))

    if len(type_table) > 1:
        fig.add_trace(go.Scatterpolar(
            r=type_table.iloc[1].values,
            theta=type_table.columns,
            fill='toself',
            name=type_table.index[1]
        ))

    fig.update_layout(
        polar=dict(
            bgcolor=CARD
        ),
        paper_bgcolor=CARD,
        font_color="white",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# SECTION 3
# CITY WISE STUDENT DISTRIBUTION
# =========================================================
st.subheader("🌍 City Wise Student Distribution")

city_table = (
    filtered_df.groupby("City")
    .agg({
        "Total_Enrollment":"sum"
    })
    .sort_values(by="Total_Enrollment", ascending=False)
    .head(15)
)

col1, col2 = st.columns([1,2])

with col1:

    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

    st.dataframe(
        city_table,
        use_container_width=True,
        height=450
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    fig = px.sunburst(
        filtered_df,
        path=["Province","City"],
        values="Total_Enrollment",
        color="Total_Enrollment",
        color_continuous_scale=[
            "#85EFA3",
            "#00AFFF",
            "#FF7570"
        ]
    )

    fig.update_layout(
        paper_bgcolor=CARD,
        font_color="white",
        height=550
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# SECTION 4
# RESEARCH VS EMPLOYMENT
# =========================================================
st.subheader("📈 Research Impact on Employment")

research_table = (
    filtered_df.groupby("Department_Category")
    .agg({
        "Research_Papers_Published":"mean",
        "Employment_Ratio_Pct":"mean",
        "Avg_CGPA":"mean"
    })
    .round(2)
)

col1, col2 = st.columns([1,2])

with col1:

    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

    st.dataframe(
        research_table,
        use_container_width=True,
        height=350
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    fig = px.scatter_3d(
        research_table.reset_index(),
        x="Research_Papers_Published",
        y="Employment_Ratio_Pct",
        z="Avg_CGPA",
        color="Department_Category",
        size="Employment_Ratio_Pct"
    )

    fig.update_layout(
        paper_bgcolor=CARD,
        font_color="white",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# SECTION 5
# DROPOUT ANALYTICS
# =========================================================
st.subheader("⚠ Dropout & Risk Intelligence")

dropout_table = (
    filtered_df.groupby("Province")
    .agg({
        "Dropout_Rate_Pct":"mean",
        "Risk_Index":"mean",
        "Female_Share_Pct":"mean"
    })
    .round(2)
)

col1, col2 = st.columns([1,2])

with col1:

    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

    st.dataframe(
        dropout_table,
        use_container_width=True,
        height=350
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    fig = px.density_heatmap(
        filtered_df,
        x="Dropout_Rate_Pct",
        y="Risk_Index",
        z="Female_Share_Pct",
        nbinsx=20,
        nbinsy=20,
        color_continuous_scale=[
            "#85EFA3",
            "#00AFFF",
            "#FF7570"
        ]
    )

    fig.update_layout(
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        font_color="white",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# EXTRA INTERACTIVE SECTION
# =========================================================
st.subheader("🔎 Explore Any Numerical Column")

numeric_cols = filtered_df.select_dtypes(include='number').columns

selected_x = st.selectbox(
    "Select X Axis",
    numeric_cols,
    index=0
)

selected_y = st.selectbox(
    "Select Y Axis",
    numeric_cols,
    index=1
)

fig = px.scatter(
    filtered_df,
    x=selected_x,
    y=selected_y,
    color="Province",
    size="Total_Enrollment",
    hover_name="UNI_Name"
)

fig.update_layout(
    paper_bgcolor=CARD,
    plot_bgcolor=CARD,
    font_color="white",
    height=650
)

st.plotly_chart(fig, use_container_width=True)