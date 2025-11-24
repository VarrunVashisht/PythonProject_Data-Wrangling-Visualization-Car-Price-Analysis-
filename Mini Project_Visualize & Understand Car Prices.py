# %% IMPORTS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
plt.rcParams["figure.dpi"] = 100

# %% 1) LOAD DATA
#print("Loading file from:", DATA_PATH)
df = pd.read_csv("raw_data_automotive.csv", header=None)   # file has no header row
print("Loaded. Shape (rows,cols):", df.shape)

# %% 2) ASSIGN COLUMN NAMES
# These are the expected columns for the common 'automobile' dataset
columns = [
    "symboling", "normalized_losses", "make", "fuel_type", "aspiration",
    "num_doors", "body_style", "drive_wheels", "engine_location",
    "wheel_base", "length", "width", "height", "curb_weight",
    "engine_type", "num_cylinders", "engine_size", "fuel_system",
    "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
    "city_mpg", "highway_mpg", "price"
]

# If file has exactly same number of columns, assign directly.
if df.shape[1] == len(columns):
    df.columns = columns
else:
    # If the file has different number of columns, assign only the matching count
    df.columns = columns[:df.shape[1]]
    print("Note: file columns differ from expected. Assigned first", df.shape[1], "names.")

# %% 3) QUICK PEEK
print("\nFirst 6 rows:")
print(df.head(6))
print("\nData types:")
print(df.dtypes)

# %% 4) HANDLE MISSING PLACEHOLDERS
# In many datasets missing values are shown as '?' — convert these to np.nan
df.replace("?", np.nan, inplace=True)
print("\nReplaced '?' with NaN.")

# %% 5) CONVERT NUMERIC COLUMNS
# Columns that should be numeric (if present)
numeric_cols = ["normalized_losses","wheel_base","length","width","height","curb_weight",
                "engine_size","bore","stroke","compression_ratio","horsepower","peak_rpm",
                "city_mpg","highway_mpg","price"]
numeric_cols = [c for c in numeric_cols if c in df.columns]

# Convert using pd.to_numeric (invalid parsing -> NaN)
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# %% 6) CHECK MISSING VALUES BEFORE IMPUTATION
print("\nMissing values per column (before imputation):")
print(df.isna().sum().sort_values(ascending=False).head(10))

# %% 7) IMPUTATION / FILL MISSING VALUES (beginner-friendly choices)
# Numeric: fill NaN with mean (simple approach). Note: median might be better if data is skewed.
for col in numeric_cols:
    if df[col].isna().sum() > 0:
        mean_val = df[col].mean()
        df[col] = df[col].fillna(mean_val)

# Categorical: fill with mode (most common category)
cat_cols = [c for c in ["make","fuel_type","aspiration","num_doors","body_style","drive_wheels",
                       "engine_type","num_cylinders","fuel_system","engine_location"] if c in df.columns]
for col in cat_cols:
    if df[col].isna().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])
print("\nMissing values per column (after imputation):")
print(df.isna().sum().sort_values(ascending=False).head(10))

# %% 8) MAP TEXT DOOR COUNTS TO NUMERIC
door_map = {"two": 2, "four": 4}
if 'num_doors' in df.columns:
    df['num_doors_num'] = df['num_doors'].astype(str).str.lower().map(door_map)
    # If some entries could not be mapped, fill with mode
    if df['num_doors_num'].isna().sum() > 0:
        df['num_doors_num'].fillna(df['num_doors_num'].mode()[0], inplace=True)

# %% 9) QUICK STATISTICS
print("\nNumeric summary (describe):")
print(df[numeric_cols].describe().transpose())

# %% 10) SAVE CLEANED DATA

SAVE_PATH = r"C:\Users\61424\PycharmProjects\PythonProject\Mini Project_Visualize & Understand Car Prices\cleaned_automobile_data.csv"
try:
    df.to_csv(SAVE_PATH, index=False)
    print(f"\nCleaned dataset saved successfully to:\n{SAVE_PATH}")
except Exception as e:
    print("Error while saving file:", e)

# ---------- VISUALIZATIONS ----------
# Helper: small function to show and clear
def show_plot():
    plt.show()
    plt.clf()

# A: Line Plot (simple trend of average price by index or by make)
plt.figure(figsize=(8,4))
# Line of price over row index (not time) — shows overall spread/trend in dataset order
plt.plot(df.index, df['price'], marker='o', linestyle='-', markersize=3)
plt.title("Price over dataset index (trend)")
plt.xlabel("Row index")
plt.ylabel("Price")
show_plot()
# Why: quick sense if prices increase/decrease across the file (not time series). Expectation: no real trend, scattered.

# B: Scatter Plot (horsepower vs price)
plt.figure(figsize=(7,5))
plt.scatter(df['horsepower'], df['price'], alpha=0.7)
plt.title("Horsepower vs Price")
plt.xlabel("Horsepower")
plt.ylabel("Price")
show_plot()
# Why: checks relationship. Observation: generally higher horsepower -> higher price but with wide spread.

# C: Histogram (price distribution)
plt.figure(figsize=(7,5))
plt.hist(df['price'], bins=20, edgecolor='black')
plt.title("Distribution of Car Prices")
plt.xlabel("Price")
plt.ylabel("Count")
show_plot()
# Why: see distribution shape. Observation: likely right-skew (more lower-priced cars, fewer expensive ones).

# D: Bar plot (average price by body_style)
plt.figure(figsize=(8,4))
avg_by_body = df.groupby('body_style')['price'].mean().sort_values()
avg_by_body.plot(kind='bar')
plt.title("Average Price by Body Style")
plt.ylabel("Average Price")
show_plot()
# Why: compare categories. Observation: luxury body styles (convertible) often show higher avg price.

# E: Pcolor (pivot table: make × body_style average price)
pivot = df.pivot_table(values='price', index='make', columns='body_style', aggfunc='mean')
plt.figure(figsize=(10,8))
plt.pcolor(pivot.fillna(0))  # pcolor needs numeric; fill nan for visualization
plt.colorbar(label='Avg Price')
plt.yticks(np.arange(0.5, len(pivot.index), 1), pivot.index)
plt.xticks(np.arange(0.5, len(pivot.columns), 1), pivot.columns, rotation=45)
plt.title("Average Price: make × body_style (pcolor)")
show_plot()
# Why: quick heatmap-like view of where expensive combinations are. Observation: certain makes & styles show high price.

# F: Seaborn regression plot (hp vs price)
plt.figure(figsize=(7,5))
sns.regplot(x='horsepower', y='price', data=df, scatter_kws={'alpha':0.6})
plt.title("Regression: Horsepower vs Price")
show_plot()
# Why: adds regression line and 95% CI to quantify linear relationship. Observation: positive slope but wide CI.

# G: Boxplot (price per body_style)
plt.figure(figsize=(8,5))
sns.boxplot(x='body_style', y='price', data=df)
plt.title("Price Distribution by Body Style (boxplot)")
plt.xticks(rotation=45)
show_plot()
# Why: shows median, IQR, outliers