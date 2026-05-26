# 🎓 EDA of Pakistani Universities
 
An end-to-end Exploratory Data Analysis project on Pakistan's higher education landscape — covering data inspection, cleaning, aggregation, feature engineering, and an interactive Streamlit dashboard.
 
---
 
## 📁 Project Structure
 
```
├── pakistan_universities_dataset.csv         # Raw dataset (2,584 rows × 34 columns)
├── pakistan_universities_dataset_clean.csv   # Cleaned dataset (2,584 rows × 50 columns)
├── pakistan_universities_dataset_enhanced.csv# Feature-engineered dataset (2,584 rows × 64 columns)
├── EDA_of_Pakistani_Universities.ipynb       # Jupyter Notebook — full EDA pipeline
└── dashboard.py                              # Streamlit interactive dashboard
```
 
---
 
## 📊 Dataset Overview
 
| Property | Value |
|---|---|
| Source | Pakistani universities (multi-year, department-level) |
| Raw Shape | 2,584 rows × 34 columns |
| Universities | Multiple institutions across all provinces |
| Provinces | Across Pakistan including AJK, Punjab, Sindh, KPK, Balochistan, and others |
 
### Key Columns
 
| Column | Description |
|---|---|
| `UNI_ID` / `UNI_Name` | University identifier and name |
| `Type` | Public or Private |
| `Province` / `City` | Geographic location |
| `HEC_Ranking` / `HEC_Category` | Higher Education Commission ranking and tier |
| `Total_Enrollment` | Total student count |
| `Male_Enrollment` / `Female_Enrollment` | Gender-disaggregated enrollment |
| `Faculty_Count` / `Student_Faculty_Ratio` | Faculty metrics |
| `PhD_Students` / `MS_MPhil_Students` / `BS_Students` | Program-level enrollment |
| `Research_Papers_Published` | Annual research output |
| `Avg_CGPA` | Average student CGPA |
| `Employment_Ratio_Pct` | Graduate employment rate |
| `Dropout_Rate_Pct` | Student dropout percentage |
| `Fee_Per_Semester_PKR` | Tuition fee per semester |
| `Entry_Test_Required` / `Entry_Test_Tier` | Admission selectivity |
 
---
 
## 🔬 Analysis Pipeline
 
### 1. Loading & Inspection (`EDA_of_Pakistani_Universities.ipynb`)
 
15 structured inspection steps including shape analysis, data types, null coverage, memory usage, statistical summaries, and index profiling.
 
### 2. Data Cleaning (8-Step Pipeline)
 
| Step | Action |
|---|---|
| 1 | Replace disguised nulls (`'N/A'`, `'na'`, `'unknown'`, `''`) with `pd.NA` |
| 2 | Create 16 boolean `_is_imputed` flag columns before any filling |
| 3 | Clean `HEC_Ranking` — strip decimals, coerce to int, map zeros to `'None'` |
| 4 | Numeric imputation via university-specific medians, fallback to global median |
| 5 | Logically reconstruct `BS_Students`, `PhD_Students`, `MS_MPhil_Students` from `Total_Enrollment` |
| 6 | Categorical imputation using province-level mode (reduces urban bias) |
| 7 | Strip whitespace from all object-type columns |
| 8 | Downcast numeric dtypes and convert 12 text columns to `category` dtype |
 
**Result:** 0 structural missing values remaining; 16 new audit flag columns added.
 
### 3. Grouping & Aggregations (10 Questions)
 
| # | Question |
|---|---|
| Q1 | HEC category ranking by average CGPA |
| Q2 | Number of universities by province |
| Q3 | Total research papers by department category |
| Q4 | Median fee per semester by university type |
| Q5 | Top 5 cities by employment ratio (min. 3 universities) |
| Q6 | Dropout rates by province — overall and public/private breakdown |
| Q7 | Average CGPA and employment by entry test difficulty tier |
| Q8 | Province × department summary for enrollments > 50,000 |
| Q9 | Universities exceeding their provincial female share baseline |
| Q10 | Top research department category per year |
 
### 4. Feature Engineering (14 New Features)
 
| Feature | Description |
|---|---|
| `Female_Share_Pct` | Female enrollment as % of total |
| `Gender_Balance_Category` | Male Dominated / Balanced / Female Dominated |
| `Annual_Fee_PKR` | Semester fee × 2 |
| `Fee_Band` | Percentile-based Low / Mid / High bands |
| `Research_Per_Faculty` | Research papers ÷ faculty count |
| `Campus_Density` | Total enrollment ÷ number of buildings |
| `Is_Overcrowded` | 1 if campus density > 1.5× national median |
| `PG_Ratio` | % of students in MS/MPhil or PhD programs |
| `Is_Research_Focused` | 1 if PG Ratio > 30% AND research/faculty > national median |
| `Selectivity_Score` | Entry test tier (50%) + normalised CGPA (50%), range 0–3 |
| `University_Score` | Weighted composite: Employment (35%) + Research/Faculty (25%) + CGPA (25%) + Industry Tie-Ups (15%) |
| `Fee_Value_Score` | Employment ratio ÷ annual fee × 100,000 |
| `Peer_CGPA_Gap` | University CGPA minus Province × HEC Category group mean |
| `Risk_Index` | Equal-weighted: dropout rate + student-faculty ratio + inverted female share, range 0–1 |
 
---
 
## 🖥️ Streamlit Dashboard
 
An interactive web dashboard with 6 pages:
 
| Page | Contents |
|---|---|
| 🏠 Home | KPI cards (universities, enrollment, CGPA, research), column overview, data snapshot |
| 📂 Dataset Viewer | Filterable raw/clean table views with side-by-side column comparison |
| 🔍 Inspection | All 15 inspection steps as interactive expanders |
| 🧹 Cleaning | Pipeline steps, before/after missing value metrics, imputation flag explorer |
| 📊 Grouping & Aggregations | All 10 analytical questions with live tables |
| ⚙️ Feature Engineering | All 14 engineered features with per-feature summaries and top-university rankings |
 
### Running the Dashboard
 
```bash
pip install streamlit pandas numpy
streamlit run dashboard.py
```
 
Make sure all three CSV files are in the same directory as `dashboard.py`.
 
---
 
## 🛠️ Requirements
 
```
pandas
numpy
streamlit
jupyter
```
 
---
 
## 📌 Key Findings
 
- Entry test selectivity correlates positively with both CGPA and graduate employment outcomes.
- Province-level mode imputation was used for student background to avoid urban dominance bias.
- Logical arithmetic constraints were applied to preserve internal consistency across enrollment sub-groups.
- The composite `University_Score` and `Risk_Index` provide a holistic view of institutional quality and vulnerability.