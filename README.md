🎓 EDA of Pakistani Universities
<p align="center">
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
</p>

A solo end-to-end EDA project exploring Pakistan's higher education landscape — enrollment, faculty, research output, fees, and more. Built with precision, patience, and a lot of chai ☕

Author: Faizan Toheed

📁 Files
FileDescriptionEDA_of_Pakistani_Universities.ipynbCore analysis notebookdashboard.pyStreamlit interactive dashboardpakistan_universities_dataset.csvRaw dataset — 2,584 rows × 34 colspakistan_universities_dataset_clean.csvCleaned dataset — 2,584 rows × 50 cols

📊 Dataset

91 universities across 7 provinces
34 features covering enrollment, faculty, HEC ranking, research, fees, dropout rates, and entry tests
Multi-year longitudinal records (Year column)
After cleaning: 50 columns with 16 imputation audit flag columns added


🗺️ Progress
SessionTopicStatus1Loading & Inspection✅ Complete2Data Cleaning✅ Complete3Grouping & Aggregations🔜 Upcoming4Feature Engineering🔜 Upcoming5Visualization🔜 Upcoming
Session 1 — Loading & Inspection
Covered shape, dtypes, null profile, descriptive stats, memory usage, unique value counts, random sampling, and index inspection across all 34 columns.
Session 2 — Data Cleaning
An 8-step pipeline: replaced disguised nulls, created imputation audit flags, repaired HEC_Ranking, filled numeric columns via per-university medians, reconstructed enrollment sub-columns logically, applied regional mode imputation for categorical fields, stripped whitespace, and downcast types to category/smaller numerics.
Result: 0 structural missing values. Exported as pakistan_universities_dataset_clean.csv.

🖥️ Dashboard
A Streamlit dashboard with a white + blue theme and four pages:

Home — KPI cards, project overview, column inventory
Dataset Viewer — Explore raw and cleaned datasets with filters
Inspection — All 15 inspection steps as interactive expandable panels
Cleaning — Pipeline steps, imputation flag explorer, cleaned data preview

bashpip install -r requirements.txt
streamlit run dashboard.py

🛠️ Stack
Python · Pandas · NumPy · Streamlit · Jupyter · Matplotlib · Seaborn · Plotly (viz upcoming)

<p align="center">Made with 🧠 and ☕ by <b>Faizan Toheed</b></p>