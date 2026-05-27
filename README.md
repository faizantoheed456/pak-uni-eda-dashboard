# 🎓 EDA of Pakistani Universities
 
> A full end-to-end Exploratory Data Analysis of Pakistan's higher education landscape — spanning data inspection, multi-step cleaning, grouped aggregations, feature engineering, and an interactive Streamlit dashboard.
 
---
 
## 📋 Table of Contents
 
- [Project Overview](#-project-overview)
- [Project Structure](#-project-structure)
- [Dataset Overview](#-dataset-overview)
- [Analysis Pipeline](#-analysis-pipeline)
  - [1. Data Loading & Inspection](#1-data-loading--inspection)
  - [2. Data Cleaning](#2-data-cleaning)
  - [3. Grouping & Aggregations](#3-grouping--aggregations)
  - [4. Feature Engineering](#4-feature-engineering)
- [Streamlit Dashboard](#️-streamlit-dashboard)
- [Key Findings](#-key-findings)
- [Requirements & Installation](#-requirements--installation)
- [Running the Project](#-running-the-project)
---
 
## 📌 Project Overview
 
This project performs a comprehensive Exploratory Data Analysis (EDA) on a multi-year, department-level dataset of **91 Pakistani universities** across **7 provinces and regions**, covering academic years **2022–2025**.
 
The goal is to surface data-driven insights about institutional quality, gender equity, research output, selectivity, dropout risk, and graduate employability across Pakistan's higher education sector.
 
The project is structured as a **three-layer deliverable**:
 
| Layer | Artifact |
|-------|----------|
| Analysis | `EDA_of_Pakistani_Universities.ipynb` — Full Jupyter notebook pipeline |
| Data | Three versioned CSVs (raw → clean → enhanced) |
| Visualization | `dashboard.py` — Interactive 6-page Streamlit dashboard |
 
---
 
## 📁 Project Structure
 
```
📦 EDA of Pakistani Universities
├── pakistan_universities_dataset.csv          # Raw dataset          (2,584 rows × 34 columns)
├── pakistan_universities_dataset_clean.csv    # Cleaned dataset      (2,584 rows × 50 columns)
├── pakistan_universities_dataset_enhanced.csv # Feature-engineered   (2,584 rows × 64 columns)
├── EDA_of_Pakistani_Universities.ipynb        # Jupyter Notebook — full EDA pipeline
├── dashboard.py                               # Streamlit interactive dashboard
└── README.md                                  # This file
```
 
---
 
## 📊 Dataset Overview
 
| Property | Value |
|----------|-------|
| **Source** | Pakistani universities — multi-year, department-level records |
| **Raw Shape** | 2,584 rows × 34 columns |
| **Universities** | 91 unique institutions |
| **Provinces / Regions** | AJK, Balochistan, Gilgit-Baltistan, Islamabad, KPK, Punjab, Sindh |
| **Institution Types** | Public, Private |
| **Years Covered** | 2022, 2023, 2024, 2025 |
| **Granularity** | University × Department × Year |
 
### Key Columns
 
| Column | Description |
|--------|-------------|
| `UNI_ID` / `UNI_Name` | Unique university identifier and full name |
| `Type` | Public or Private |
| `Province` / `City` | Geographic location |
| `Established_Year` | Year of founding |
| `HEC_Ranking` / `HEC_Category` | Higher Education Commission ranking and tier |
| `Department_Name` / `Department_Category` | Academic department and broad category (STEM, Business, etc.) |
| `Year` | Academic year of the record (2022–2025) |
| `Total_Enrollment` | Total student headcount |
| `Male_Enrollment` / `Female_Enrollment` | Gender-disaggregated enrollment |
| `Faculty_Count` / `Student_Faculty_Ratio` | Faculty size and teaching load |
| `PhD_Students` / `MS_MPhil_Students` / `BS_Students` | Program-level enrollment breakdown |
| `Scholarship_Students` / `International_Students` | Special student categories |
| `Research_Papers_Published` | Annual research output (papers) |
| `Avg_CGPA` | Average student CGPA |
| `Employment_Ratio_Pct` | Graduate employment rate (%) |
| `Dropout_Rate_Pct` | Student dropout percentage |
| `Fee_Per_Semester_PKR` | Tuition fee per semester in PKR |
| `Lab_Count` / `No_of_Buildings` | Physical infrastructure metrics |
| `Industry_Tie_Ups` | Number of industry partnerships |
| `Entry_Test_Required` / `Entry_Test_Type` / `Entry_Test_Tier` | Admission test details and selectivity tier |
| `Entry_Test_Passing_Criteria` | Minimum score/percentage to pass entry test |
| `Avg_Student_Background` | Socioeconomic profile of the student body |
 
---
 
## 🔬 Analysis Pipeline
 
### 1. Data Loading & Inspection
 
**15 structured inspection steps** covering:
 
| Step | Description |
|------|-------------|
| 1 | Load and display raw shape |
| 2 | Column names and data types |
| 3 | First and last 5 rows |
| 4 | Missing value counts and percentages |
| 5 | Null coverage heatmap |
| 6 | Statistical summary (describe) for numeric columns |
| 7 | Unique value counts per categorical column |
| 8 | Cardinality assessment |
| 9 | Memory usage per column and total |
| 10 | Duplicate row detection |
| 11 | Index profiling |
| 12 | Value distribution for key categoricals |
| 13 | Outlier detection via IQR |
| 14 | Correlation matrix for numeric features |
| 15 | Year-over-year record count by university |
 
---
 
### 2. Data Cleaning
 
An **8-step, audit-traceable cleaning pipeline** that produces `pakistan_universities_dataset_clean.csv` with **zero structural missing values** and **16 new imputation flag columns**.
 
| Step | Action |
|------|--------|
| **1** | Replace disguised nulls (`'N/A'`, `'na'`, `'unknown'`, `''`, `'none'`) with `pd.NA` |
| **2** | Create 16 boolean `_is_imputed` flag columns **before** any filling (preserves transparency) |
| **3** | Clean `HEC_Ranking` — strip decimal points, coerce to integer, map zeros to `'None'` |
| **4** | Numeric imputation using **university-specific medians**, with fallback to global median |
| **5** | Logically reconstruct `BS_Students`, `PhD_Students`, `MS_MPhil_Students` from `Total_Enrollment` where missing |
| **6** | Categorical imputation using **province-level mode** (reduces urban-centre dominance bias) |
| **7** | Strip leading/trailing whitespace from all `object`-type columns |
| **8** | Downcast numeric dtypes for memory efficiency; convert 12 text columns to `category` dtype |
 
**Key outcomes:**
- 0 structural missing values remaining in the clean dataset
- 16 boolean audit-flag columns track every imputation decision
- Dataset grows from 34 → 50 columns
---
 
### 3. Grouping & Aggregations
 
**10 analytical questions** answered via grouped aggregations:
 
| # | Question |
|---|----------|
| Q1 | Which HEC category ranks highest by average student CGPA? |
| Q2 | How many universities exist per province? |
| Q3 | What is the total research output by department category? |
| Q4 | What is the median fee per semester — Public vs. Private? |
| Q5 | Top 5 cities by graduate employment ratio (minimum 3 universities per city) |
| Q6 | Dropout rates by province — overall AND broken down by Public vs. Private |
| Q7 | Does entry test difficulty tier correlate with CGPA and employment outcomes? |
| Q8 | Province × Department summary for enrollments exceeding 50,000 |
| Q9 | Which universities exceed their provincial female enrollment share baseline? |
| Q10 | Which department category produced the most research papers per year (2022–2025)? |
 
---
 
### 4. Feature Engineering
 
**14 new engineered features** added to produce `pakistan_universities_dataset_enhanced.csv` (50 → 64 columns):
 
| Feature | Formula / Logic | Insight |
|---------|----------------|---------|
| `Female_Share_Pct` | `Female_Enrollment / Total_Enrollment × 100` | Gender parity metric |
| `Gender_Balance_Category` | Buckets: Male Dominated / Balanced / Female Dominated | Categorical representation |
| `Annual_Fee_PKR` | `Fee_Per_Semester_PKR × 2` | Comparable annual cost |
| `Fee_Band` | Percentile-based: Low / Mid / High | Relative affordability tier |
| `Research_Per_Faculty` | `Research_Papers_Published / Faculty_Count` | Faculty research productivity |
| `Campus_Density` | `Total_Enrollment / No_of_Buildings` | Physical crowding proxy |
| `Is_Overcrowded` | `1` if Campus Density > 1.5× national median | Infrastructure stress flag |
| `PG_Ratio` | `(MS_MPhil + PhD) / Total_Enrollment × 100` | Postgraduate concentration |
| `Is_Research_Focused` | `1` if PG Ratio > 30% AND Research/Faculty > national median | Research intensity flag |
| `Selectivity_Score` | Entry test tier (50%) + normalised CGPA (50%) → range 0–3 | Admission competitiveness |
| `University_Score` | Employment (35%) + Research/Faculty (25%) + CGPA (25%) + Industry Tie-Ups (15%) | Composite quality index |
| `Fee_Value_Score` | `Employment_Ratio_Pct / Annual_Fee_PKR × 100,000` | Return on tuition investment |
| `Peer_CGPA_Gap` | University CGPA minus Province × HEC Category group mean | Academic peer comparison |
| `Risk_Index` | Equal-weighted average of: dropout rate + student-faculty ratio + (1 − female share) → range 0–1 | Institutional vulnerability score |
 
---
 
## 🖥️ Streamlit Dashboard
 
An interactive web dashboard built with **Streamlit + Plotly**, featuring a white-and-blue themed UI with a gradient sidebar. The dashboard has **6 pages**:
 
| Page | Contents |
|------|----------|
| 🏠 **Home** | KPI cards (total universities, total enrollment, avg CGPA, total research papers), column overview table, raw data snapshot |
| 📂 **Dataset Viewer** | Filterable table views for raw/clean datasets; side-by-side column comparison with dtype and null info |
| 🔍 **Inspection** | All 15 inspection steps as interactive collapsible expanders with live output |
| 🧹 **Cleaning** | Step-by-step cleaning pipeline breakdown; before/after missing value metrics; imputation flag explorer |
| 📊 **Grouping & Aggregations** | All 10 analytical questions with sortable live tables and Plotly charts |
| ⚙️ **Feature Engineering** | All 14 engineered features with per-feature distribution summaries and top/bottom university rankings |
 
### Dashboard Preview
 
```
Sidebar Navigation          Main Content Area
─────────────────────       ─────────────────────────────────────────
🎓 Pakistani Universities   📊 [KPI Cards] [KPI Cards] [KPI Cards]
─────────────────────       
○ Home                      ┌──────────────────────────────────────┐
○ Dataset Viewer            │  Total        Total       Avg CGPA   │
○ Inspection                │  Universities Enrollment             │
○ Cleaning                  │  91           2,584 rows  3.xx       │
○ Grouping & Aggregations   └──────────────────────────────────────┘
○ Feature Engineering       
                            [Column Overview Table] [Data Snapshot]
```
 
---
 
## 📌 Key Findings
 
- **Entry test selectivity** positively correlates with both CGPA and graduate employment outcomes — more competitive institutions produce better-prepared graduates.
- **Province-level mode imputation** was deliberately chosen for categorical student background data to avoid over-representing urban universities and their characteristics.
- **Logical arithmetic constraints** were applied when reconstructing enrollment sub-groups (BS, MS, PhD) to preserve internal consistency and prevent sub-group sums from exceeding total enrollment.
- **The composite `University_Score`** (employment 35% + research 25% + CGPA 25% + industry ties 15%) provides a holistic, multi-dimensional view of institutional quality that no single metric captures alone.
- **The `Risk_Index`** (dropout + student-faculty ratio + gender imbalance) identifies which institutions are most vulnerable — often smaller, underfunded private universities in less urbanised provinces.
- **Research output is heavily skewed** — a small number of well-ranked, research-focused universities account for a disproportionate share of total published papers.
- **Dropout rates vary significantly by province**, with some public universities in underserved regions showing elevated rates despite lower fees, suggesting non-financial barriers to retention.
- **Fee Value Score** (`Employment / Annual Fee`) surfaces cost-efficient public universities that deliver strong employment outcomes relative to their tuition, which may not appear in traditional rankings.
---
 
## 📦 Requirements & Installation
 
### Python Dependencies
 
```
pandas
numpy
streamlit
plotly
jupyter
```
 
Install all dependencies at once:
 
```bash
pip install pandas numpy streamlit plotly jupyter
```
 
### Versions (recommended)
 
| Package | Minimum Version |
|---------|----------------|
| Python | 3.8+ |
| pandas | 1.3+ |
| numpy | 1.21+ |
| streamlit | 1.20+ |
| plotly | 5.0+ |
 
---
 
## 🚀 Running the Project
 
### Option 1 — Jupyter Notebook (Full EDA Pipeline)
 
```bash
jupyter notebook EDA_of_Pakistani_Universities.ipynb
```
 
Run all cells in sequence. The notebook auto-saves intermediate outputs to the clean and enhanced CSV files.
 
### Option 2 — Streamlit Dashboard
 
Ensure all three CSV files are in the **same directory** as `dashboard.py`, then run:
 
```bash
streamlit run dashboard.py
```
 
The dashboard will open automatically at `http://localhost:8501` in your browser.
 
### Directory Setup
 
Before running, confirm your working directory looks like this:
 
```
your-folder/
├── dashboard.py
├── pakistan_universities_dataset.csv
├── pakistan_universities_dataset_clean.csv
└── pakistan_universities_dataset_enhanced.csv
```
 
> ⚠️ **Note:** The dashboard requires **all three CSV files** to be present. The raw file powers the Inspection and Dataset Viewer pages, while the clean and enhanced files power the Cleaning, Aggregations, and Feature Engineering pages.
 
---
 
## 🗂️ Data Versioning Summary
 
| File | Rows | Columns | Description |
|------|------|---------|-------------|
| `pakistan_universities_dataset.csv` | 2,584 | 34 | Raw data — as-collected, with missing values and disguised nulls |
| `pakistan_universities_dataset_clean.csv` | 2,584 | 50 | After 8-step cleaning — 0 structural nulls, 16 imputation flags added |
| `pakistan_universities_dataset_enhanced.csv` | 2,584 | 64 | After feature engineering — 14 derived features added on top of clean |
 
---
 
## 📄 License
 
This project is intended for educational and research purposes. The dataset covers publicly available information about Pakistani higher education institutions.
 
---
 
*Built with Python · pandas · NumPy · Streamlit · Plotly · Jupyter*