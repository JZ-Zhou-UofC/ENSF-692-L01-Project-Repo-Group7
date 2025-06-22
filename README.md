# ENSF-692 Data Analysis Project

# We are Group7

## Authors

- John Zhou
- Jack Shenfield

## Demo

## Project Overview

This project analyzes Canadian interprovincial migration, housing, employment, and economic trends, inspired by the article:

> "Seeking affordability, young families flee Canada's big cities for cheaper options" by John Macfarlane ([Yahoo Finance](https://ca.finance.yahoo.com/news/seeking-affordability-young-families-flee-canadas-big-cities-for-cheaper-options-192548346.html))

The codebase processes and analyzes multiple public datasets to:

- Clean and prepare raw data from various sources
- Perform data analysis and generate insights
- Provide an interactive CLI for exploring trends

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone git@github.com:JZ-Zhou-UofC/ENSF-692-L01-Project-Repo-Group7.git
   cd ENSF-692-L01-Project-Repo-Group7
   ```

2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Run Cleaning Scripts

The raw data is too big(GB size) and can not be uploaded to github. So we made scripts to clean each file and saved them in the data folder.
Each script in the `scripts/` directory processes a specific raw data file and outputs a cleaned version.

Example (run each as needed):

```bash
python -m scripts.clean_wage_data
python -m scripts.clean_interprovincial_migration_data.py
```

## Running the Project

### 1. Run the Main CLI Application

This will process the data and launch an interactive command-line interface:

```bash
python main.py
```

- The CLI will guide you through data exploration, analysis, and visualizations.

## Requirements

- Python 3.9+
- See `requirements.txt` for package versions:
  - pandas
  - numpy
  - matplotlib
