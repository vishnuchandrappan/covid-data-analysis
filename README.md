# COVID-19 Data Analysis and Visualization

This project focuses on analyzing and visualizing COVID-19 data using Python for data cleaning and Tableau for interactive dashboards. The goal is to derive meaningful insights from the data and present them in an accessible and interactive format.

## Project Structure

- **`data/`**: Contains the raw and cleaned datasets.
  - `covid-data.csv`: Raw dataset.
  - `covid-data-cleaned.csv`: Cleaned dataset (generated after running the cleaning script).
- **`clean_data.py`**: Python script for cleaning and preprocessing the dataset.
- **`pyproject.toml`**: Poetry configuration file for managing dependencies.
- **`poetry.lock`**: Lock file for dependency versions.
- **`README.md`**: Project documentation.

## Steps to Run the Project

1. **Set Up the Environment**:

   - Ensure you have Python 3.9 or higher installed.
   - Install Poetry by following the [official guide](https://python-poetry.org/docs/#installation).
   - Run `poetry install` to install dependencies and set up the environment.

2. **Activate the Virtual Environment**:

   - Run `poetry shell` to activate the virtual environment.

3. **Clean the Data**:

   - Execute the cleaning script by running:
     ```bash
     python clean_data.py
     ```
   - This will generate a cleaned dataset at `data/covid-data-cleaned.csv`.

4. **Visualize the Data**:
   - Open Tableau Desktop.
   - Connect to the cleaned dataset (`data/covid-data-cleaned.csv`).
   - Create visualizations and dashboards to explore the data.

## Key Features

- **Data Cleaning**:

  - Handles missing values.
  - Standardizes column names.
  - Creates calculated fields (e.g., death rate).

- **Interactive Dashboards**:
  - Visualize global COVID-19 trends.
  - Analyze cases and deaths by region and country.
  - Explore time-series and geographic data.

## Dependencies

- `pandas`: For data cleaning and preprocessing.
- `pytest`: For testing (development dependency).

## Dataset

The dataset is sourced from the World Health Organization (WHO) and contains information on COVID-19 cases and deaths globally.

## License

This project is for educational purposes only. The dataset is publicly available and belongs to the respective data provider.
