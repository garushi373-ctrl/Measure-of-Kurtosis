
import pandas as pd
from scipy.stats import kurtosis, skew

# 1. Load dataset
file_path = "Nagpur_Daily_Rainfall_Cleaned.csv"
df = pd.read_csv(file_path)

# 2. Data preprocessing
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Rainfall_mm"] = pd.to_numeric(
    df["Rainfall_mm"], errors="coerce"
)

df = df.dropna(subset=["Date", "Rainfall_mm"])
df = df[df["Rainfall_mm"] >= 0]
df = df.drop_duplicates(subset=["Date"])
df = df.sort_values("Date").reset_index(drop=True)

# 3. Calculate statistics
rainfall = df["Rainfall_mm"]

mean_value = rainfall.mean()
median_value = rainfall.median()
variance_value = rainfall.var()
std_value = rainfall.std()
skewness_value = skew(rainfall, bias=False)
kurtosis_value = kurtosis(rainfall, fisher=True, bias=False)

# 4. Display console output
print("=" * 55)
print("       MEASURE OF KURTOSIS PROJECT")
print("       NAGPUR DAILY RAINFALL ANALYSIS")
print("=" * 55)

print("\n1. DATASET INFORMATION")
print("-" * 35)
print("Total records:", len(df))
print("Columns:", list(df.columns))
print("Start date:", df["Date"].min().date())
print("End date:", df["Date"].max().date())
print("Missing values:\n", df.isnull().sum().to_string())

print("\n2. DESCRIPTIVE STATISTICS")
print("-" * 35)
print(f"Mean rainfall       : {mean_value:.4f} mm")
print(f"Median rainfall     : {median_value:.4f} mm")
print(f"Minimum rainfall    : {rainfall.min():.4f} mm")
print(f"Maximum rainfall    : {rainfall.max():.4f} mm")
print(f"Variance            : {variance_value:.4f} mm²")
print(f"Standard deviation  : {std_value:.4f} mm")

print("\n3. SHAPE OF DISTRIBUTION")
print("-" * 35)
print(f"Skewness             : {skewness_value:.4f}")
print(f"Excess Kurtosis      : {kurtosis_value:.4f}")

if kurtosis_value > 0:
    print("Interpretation       : Leptokurtic")
elif kurtosis_value < 0:
    print("Interpretation       : Platykurtic")
else:
    print("Interpretation       : Mesokurtic-level excess kurtosis")

if skewness_value > 0:
    print("Skewness result      : Positively skewed")
elif skewness_value < 0:
    print("Skewness result      : Negatively skewed")
else:
    print("Skewness result      : Approximately symmetric")

print("\n4. FIRST 10 RECORDS")
print("-" * 35)
print(df.head(10).to_string(index=False))

print("\n" + "=" * 55)
print("           ANALYSIS COMPLETED")
print("=" * 55)
