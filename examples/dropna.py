import numpy as np
import pandas as pd

# 1. CREATE A MESSY STARTING DATAFRAME
# We use np.nan and None to represent missing values in our table.
data = {
    "Name": ["Alice", "Bob", "Charlie", None],
    "Age": [25, np.nan, 30, None],
    "City": ["New York", "Los Angeles", None, None],
    "Score": [90, np.nan, np.nan, None],
}
df_original = pd.DataFrame(data)

print("--- ORIGINAL DATAFRAME ---")
print(df_original)
print("\n" + "=" * 50 + "\n")


# 2. DEMO: DEFAULT BEHAVIOR (axis=0, how='any')
# This drops any row if it contains at least ONE missing value.
# Result: Only Alice's row survives because it is the only fully complete row.
df_default = df_original.dropna(axis=0, how="any")

print("--- DEMO 1: dropna() [Default settings] ---")
print("Original stays unchanged:")
print(df_original)
print("\nNew DataFrame (Dropped rows with ANY missing value):")
print(df_default)
print("\n" + "=" * 50 + "\n")


# 3. DEMO: DROP ONLY IF ENTIRELY EMPTY (how='all')
# This only drops a row if EVERY single column in that row is missing.
# Result: Row 3 (the last row) is completely gone, but Bob and Charlie stay.
df_all_empty = df_original.dropna(axis=0, how="all")

print("--- DEMO 2: dropna(how='all') ---")
print("Original stays unchanged:")
print(df_original)
print("\nNew DataFrame (Dropped only rows where ALL values are missing):")
print(df_all_empty)
print("\n" + "=" * 50 + "\n")


# 4. DEMO: TARGET SPECIFIC COLUMNS (subset)
# This tells pandas to ONLY look for missing data in the 'Age' column.
# Result: Charlie stays (even though his City/Score are missing) because his Age is valid.
df_subset = df_original.dropna(subset=["Age"])

print("--- DEMO 3: dropna(subset=['Age']) ---")
print("Original stays unchanged:")
print(df_original)
print("\nNew DataFrame (Dropped rows ONLY if 'Age' was missing):")
print(df_subset)
print("\n" + "=" * 50 + "\n")


# 5. DEMO: DROP COLUMNS INSTEAD OF ROWS (axis=1)
# This switches the direction. It removes any COLUMN that has a missing value.
# Result: Columns 'Age', 'City', and 'Score' are dropped. Only 'Name' remains.
df_columns = df_original.dropna(axis=1, how="any")

print("--- DEMO 4: dropna(axis=1) ---")
print("Original stays unchanged:")
print(df_original)
print("\nNew DataFrame (Dropped vertical COLUMNS with missing values):")
print(df_columns)
print("\n" + "=" * 50 + "\n")


# 6. DEMO: MODIFY IN PLACE (inplace=True)
# This does not create a new variable. It permanently overwrites the original variable.
# Result: df_original itself changes right here in memory.
print("--- DEMO 5: dropna(inplace=True) ---")
print("Original before inplace operation:")
print(df_original)

# We apply the drop directly to the original dataframe
df_original.dropna(subset=["Name"], inplace=True)

print("\nOriginal after inplace operation (Rows missing a 'Name' are permanently gone):")
print(df_original)
