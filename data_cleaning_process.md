# Data Cleaning Process

This document outlines the steps taken to clean and preprocess the COVID-19 dataset for analysis and visualization.

## Initial Cleaning Steps

1. **Standardized Column Names**:

   - Renamed columns for consistency and easier reference.

2. **Handled Missing Values**:

   - Replaced empty strings with `NaN`.
   - Dropped rows with missing critical data (e.g., `Country`, `Cumulative_Cases`, `Cumulative_Deaths`).

3. **Converted Data Types**:

   - Ensured numeric columns were properly converted to numeric types.

4. **Created Calculated Fields**:
   - Added a `Death_Rate` column to calculate the percentage of deaths relative to cases.

## Additional Cleaning Steps

1. **Removed Invalid or Placeholder Country Names**:

   - Excluded rows with invalid or placeholder country names such as `Global`, `Other`, and international conveyances.

2. **Fixed Encoding Issues**:

   - Corrected encoding issues in country names (e.g., `C�te d'Ivoire` to `Côte d'Ivoire`).

3. **Dropped Unnecessary Columns**:

   - Removed columns that were not useful for analysis (e.g., `New_Cases_24_Hours`, `New_Deaths_24_Hours`).

4. **Handled Outliers**:
   - Applied the Interquartile Range (IQR) method to clip extreme values in `Cases_Per_100k` and `Deaths_Per_100k`.

## Final Output

- The cleaned dataset is saved as `data/covid-data-cleaned.csv`.
- It is now ready for analysis and visualization in Tableau.
