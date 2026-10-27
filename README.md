# 🌧️ Measure of Kurtosis – Nagpur Daily Rainfall Analysis

A small statistics project that analyses the **shape of the distribution** of Nagpur's daily rainfall using **kurtosis** and **skewness**.

## What it does
- Loads and cleans the daily rainfall dataset (removes invalid dates, missing and negative values)
- Calculates mean, median, variance, standard deviation, skewness and excess kurtosis
- Interprets the result (Leptokurtic / Platykurtic, positively / negatively skewed)
- Shows an interactive dashboard with a rainfall line chart, histogram and data table

## Project files
| File | Purpose |
|------|---------|
| `app.py` | Streamlit web dashboard |
| `main.py` | Console (terminal) version of the analysis |
| `Nagpur_Daily_Rainfall_Cleaned.csv` | Dataset (`Date`, `Rainfall_mm`) |
| `requirements.txt` | Python libraries needed |

## How to run

1. Install the libraries:
   pip install -r requirements.txt

2. Run the console version:
   python main.py

3. Run the Streamlit dashboard:
   streamlit run app.py

Keep the CSV file in the same folder as `app.py` and `main.py`.

## Tech stack
Python, Pandas, SciPy, Matplotlib, Streamlit

## About kurtosis
Excess kurtosis compares the tails of a distribution with a normal distribution:
- **> 0 (Leptokurtic):** heavier tails, more extreme values
- **< 0 (Platykurtic):** lighter tails, fewer extreme values
- **≈ 0 (Mesokurtic):** similar to a normal distribution
