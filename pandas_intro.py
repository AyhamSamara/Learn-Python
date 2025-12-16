import pandas as pd
import numpy as np  # Often used with pandas for logic

# ==========================================
# PART 1: CREATING A NEW EXCEL FILE
# ==========================================
print("--- 1. Creating a New Workbook ---")

# 1. Define Data (Using a Dictionary is easiest in Pandas)
data = {
    "Student Name": ["Ayham", "Tareq", "Omar", "Yousef", "Zaid"],
    "Math Score": [85, 45, 70, 95, 40],
    "Science Score": [90, 60, 55, 99, 35]
}

# 2. Create a DataFrame (Think of this as the Table)
df = pd.DataFrame(data)

# 3. Save to Excel
# index=False prevents pandas from adding a 0,1,2,3 column on the left
filename = "grades_report_pandas.xlsx"
df.to_excel(filename, index=False)

print(f"Created '{filename}' with dummy data.\n")


# ==========================================
# PART 2: READING & PROCESSING DATA
# ==========================================
print("--- 2. Processing Data ---")

# 1. Read the Excel file back into memory
df = pd.read_excel(filename)

# 2. Calculate Total Score
# NO LOOP NEEDED! Pandas adds the whole column at once.
df["Total Score"] = df["Math Score"] + df["Science Score"]

# 3. Determine Pass/Fail Status
# We use numpy.where (logic: if condition, value_if_true, value_if_false)
df["Status"] = np.where(df["Total Score"] >= 100, "PASS", "FAIL")

print("Preview of processed data:")
print(df)

# ==========================================
# PART 3: SAVING THE RESULT
# ==========================================
new_filename = "grades_report_pandas_processed.xlsx"

# Save the updated DataFrame to a new file
df.to_excel(new_filename, index=False)

print(f"\n--- Done! Saved processed file as '{new_filename}' ---")