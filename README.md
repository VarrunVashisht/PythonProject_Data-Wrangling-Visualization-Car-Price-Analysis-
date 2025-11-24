# 🚗 Car Price Analysis & Visualization

### *A Beginner-Friendly Data Wrangling & Visualization Project*

---

## 📌 Project Overview

This project is a complete, beginner-friendly walkthrough of loading, cleaning, analyzing, and visualizing real-world automotive data.
The dataset contains car specifications such as engine size, horsepower, fuel type, number of doors, and price.

The goal is to help beginners understand **data wrangling**, **exploratory data analysis (EDA)**, and **Python data visualization** using:

* **Pandas** (data cleaning & transformations)
* **NumPy**
* **Matplotlib**
* **Seaborn**

---

## 🎯 Objectives

This mini-project shows how to:

### 🔹 1. Load raw data

The dataset originally has:

* No header row
* Missing values marked as `"?"`
* Mixed data types

### 🔹 2. Clean & preprocess the data

The project demonstrates:

* Assigning proper column names
* Replacing “?” with numerical NaN values
* Converting numeric columns to the correct type
* Filling missing values (mean for numbers, mode for categories)
* Mapping categorical text (e.g., “two”, “four”) into numeric values

### 🔹 3. Explore the dataset

You generate:

* Quick previews of the dataset
* Summary statistics
* Checks for missing data

### 🔹 4. Save the cleaned dataset

A fully usable cleaned CSV file is created for reuse or modeling.

---

## 📊 Visualizations Included

The project includes a variety of visualizations — each one chosen for a different analytical purpose.

### **Matplotlib Visualizations**

✔ **Line Plot** — to observe general trends in car prices
✔ **Scatter Plot** — horsepower vs. price relationship
✔ **Histogram** — price distribution
✔ **Bar Plot** — average price by body style
✔ **Pcolor Heatmap** — price patterns across car make × body style

### **Seaborn Visualizations**

✔ **Regression Plot** — regression line showing correlation
✔ **Boxplot** — price comparison across car styles
✔ **(Optional) KDE / Distribution Plot** — density of price values

Each visualization helps answer real questions like:

* *Do more powerful cars cost more?*
* *Which body style is most expensive on average?*
* *Which brands tend to produce higher-priced models?*

---

## 📁 Files Included

* **raw_data_automotive.csv** – original dataset (no headers)
* **Main Python script** – handles data cleaning & visualization

---

## 🧠 What You’ll Learn

This project is designed for beginners and teaches:

### ✔ Data cleaning fundamentals

* Identifying missing values
* Converting types
* Handling categorical and numeric variables

### ✔ Data preparation

* Extracting, mapping, grouping
* Summary statistics

### ✔ Data visualization

A complete introduction to both **matplotlib** and **seaborn**.

### ✔ Real-world interpretation

For every chart, you understand:

* Why it was created
* What insights it reveals
* How to read & interpret patterns

---

## 🌱 Ideal For

This project is perfect for:

* Beginners learning Pandas & Python data analytics
* Students practicing data cleaning techniques
* Anyone starting with data visualization
* Portfolio building for GitHub

---

## 🚀 How to Run

1. Clone the repository
2. Ensure Python 3.8+ is installed
3. Install required libraries:

   ```
   pip install pandas numpy matplotlib seaborn
   ```
4. Run the script in **PyCharm**, VS Code, or Jupyter Notebook

The cleaned dataset will be automatically saved to the output directory.

---


## Author: Varrun Vashisht
