
raw
Readme · MD
# 🎓 EDA of Pakistani Universities
 
<p align="center">
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-1.x-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
</p>
<p align="center">
  <b>A structured, solo end-to-end Exploratory Data Analysis on Pakistan's higher education landscape — built session by session, with precision and patience. ☕</b>
</p>
---
 
## 👤 Author
 
**Faizan Toheed**  
Solo data analyst working through every phase of this project independently — from raw dataset inspection to a fully cleaned, analysis-ready pipeline.
 
---
 
## 📌 Project Overview
 
This project is a **multi-session EDA** of Pakistani universities covering institutional metrics like enrollment, faculty ratios, HEC rankings, research output, fee structures, dropout rates, and more — across all major provinces, tracked over multiple years.
 
The pipeline progresses through five phases: loading & inspection → data cleaning → grouping & aggregations → feature engineering → visualization. Each phase is a dedicated notebook section with a companion **Streamlit dashboard** for interactive exploration.
 
---
 
## 📂 Repository Structure
 
```
pakistan-universities-eda/
│
├── 📓 EDA_of_Pakistani_Universities.ipynb          ← Main analysis notebook (all sessions)
├── 📊 dashboard.py                                 ← Streamlit interactive dashboard
├── 📄 pakistan_universities_dataset.csv            ← Raw dataset  (2,584 rows × 34 cols)
├── 📄 pakistan_universities_dataset_clean.csv      ← Cleaned dataset (2,584 rows × 50 cols)
└── 📋 README.md                                    ← You are here
```
 
---
 
## 📊 Dataset at a Glance
 
| Property | Raw Dataset | Cleaned Dataset |
|---|---|---|
| **Rows** | 2,584 | 2,584 |
| **Columns** | 34 | 50 (+16 imputation flag cols) |
| **Numerical Features** | 22 | — |
| **Categorical Features** | 12 | — |
| **Missing Values** | Present | Fully resolved |
| **Coverage** | All major provinces of Pakistan | — |
| **Time Dimension** | Multi-year longitudinal (`Year` column) | — |
 
### 🗂️ Feature Inventory (Raw — 34 Columns)
 
| Column | Type | Description |
|---|---|---|
| `UNI_ID` | String | Unique university identifier |
| `UNI_Name` | String | Full university name |
| `Type` | Category | Public / Private |
| `Province` | Category | Province of location |
| `City` | Category | City of operation |
| `Established_Year` | Integer | Year university was established |
| `HEC_Ranking` | Float | HEC national ranking |
| `HEC_Category` | Category | HEC tier (W, X, Y, Z) |
| `Department_Name` | Category | Department name |
| `Department_Category` | Category | Broad academic field |
| `Year` | Integer | Academic year of record |
| `Total_Enrollment` | Integer | Total enrolled students |
| `Male_Enrollment` | Integer | Male student count |
| `Female_Enrollment` | Integer | Female student count |
| `Faculty_Count` | Integer | Number of faculty members |
| `Student_Faculty_Ratio` | Float | Students per faculty member |
| `PhD_Students` | Float | PhD-enrolled students |
| `MS_MPhil_Students` | Float | MS/MPhil enrolled students |
| `BS_Students` | Float | Undergraduate students |
| `Scholarship_Students` | Float | Students on scholarship |
| `International_Students` | Float | International student count |
| `Research_Papers_Published` | Integer | Annual research output |
| `Avg_CGPA` | Float | Average student CGPA |
| `Employment_Ratio_Pct` | Float | Graduate employment rate (%) |
| `Dropout_Rate_Pct` | Float | Dropout rate (%) |
| `Avg_Student_Background` | Category | Average socioeconomic background |
| `Fee_Per_Semester_PKR` | Float | Fee per semester (PKR) |
| `Lab_Count` | Float | Number of labs |
| `Industry_Tie_Ups` | Float | Industry partnerships count |
| `Entry_Test_Required` | Category | Whether entry test is required |
| `Entry_Test_Type` | Category | Type of entry test |
| `Entry_Test_Tier` | Category | Tier classification |
| `Entry_Test_Passing_Criteria` | Category | Minimum passing criteria |
| `No_of_Buildings` | Float | Number of campus buildings |
 
> The **cleaned dataset** adds 16 boolean `_is_imputed` flag columns (one per imputed feature) to maintain full audit transparency.
 
---
 
## 🗺️ Project Roadmap
 
```
Session 1 ✅  →  Session 2 ✅  →  Session 3 🔜  →  Session 4 🔜  →  Session 5 🔜
Inspection      Cleaning        Grouping          Feature Eng.      Visualization
```
 
---
 
### ✅ Session 1 — Loading & Inspection *(Complete)*
 
A 15-step structured pipeline that fully profiles the raw dataset before any transformation.
 
| # | Analysis Task |
|---|---|
| 1 | First 10 rows preview |
| 2 | Dataset shape (rows × columns) |
| 3 | All columns with their data types |
| 4 | Concise structural summary via `.info()` |
| 5 | Descriptive statistics via `.describe()` |
| 6 | Mean total enrollment across all Pakistani universities |
| 7 | Last 15 rows of the dataset |
| 8 | Full column name list |
| 9 | 10 random rows (seeded at `random_state=42`) |
| 10 | Numerical vs. categorical column counts |
| 11 | All columns containing null values |
| 12 | Memory footprint of the DataFrame (in MB) |
| 13 | Column with the highest unique-value cardinality |
| 14 | Corner slice — first 3 rows × last 3 columns |
| 15 | Index range and dtype |
 
---
 
### ✅ Session 2 — Data Cleaning *(Complete)*
 
An 8-step production-grade cleaning pipeline with full imputation audit logging.
 
| # | Cleaning Step | Details |
|---|---|---|
| 1 | **Disguised nulls** | Replaced `'N/A'`, `'na'`, `'unknown'`, `''` with `pd.NA` |
| 2 | **Imputation flag columns** | Created 16 boolean `_is_imputed` columns to log which rows were filled |
| 3 | **HEC Ranking normalisation** | Stripped `.0` float suffixes; mapped missing/zero values to `'None'` string |
| 4 | **Numerical imputation** | University-specific median per `UNI_ID` → global median fallback for 9 columns |
| 5 | **Logical student-level fill** | Derived `BS_Students`, `PhD_Students`, `MS_MPhil_Students` from `Total_Enrollment` arithmetic |
| 6 | **Categorical imputation** | Province-level mode for `Avg_Student_Background` (mitigates urban bias); entry test columns filtered by `Entry_Test_Required` mask |
| 7 | **Text whitespace cleaning** | Stripped leading/trailing whitespace from all string columns |
| 8 | **Memory optimisation** | Downcasted int64/float64 columns; converted 12 low-cardinality text columns to `category` dtype |
 
**Pipeline output:**
- ✅ `0` remaining structural missing values
- ✅ `16` imputation flag columns generated
- ✅ Final shape: `2,584 rows × 50 columns`
- ✅ Exported to `pakistan_universities_dataset_clean.csv`
---
 
### 🔜 Session 3 — Grouping & Aggregations *(Upcoming)*
 
- Enrollment trends by Province, City, and University Type
- HEC category-wise performance averages
- Department-level aggregations across all institutions
- Year-over-year longitudinal comparisons
- Public vs. Private university head-to-head metrics
---
 
### 🔜 Session 4 — Feature Engineering *(Upcoming)*
 
- `Gender_Ratio` — Female / Total Enrollment
- `Research_Output_Per_Faculty` — Research Papers / Faculty Count
- `Fee_Tier` — Binned classification from `Fee_Per_Semester_PKR`
- `Enrollment_Growth_Rate` — Year-on-year percentage change
- `University_Age` — Derived from `Established_Year`
- `University_Performance_Score` — Composite metric across CGPA, Employment, Research
---
 
### 🔜 Session 5 — Visualization *(Upcoming)*
 
Using **Matplotlib**, **Seaborn**, and **Plotly**:
 
- Distribution and box plots for all key numerical features
- Province-wise enrollment heatmaps
- Correlation matrix and pairplots
- HEC Ranking vs. Research Output scatter analysis
- Dropout Rate trends over time
- Interactive Plotly charts for provincial comparisons
- Fee structure breakdown — Public vs. Private
---
 
## 🖥️ Interactive Streamlit Dashboard
 
The dashboard (`dashboard.py`) runs alongside the notebook as a live interactive interface. It has been updated to match both completed sessions.
 
### Dashboard Panels
 
| Panel | Contents |
|---|---|
| 🏠 **Home** | Project overview, dataset summary, pipeline phase status |
| 📂 **Dataset Viewer** | Filterable raw data table by Province and Type, column comparison tool |
| 🔍 **Inspection** | Full 15-step inspection pipeline — dtypes, nulls, stats, memory, index |
| 🧹 **Cleaning** | Cleaning pipeline output — imputation audit, before/after comparisons |
 
### Running the Dashboard
 
```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/pakistan-universities-eda.git
cd pakistan-universities-eda
 
# 2. Install dependencies
pip install -r requirements.txt
 
# 3. Launch
streamlit run dashboard.py
```
 
---
 
## 🛠️ Tech Stack
 
| Tool | Purpose |
|---|---|
| **Python 3.10+** | Core language |
| **Pandas** | Data loading, inspection, cleaning, grouping |
| **NumPy** | Numerical operations and derived calculations |
| **Matplotlib** | Static visualizations *(upcoming)* |
| **Seaborn** | Statistical visualizations *(upcoming)* |
| **Plotly** | Interactive visualizations *(upcoming)* |
| **Streamlit** | Interactive multi-panel dashboard |
| **Jupyter Notebook** | Session-based analysis pipeline |
 
---
 
## ⚙️ Setup & Installation
 
```bash
# Clone
git clone https://github.com/<your-username>/pakistan-universities-eda.git
cd pakistan-universities-eda
 
# (Optional) Virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
 
# Install
pip install -r requirements.txt
```
 
**`requirements.txt`**
```
pandas
numpy
matplotlib
seaborn
plotly
streamlit
jupyter
```
 
---
 
## 📈 Progress Tracker
 
| Session | Topic | Status |
|---|---|---|
| Session 1 | Loading & Inspection | ✅ Complete |
| Session 2 | Data Cleaning | ✅ Complete |
| Session 3 | Grouping & Aggregations | 🔜 Upcoming |
| Session 4 | Feature Engineering | 🔜 Upcoming |
| Session 5 | Visualization | 🔜 Upcoming |
 
---
 
## 📄 License
 
This project is open-source under the [MIT License](LICENSE).
 
---
 
<p align="center">
  Made with 🧠 and ☕ by <b>Faizan Toheed</b> — solo, steady, and shipping.
</p>