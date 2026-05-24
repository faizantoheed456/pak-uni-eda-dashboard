🎓 Pakistan Universities — Exploratory Data Analysis
<p align="center">
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
</p>
<p align="center">
  <b>A solo end-to-end EDA project on Pakistan's higher education landscape — built with precision, patience, and a lot of chai ☕</b>
</p>

👤 Author
Faizan Toheed
Solo data analyst working through every phase of this project from raw inspection to rich visualization — independently, methodically, and with a genuine curiosity about Pakistan's university ecosystem.

📌 Project Overview
This project is a structured, multi-session exploratory data analysis of Pakistani universities. The dataset captures a wide range of institutional metrics — enrollment figures, faculty ratios, HEC rankings, research output, dropout rates, fee structures, and more — across universities in all major provinces.
The goal is to understand patterns, expose inconsistencies, engineer useful features, and ultimately tell a data-driven story about higher education in Pakistan.

📂 Repository Structure
pakistan-universities-eda/
│
├── 📓 EDA_of_Pakistani_Universities.ipynb       ← Core analysis notebook (Sessions 1 & 2)
├── 📊 dashboard.py                              ← Streamlit interactive dashboard
├── 📄 pakistan_universities_dataset.csv         ← Raw dataset (2,584 rows × 34 cols)
├── 📄 pakistan_universities_dataset_clean.csv   ← Cleaned dataset (2,584 rows × 50 cols)
└── 📋 README.md                                 ← You are here

📊 Dataset at a Glance
PropertyRaw DatasetCleaned DatasetTotal Records2,584 rows2,584 rowsTotal Features34 columns50 columnsNumerical Features21—Categorical Features13—Universities91 unique91 uniqueProvinces Covered77Time DimensionMulti-year (Year)Multi-year (Year)Imputation Flag Cols—16 audit flag columns
🗂️ Feature Inventory
ColumnTypeDescriptionUNI_IDStringUnique university identifierUNI_NameStringFull university nameTypeStringPublic / PrivateProvinceStringProvince of locationCityStringCity of operationEstablished_YearIntegerYear of establishmentHEC_RankingFloatHEC national rankingHEC_CategoryStringHEC category (W, X, Y, Z)Department_NameStringDepartment nameDepartment_CategoryStringBroad field classificationYearIntegerAcademic year of recordTotal_EnrollmentIntegerTotal enrolled studentsMale_EnrollmentIntegerMale student countFemale_EnrollmentIntegerFemale student countFaculty_CountIntegerNumber of faculty membersStudent_Faculty_RatioFloatStudents per faculty memberPhD_StudentsFloatPhD-enrolled studentsMS_MPhil_StudentsFloatMS/MPhil enrolled studentsBS_StudentsFloatBS enrolled studentsScholarship_StudentsFloatStudents on scholarshipInternational_StudentsFloatInternational student countResearch_Papers_PublishedIntegerAnnual research outputAvg_CGPAFloatAverage student CGPAEmployment_Ratio_PctFloatGraduate employment rate (%)Dropout_Rate_PctFloatDropout rate (%)Avg_Student_BackgroundStringAvg student socioeconomic backgroundFee_Per_Semester_PKRFloatFee per semester (PKR)Lab_CountFloatNumber of labsIndustry_Tie_UpsFloatIndustry partnerships countEntry_Test_RequiredStringWhether entry test is requiredEntry_Test_TypeStringType of entry testEntry_Test_TierStringTier classification of entry testEntry_Test_Passing_CriteriaStringMinimum passing criteriaNo_of_BuildingsFloatNumber of campus buildings

🗺️ Project Roadmap
Phase 1 ✅  →  Phase 2 ✅  →  Phase 3 🔜  →  Phase 4 🔜  →  Phase 5 🔜
✅ Session 1 — Loading & Inspection (Completed)

Notebook: EDA_of_Pakistani_Universities.ipynb


Loaded and previewed first 10 and last 15 rows of the dataset
Extracted structural dimensions: shape, dtypes, column inventory
Built a completeness profile — populated vs. missing rows per feature
Generated descriptive statistics across all numerical columns
Computed mean total enrollment across all Pakistani universities
Identified the most unique-cardinality column (UNI_Name)
Calculated memory footprint of the loaded DataFrame
Inspected the DataFrame index range and dtype
Enumerated all columns containing null values and their counts
Extracted a corner slice: first 3 rows × last 3 columns
Enumerated numeric vs. non-numeric column counts
Drew 10 random sample rows for a quick sanity check


✅ Session 2 — Data Cleaning (Completed)

Notebook: EDA_of_Pakistani_Universities.ipynb

An advanced 8-step production cleaning pipeline was designed and executed:

Disguised Missing Values — Replaced 'N/A', 'na', 'unknown', and empty strings with pd.NA
Imputation Audit Trail — Created 16 boolean flag columns (col_is_imputed) before any filling
HEC_Ranking Repair — Stripped .0 decimal artifacts; mapped zero/missing to 'None'
Numeric Imputation — Filled 9 numeric columns via per-university median, falling back to global median
Logical Enrollment Reconstruction — Recalculated BS_Students, PhD_Students, MS_MPhil_Students from Total_Enrollment arithmetic constraints
Regional Categorical Imputation — Filled Avg_Student_Background with province-level mode to reduce urban bias; entry test fields filled conditionally
Whitespace Cleaning — Stripped all leading/trailing whitespace across object columns
Type Optimisation — Downcast numeric types; converted 12 categorical columns to category dtype

Result: Cleaned dataset exported as pakistan_universities_dataset_clean.csv (50 columns, 0 structural missing values).

🔜 Session 3 — Grouping & Aggregations (Upcoming)

Enrollment trends by Province, City, and University Type
HEC category-wise averages (research output, dropout rate, CGPA)
Department-level aggregations across all universities
Year-over-year longitudinal comparisons
Public vs. Private university metrics comparison


🔜 Session 4 — Feature Engineering (Upcoming)

Derive Gender_Ratio from Male and Female enrollment
Compute Research_Output_Per_Faculty
Create Fee_Tier classification from Fee_Per_Semester_PKR
Engineer Enrollment_Growth_Rate from yearly longitudinal data
Build composite University_Performance_Score
Extract University_Age from Established_Year


🔜 Session 5 — Visualization (Upcoming)
Using Matplotlib, Seaborn, and Plotly for:

Distribution plots of key numerical features
Province-wise and city-wise enrollment heatmaps
Correlation matrix and pairplots
HEC Ranking vs. Research Output scatter analysis
Dropout Rate trends over time (line charts)
Interactive Plotly dashboards for provincial comparisons
Fee structure analysis across public vs. private institutions


🖥️ Interactive Dashboard
An interactive Streamlit dashboard (dashboard.py) provides live visual inspection of the full data pipeline with a clean white + blue theme.
Running the Dashboard
bash# 1. Clone the repository
git clone https://github.com/<your-username>/pakistan-universities-eda.git
cd pakistan-universities-eda

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the dashboard
streamlit run dashboard.py
Dashboard Pages
PageContents🏠 HomeProject title, KPI cards (universities, enrollments, avg CGPA, research papers), project overview, column badge inventory, raw data snapshot📂 Dataset ViewerRaw dataset explorer (filter by Province & Type), Cleaned dataset explorer (column selector), side-by-side column comparison tool🔍 InspectionAll 15 inspection steps rendered interactively — head/tail, shape, dtypes, null profile, descriptive stats, memory usage, unique value counts, index info🧹 CleaningBefore/after missing value metrics, all 8 pipeline steps explained, imputation flag explorer table, cleaned dataset preview

More panels will be added as each session is completed.


🛠️ Tech Stack
ToolPurposePython 3.10+Core languagePandasData loading, inspection, cleaning, groupingNumPyNumerical operationsMatplotlibStatic visualizations (upcoming)SeabornStatistical visualizations (upcoming)PlotlyInteractive visualizations (upcoming)StreamlitInteractive dashboardJupyter NotebookSession-based analysis pipeline

⚙️ Setup & Installation
bash# Clone the repository
git clone https://github.com/<your-username>/pakistan-universities-eda.git
cd pakistan-universities-eda

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install all dependencies
pip install -r requirements.txt
requirements.txt
pandas
numpy
matplotlib
seaborn
plotly
streamlit
jupyter

🔍 Key Findings So Far
Session 1 — Inspection

The dataset spans 2,584 records across 34 features, offering a longitudinally rich view of Pakistani higher education.
The mean total enrollment is skewed upward by high-enrollment public institutions.
Nulls are concentrated in capacity-related features: Lab_Count, Industry_Tie_Ups, PhD_Students, and No_of_Buildings.
The column with the highest unique cardinality is UNI_Name, reflecting 91 distinct institutions.
The dataset's memory footprint is lightweight, making it efficient for in-memory pandas operations.

Session 2 — Cleaning

16 imputation flag columns were added, creating a full audit trail of every filled value.
Enrollment sub-columns (BS, PhD, MS/MPhil) were reconstructed logically from Total_Enrollment — preserving internal arithmetic consistency.
Province-level mode imputation for Avg_Student_Background mitigates urban-centric bias common in Pakistani institutional data.
Final cleaned shape: 2,584 rows × 50 columns with 0 structural missing values.


📈 Progress Tracker
SessionTopicStatusSession 1Loading & Inspection✅ CompleteSession 2Data Cleaning✅ CompleteSession 3Grouping & Aggregations🔜 UpcomingSession 4Feature Engineering🔜 UpcomingSession 5Visualization🔜 Upcoming

🤝 Contributing
This is currently a solo project — built independently by Faizan Toheed as a personal deep-dive into Pakistan's university data. Contributions, suggestions, and feedback are always welcome though. Feel free to open an issue or a pull request.

📄 License
This project is open-source under the MIT License.

<p align="center">
  Made with 🧠 and ☕ by <b>Faizan Toheed</b> — solo, steady, and shipping.
</p>