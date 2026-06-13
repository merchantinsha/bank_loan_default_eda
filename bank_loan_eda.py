"""
Bank Loan Default — Exploratory Data Analysis
==============================================
Analyse an 850-record bank loan dataset to uncover patterns
in borrower demographics, debt ratios, and default behaviour.

Dataset features: age, education level, employment tenure,
address tenure, income, debt-to-income ratio, credit debt,
other debt, and default status.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. Load dataset ──────────────────────────────────────────

df = pd.read_csv("bankloan.csv")

# ── 2. Initial inspection ────────────────────────────────────

print("Shape:", df.shape)
print("\nFirst 10 records:")
print(df.head(10))

print("\nFeature names:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)

print("\nDataset info:")
print(df.info())

print("\nNull values per column:")
print(df.isnull().sum())

# ── 3. Sorting & slicing ─────────────────────────────────────

# Last 10 records sorted by age
sorted_by_age = df.sort_values(by="age")
print("\nLast 10 records sorted by age:")
print(sorted_by_age.tail(10))

# Min and max age records
print("\nYoungest borrower:")
print(sorted_by_age.iloc[[0]])
print("\nOldest borrower:")
print(sorted_by_age.iloc[[-1]])

# Records from index 700, columns 4–8
print("\nSlice — index 700:710, columns 4:9:")
print(df.iloc[700:710, 4:9])

# ── 4. Unique age distribution ───────────────────────────────

print("\nUnique age counts:")
print(df["age"].value_counts())

# Check for unexpected ages
outliers = df[(df["age"] < 0) | (df["age"] > 100)]
print(f"\nAge outliers (outside 0–100): {len(outliers)} records")

# ── 5. Default analysis ──────────────────────────────────────

print("\nDefault rate (%):")
print(df["default"].value_counts(normalize=True) * 100)

print("\nDefaulters and non-defaulters by age:")
print(df.groupby("age")["default"].value_counts())

# ── 6. Visualisations ────────────────────────────────────────

# Age distribution
plt.figure(figsize=(10, 5))
plt.hist(df["age"], bins=20, edgecolor="black", color="steelblue")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of Borrowers")
plt.tight_layout()
plt.savefig("age_distribution.png", dpi=150)
plt.show()

# Default rate by age group
age_bins = [20, 30, 40, 50, 60]
labels = ["20-29", "30-39", "40-49", "50-59"]
df["age_group"] = pd.cut(df["age"], bins=age_bins, labels=labels)

default_by_age = df.groupby("age_group")["default"].mean() * 100
plt.figure(figsize=(8, 5))
default_by_age.plot(kind="bar", color="coral", edgecolor="black")
plt.xlabel("Age Group")
plt.ylabel("Default Rate (%)")
plt.title("Default Rate by Age Group")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("default_rate_by_age.png", dpi=150)
plt.show()

# Income vs debt-to-income ratio coloured by default status
plt.figure(figsize=(10, 6))
colours = {0.0: "steelblue", 1.0: "coral"}
for status, group in df.dropna(subset=["default"]).groupby("default"):
    label = "Defaulted" if status == 1.0 else "Non-default"
    plt.scatter(group["income"], group["debtinc"],
                alpha=0.5, label=label, c=colours[status])
plt.xlabel("Income")
plt.ylabel("Debt-to-Income Ratio")
plt.title("Income vs Debt-to-Income Ratio by Default Status")
plt.legend()
plt.tight_layout()
plt.savefig("income_vs_debtinc.png", dpi=150)
plt.show()

print("\nAnalysis complete. Charts saved.")
