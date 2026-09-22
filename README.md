# Python Data Science Assignment

A hands-on Python Data Science assignment focused on data manipulation
and data visualization using Python, Pandas, NumPy, Matplotlib, Seaborn,
and Jupyter Notebook.

The project is designed to build practical understanding of the basic
data-science workflow:

``` text
Data Ingestion
      ↓
Data Inspection
      ↓
Data Cleaning
      ↓
Data Transformation
      ↓
Data Analysis
      ↓
Data Visualization
      ↓
Output Generation
```

------------------------------------------------------------------------

## 1. Project Objective

The objective of this assignment is to practice fundamental Python
data-science concepts using a sales dataset.

The assignment is divided into two practices.

### Practice 1 --- Data Manipulation with Pandas

The following tasks will be performed:

1.  Load a CSV dataset into a Pandas DataFrame.
2.  Inspect the first five rows.
3.  Inspect the structure and data types of the dataset.
4.  Identify missing values.
5.  Clean missing values by filling a numeric column with its median.
6.  Create a calculated column called `Profit_Margin`.
7.  Use `groupby()` to calculate total `Sales` for each `Region`.
8.  Save the processed data and analytical results.

### Practice 2 --- Data Visualization

The following visualizations will be created:

1.  Histogram of `Sales`.
2.  Box plot showing the distribution of `Profit` across
    `Product Categories`.
3.  Scatter plot showing the relationship between `Sales` and `Profit`.
4.  Customize the scatter plot with:
    -   Axis labels
    -   Title
    -   Product Category-based point coloring

The generated figures will be saved automatically inside the project's
`outputs/figures/` directory.

------------------------------------------------------------------------

## 2. Technology Stack

The project uses:

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn
-   Jupyter Notebook
-   IPython
-   Jupyter Kernel
-   Visual Studio Code
-   Anaconda / Conda

------------------------------------------------------------------------

## 3. Development Environment

A dedicated Conda environment has been created for this project.

### Conda Environment

``` text
Environment Name:
python-data-science
```

Environment location:

``` text
C:\Users\Ashish\anaconda3\envs\python-data-science
```

The project itself is kept separately from the Conda environment.

### Project Location

``` text
C:\Users\Ashish\Desktop\python-data-science-assignment
```

This separation keeps the Python environment and project files
independent.

------------------------------------------------------------------------

## 4. Python Version

The project uses:

``` text
Python 3.14.7
```

The Python version was verified from the active `python-data-science`
Conda environment.

------------------------------------------------------------------------

## 5. Installed Dependencies

The following packages have been installed and verified in the project
environment.

  Package        Version Purpose
  ------------ --------- --------------------------------
  Python          3.14.7 Programming language
  Pandas           3.0.6 Data manipulation and analysis
  NumPy            2.5.2 Numerical computing
  Matplotlib      3.11.2 Data visualization
  Seaborn         0.13.2 Statistical visualization
  Jupyter          1.1.1 Notebook environment
  IPython         9.11.0 Interactive Python
  ipykernel        7.2.0 Jupyter Python kernel

------------------------------------------------------------------------

## 6. Requirements

The project's dependencies are recorded in:

``` text
requirements.txt
```

Current contents:

``` text
pandas==3.0.6
numpy==2.5.2
matplotlib==3.11.2
seaborn==0.13.2
jupyter==1.1.1
ipykernel==7.2.0
```

The requirements file allows the project dependencies to be reproduced
in another Python environment.

To install the recorded dependencies:

``` bash
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

## 7. Development Tools

### Visual Studio Code

Visual Studio Code is used as the main development environment.

Installed extensions include:

-   Python
-   Jupyter
-   Python Debugger
-   Jupyter Renderers
-   Jupyter Cell Tags
-   Jupyter Slideshow

The Python and Jupyter extensions allow Python scripts and Jupyter
notebooks to be developed and executed directly inside VS Code.

------------------------------------------------------------------------

## 8. Jupyter Notebook Environment

Two notebooks are planned for the assignment.

### Pandas Data Manipulation

``` text
notebooks/01_pandas_data_manipulation.ipynb
```

This notebook will contain the data loading, inspection, cleaning,
transformation, and aggregation work.

### Data Visualization

``` text
notebooks/02_data_visualization.ipynb
```

This notebook will contain the Matplotlib and Seaborn visualization
work.

The notebooks will use the dedicated:

``` text
python-data-science
```

Python environment.

------------------------------------------------------------------------

## 9. Project Structure

The project follows this structure:

``` text
python-data-science-assignment/
│
├── data/
│   │
│   ├── raw/
│   │   └── sales_data.csv
│   │
│   └── processed/
│       └── cleaned_sales_data.csv
│
├── notebooks/
│   ├── 01_pandas_data_manipulation.ipynb
│   └── 02_data_visualization.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loading.py
│   ├── data_cleaning.py
│   └── visualization.py
│
├── outputs/
│   │
│   ├── figures/
│   │   ├── sales_histogram.png
│   │   ├── profit_boxplot.png
│   │   └── sales_profit_scatter.png
│   │
│   └── tables/
│       └── sales_by_region.csv
│
├── .gitignore
├── README.md
└── requirements.txt
```

------------------------------------------------------------------------

## 10. Directory Responsibilities

### `data/`

Contains datasets used by the project.

#### `data/raw/`

Stores the original/raw dataset.

``` text
data/raw/sales_data.csv
```

Raw data should remain unchanged so that the original source data is
preserved.

#### `data/processed/`

Stores cleaned or transformed data generated during the analysis.

``` text
data/processed/cleaned_sales_data.csv
```

------------------------------------------------------------------------

### `notebooks/`

Contains the Jupyter Notebooks used for learning and completing the
assignment.

``` text
notebooks/
├── 01_pandas_data_manipulation.ipynb
└── 02_data_visualization.ipynb
```

------------------------------------------------------------------------

### `src/`

Contains reusable Python source code.

#### `data_loading.py`

Responsible for data ingestion and loading the dataset.

#### `data_cleaning.py`

Contains reusable data-cleaning operations.

#### `visualization.py`

Contains reusable visualization functionality.

#### `__init__.py`

Marks the `src` directory as a Python package.

------------------------------------------------------------------------

### `outputs/`

Contains files generated during analysis.

#### `outputs/figures/`

Stores generated visualization images.

Expected figures:

``` text
sales_histogram.png
profit_boxplot.png
sales_profit_scatter.png
```

These files will be generated automatically by the visualization code.

#### `outputs/tables/`

Stores generated analytical tables.

Expected output:

``` text
sales_by_region.csv
```

This file will contain the total sales for each region.

------------------------------------------------------------------------

## 11. Data Processing Workflow

The planned data-processing workflow is:

``` text
Raw CSV
   │
   ▼
Load with Pandas
   │
   ▼
Inspect DataFrame
   │
   ├── First 5 rows
   ├── Data types
   └── Missing values
   │
   ▼
Clean Missing Values
   │
   ▼
Create Profit_Margin
   │
   ▼
Group Sales by Region
   │
   ▼
Save Processed Data
   │
   ▼
Create Visualizations
   │
   ├── Histogram
   ├── Box Plot
   └── Scatter Plot
   │
   ▼
Save Outputs
```

------------------------------------------------------------------------

## 12. Planned Data Columns

The sales dataset will contain fields required for the assignment,
including fields representing:

-   Sales
-   Profit
-   Region
-   Product Category

Additional fields may be available in the dataset and can be used where
appropriate.

The dataset will be stored as:

``` text
data/raw/sales_data.csv
```

------------------------------------------------------------------------

## 13. Data Cleaning

The assignment includes missing-value handling.

The workflow will:

1.  Identify missing values.
2.  Determine an appropriate numeric column containing missing values.
3.  Calculate its median.
4.  Fill the missing numeric values using the median.

Conceptually:

``` text
Missing numeric values
          ↓
Calculate median
          ↓
Replace missing values
          ↓
Clean DataFrame
```

The original raw dataset will remain unchanged.

------------------------------------------------------------------------

## 14. Calculated Column

A new column called:

``` text
Profit_Margin
```

will be created using:

``` text
Profit_Margin = Profit / Sales
```

This creates a derived metric that represents profit relative to sales.

------------------------------------------------------------------------

## 15. GroupBy Analysis

Pandas `groupby()` will be used to calculate total sales for each
region.

Conceptually:

``` text
Region
   ↓
Group records
   ↓
Sum Sales
   ↓
Sales by Region
```

The resulting table will be saved as:

``` text
outputs/tables/sales_by_region.csv
```

------------------------------------------------------------------------

## 16. Visualizations

Three main visualizations will be created.

### Sales Histogram

A Matplotlib histogram will show the distribution of:

``` text
Sales
```

The number of histogram bins will be customized.

Output:

``` text
outputs/figures/sales_histogram.png
```

------------------------------------------------------------------------

### Profit Box Plot

A Seaborn box plot will compare the distribution of:

``` text
Profit
```

across:

``` text
Product Categories
```

Output:

``` text
outputs/figures/profit_boxplot.png
```

------------------------------------------------------------------------

### Sales vs Profit Scatter Plot

A Matplotlib scatter plot will visualize the relationship between:

``` text
Sales
```

and:

``` text
Profit
```

The visualization will include:

-   X-axis label
-   Y-axis label
-   Chart title
-   Product Category-based point coloring

Output:

``` text
outputs/figures/sales_profit_scatter.png
```

------------------------------------------------------------------------

## 17. Generated Output Files

The following files are expected to be generated during the assignment:

``` text
data/
└── processed/
    └── cleaned_sales_data.csv

outputs/
├── figures/
│   ├── sales_histogram.png
│   ├── profit_boxplot.png
│   └── sales_profit_scatter.png
│
└── tables/
    └── sales_by_region.csv
```

These output files are produced by Python code rather than being
manually created.

------------------------------------------------------------------------

## 18. Git

Git is used for version control.

The project contains:

``` text
.gitignore
```

The `.gitignore` file will be used to prevent unnecessary files such as
Python cache files, virtual environment files, temporary files, and
generated artifacts that should not be committed from being tracked by
Git.


------------------------------------------------------------------------

## 20. Learning Approach

The assignment will be completed using a concept-first approach.

For each major concept:

``` text
Understand the concept
        ↓
Simple example
        ↓
Inspect the result
        ↓
Understand what happened
        ↓
Apply it to the assignment
```

The main concepts covered include:

-   Python data-science environment
-   Jupyter Notebook
-   Pandas
-   DataFrames
-   CSV files
-   Data inspection
-   Data types
-   Missing values
-   Median
-   Data cleaning
-   Calculated columns
-   `groupby()`
-   Aggregation
-   Matplotlib
-   Seaborn
-   Histograms
-   Box plots
-   Scatter plots
-   Data visualization customization

------------------------------------------------------------------------

## 21. Project Goal

The final goal is to demonstrate a complete basic data-science workflow
using Python:

``` text
Dataset
   ↓
Pandas DataFrame
   ↓
Data Inspection
   ↓
Data Cleaning
   ↓
Data Transformation
   ↓
Data Aggregation
   ↓
Visualization
   ↓
Saved Analytical Outputs
```

This project focuses on understanding the reasoning behind each step
rather than only producing the final code.
