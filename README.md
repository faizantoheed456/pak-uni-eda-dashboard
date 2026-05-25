# 🎓 EDA of Pakistani Universities
 
<p align="center">
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
</p>
<p align="center">
  A solo end-to-end EDA project exploring Pakistan's higher education landscape —<br>
  enrollment, faculty, research output, fees, dropout rates, and more.<br><br>
  <b>Author: Faizan Toheed</b>
</p>
---
 
## 📁 Repository Structure
 
```
pakistan-universities-eda/
├── EDA_of_Pakistani_Universities.ipynb       ← Analysis notebook
├── dashboard.py                              ← Streamlit dashboard
├── pakistan_universities_dataset.csv         ← Raw dataset
├── pakistan_universities_dataset_clean.csv   ← Cleaned dataset
└── README.md
```
 
---
 
## 📊 Dataset
 
| | Raw | Cleaned |
|---|---|---|
| Rows | 2,584 | 2,584 |
| Columns | 34 | 50 |
| Missing Values | 5,384 | 452 |
| Universities | 91 | 91 |
| Provinces | 7 (AJK, Balochistan, GB, Islamabad, KPK, Punjab, Sindh) | — |
| Years | 2022 – 2025 | — |
| University Types | Public, Private | — |
 
The 16 extra columns in the cleaned dataset are boolean imputation audit flags (`column_is_imputed`).
 
---
 
## 🗺️ Progress
 
| Session | Topic | Status |
|---|---|---|
| 1 | Loading & Inspection | ✅ Complete |
| 2 | Data Cleaning | ✅ Complete |
| 3 | Grouping & Aggregations | ✅ Complete |
| 4 | Feature Engineering | 🔜 Upcoming |
| 5 | Visualization | 🔜 Upcoming |
 
---
 
## 📓 Notebook Walkthrough
 
### Session 1 — Loading & Inspection
15 structured inspection steps: head/tail rows, shape, dtypes, null profile, descriptive stats, memory usage, unique value counts, numeric vs categorical breakdown, random sampling, and index inspection.
 
### Session 2 — Data Cleaning
An 8-step pipeline applied to the raw dataset:
 
1. Replace disguised nulls (`'N/A'`, `'na'`, `'unknown'`, empty strings) with `pd.NA`
2. Create boolean imputation flag columns before any filling
3. Repair `HEC_Ranking` — strip decimal artifacts, map missing to `'None'`
4. Fill numeric columns via per-university median, falling back to global median
5. Reconstruct `BS_Students`, `PhD_Students`, `MS_MPhil_Students` from `Total_Enrollment`
6. Impute `Avg_Student_Background` with province-level mode to reduce urban bias
7. Strip leading/trailing whitespace from all string columns
8. Downcast numeric dtypes; convert 12 categorical columns to `category`
### Session 3 — Grouping & Aggregations
10 analytical questions on the cleaned data:
 
- HEC category ranking by average CGPA
- University count by province
- Research output by department category
- Median semester fee by university type
- Top 5 cities by employment ratio (min 3 universities)
- Dropout rates by province — overall and split by sector
- CGPA and employment by entry test difficulty tier
- Province × department summary for enrollments above 50,000
- Universities exceeding their provincial female share baseline
- Top research department category per year (2022–2025)
---
 
## 🖥️ Dashboard
 
Interactive Streamlit dashboard with a white and blue theme across five pages:
 
| Page | What's inside |
|---|---|
| Home | KPI cards, project overview, column inventory |
| Dataset Viewer | Filter and explore raw and cleaned datasets; side-by-side column comparison |
| Inspection | All 15 inspection steps as expandable panels |
| Cleaning | Pipeline steps, imputation flag explorer, cleaned data preview |
| Grouping & Aggregations | All 10 analysis questions as interactive tables |
 
### Running locally
 
```bash
# Install dependencies
pip install streamlit pandas numpy
 
# Launch
streamlit run dashboard.py
```
 
> Make sure all four files (both CSVs, the notebook, and `dashboard.py`) are in the same folder.
 
---
 
## 🛠️ Tech Stack
 
`Python 3.10+` · `Pandas` · `NumPy` · `Streamlit` · `Jupyter`  
Matplotlib · Seaborn · Plotly *(planned for Session 5)*
 
---
 
<p align="center">Made with 🧠 and ☕ by <b>Faizan Toheed</b> — solo, steady, and shipping.</p>