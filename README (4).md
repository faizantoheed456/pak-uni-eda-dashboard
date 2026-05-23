# 🎓 Pakistan Universities — Exploratory Data Analysis

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

---

## 👤 Author

**Faizan Toheed**
Solo data analyst working through every phase of this project from raw inspection to rich visualization — independently, methodically, and with a genuine curiosity about Pakistan's university ecosystem.

---

## 📌 Project Overview

This project is a **structured, multi-session exploratory data analysis** of Pakistani universities. The dataset captures a wide range of institutional metrics — enrollment figures, faculty ratios, HEC rankings, research output, dropout rates, fee structures, and more — across universities in all major provinces.

The goal is to understand patterns, expose inconsistencies, engineer useful features, and ultimately tell a data-driven story about higher education in Pakistan.

---

## 📂 Repository Structure

```
pakistan-universities-eda/
│
├── 📓 Session_1_Loading_and_Inspection.ipynb   ← Current: Initial pipeline phase
├── 📊 dashboard.py                              ← Streamlit interactive dashboard
├── 📄 pakistan_universities_dataset.csv         ← Core dataset (2,584 rows × 34 cols)
└── 📋 README.md                                 ← You are here
```

---

## 📊 Dataset at a Glance

| Property               | Value                                      |
|------------------------|--------------------------------------------|
| **Total Records**      | 2,584 rows                                 |
| **Total Features**     | 34 columns                                 |
| **Numerical Features** | 22                                         |
| **Categorical Features** | 12                                       |
| **Coverage**           | Multiple provinces across Pakistan         |
| **Time Dimension**     | Multi-year longitudinal tracking (`Year`)  |

### 🗂️ Feature Inventory

| Column | Type | Description |
|---|---|---|
| `UNI_ID` | String | Unique university identifier |
| `UNI_Name` | String | Full university name |
| `Type` | String | Public / Private |
| `Province` | String | Province of location |
| `City` | String | City of operation |
| `Established_Year` | Integer | Year of establishment |
| `HEC_Ranking` | Float | HEC national ranking |
| `HEC_Category` | String | HEC category (W, X, Y, Z) |
| `Department_Name` | String | Department name |
| `Department_Category` | String | Broad field classification |
| `Year` | Integer | Academic year of record |
| `Total_Enrollment` | Integer | Total enrolled students |
| `Male_Enrollment` | Integer | Male student count |
| `Female_Enrollment` | Integer | Female student count |
| `Faculty_Count` | Integer | Number of faculty members |
| `Student_Faculty_Ratio` | Float | Students per faculty member |
| `PhD_Students` | Float | PhD-enrolled students |
| `MS_MPhil_Students` | Float | MS/MPhil enrolled students |
| `BS_Students` | Float | BS enrolled students |
| `Scholarship_Students` | Float | Students on scholarship |
| `International_Students` | Float | International student count |
| `Research_Papers_Published` | Integer | Annual research output |
| `Avg_CGPA` | Float | Average student CGPA |
| `Employment_Ratio_Pct` | Float | Graduate employment rate (%) |
| `Dropout_Rate_Pct` | Float | Dropout rate (%) |
| `Avg_Student_Background` | String | Avg student socioeconomic background |
| `Fee_Per_Semester_PKR` | Float | Fee per semester (PKR) |
| `Lab_Count` | Float | Number of labs |
| `Industry_Tie_Ups` | Float | Industry partnerships count |
| `Entry_Test_Required` | String | Whether entry test is required |
| `Entry_Test_Type` | String | Type of entry test |
| `Entry_Test_Tier` | String | Tier classification of entry test |
| `Entry_Test_Passing_Criteria` | String | Minimum passing criteria |
| `No_of_Buildings` | Float | Number of campus buildings |

---

## 🗺️ Project Roadmap

```
Phase 1 ✅  →  Phase 2 🔜  →  Phase 3 🔜  →  Phase 4 🔜  →  Phase 5 🔜
```

### ✅ Session 1 — Loading & Inspection *(Completed)*
> Notebook: `Session_1_Loading_and_Inspection.ipynb`

- Loaded and previewed first 10 and last 15 rows of the dataset
- Extracted structural dimensions: shape, dtypes, column inventory
- Built a completeness profile — populated vs. missing rows per feature
- Generated descriptive statistics across all numerical columns
- Computed mean total enrollment across all Pakistani universities
- Identified the most unique-cardinality column
- Calculated memory footprint of the loaded DataFrame
- Inspected the DataFrame index range and dtype
- Enumerated all columns containing null values and their counts
- Extracted a corner slice: first 3 rows × last 3 columns

---

### 🔜 Session 2 — Data Cleaning *(Upcoming)*

- Handle missing values (imputation strategies per column type)
- Remove or flag duplicate records
- Standardise inconsistent categorical labels
- Fix data type mismatches
- Detect and treat outliers in numerical columns
- Validate logical constraints (e.g., Male + Female ≤ Total Enrollment)

---

### 🔜 Session 3 — Grouping & Aggregations *(Upcoming)*

- Enrollment trends by Province, City, and University Type
- HEC category-wise averages (research output, dropout rate, CGPA)
- Department-level aggregations across all universities
- Year-over-year longitudinal comparisons
- Public vs. Private university metrics comparison

---

### 🔜 Session 4 — Feature Engineering *(Upcoming)*

- Derive `Gender_Ratio` from Male and Female enrollment
- Compute `Research_Output_Per_Faculty`
- Create `Fee_Tier` classification from `Fee_Per_Semester_PKR`
- Engineer `Enrollment_Growth_Rate` from yearly longitudinal data
- Build composite `University_Performance_Score`
- Extract `University_Age` from `Established_Year`

---

### 🔜 Session 5 — Visualization *(Upcoming)*

Using **Matplotlib**, **Seaborn**, and **Plotly** for:

- Distribution plots of key numerical features
- Province-wise and city-wise enrollment heatmaps
- Correlation matrix and pairplots
- HEC Ranking vs. Research Output scatter analysis
- Dropout Rate trends over time (line charts)
- Interactive Plotly dashboards for provincial comparisons
- Fee structure analysis across public vs. private institutions

---

## 🖥️ Interactive Dashboard

An interactive **Streamlit** dashboard (`dashboard.py`) runs alongside the notebooks for live visual inspection of the dataset pipeline.

### Running the Dashboard

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/pakistan-universities-eda.git
cd pakistan-universities-eda

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the dashboard
streamlit run dashboard.py
```

### Dashboard Features

| Panel | Contents |
|---|---|
| **Welcome Panel** | Project overview and navigation guide |
| **Loading & Inspection** | First/last rows, dtype layout, null profile, descriptive stats, structural insights |

> More panels will be added as each session is completed.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.10+** | Core language |
| **Pandas** | Data loading, inspection, cleaning, grouping |
| **NumPy** | Numerical operations |
| **Matplotlib** | Static visualizations *(upcoming)* |
| **Seaborn** | Statistical visualizations *(upcoming)* |
| **Plotly** | Interactive visualizations *(upcoming)* |
| **Streamlit** | Interactive dashboard |
| **Jupyter Notebook** | Session-based analysis pipeline |

---

## ⚙️ Setup & Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/pakistan-universities-eda.git
cd pakistan-universities-eda

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install all dependencies
pip install -r requirements.txt
```

### `requirements.txt`

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

## 🔍 Key Preliminary Findings *(Session 1)*

- The dataset spans **2,584 records** across **34 features**, offering a longitudinally rich view of Pakistani higher education.
- The mean total enrollment across all universities is approximately captured in the `Total_Enrollment` column — skewed by high-enrollment public institutions.
- Several columns contain **missing values**, with nulls concentrated in capacity-related features like `Lab_Count`, `Industry_Tie_Ups`, `PhD_Students`, and `No_of_Buildings`.
- The column with the **highest unique cardinality** is `UNI_Name`, reflecting the diversity of institutions in the dataset.
- The dataset's **memory footprint** is lightweight, making it efficient for in-memory pandas operations.

---

## 📈 Progress Tracker

| Session | Topic | Status |
|---|---|---|
| Session 1 | Loading & Inspection | ✅ Complete |
| Session 2 | Data Cleaning | 🔜 Upcoming |
| Session 3 | Grouping & Aggregations | 🔜 Upcoming |
| Session 4 | Feature Engineering | 🔜 Upcoming |
| Session 5 | Visualization | 🔜 Upcoming |

---

## 🤝 Contributing

This is currently a **solo project** — built independently by Faizan Toheed as a personal deep-dive into Pakistan's university data. Contributions, suggestions, and feedback are always welcome though. Feel free to open an issue or a pull request.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

<p align="center">
  Made with 🧠 and ☕ by <b>Faizan Toheed</b> — solo, steady, and shipping.
</p>
