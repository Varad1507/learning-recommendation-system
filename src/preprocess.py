import pandas as pd

df = pd.read_csv(
    r"C:\Users\mulev\OneDrive\Desktop\learning-recommendation-system\data\student_performance.csv"
)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)
print("\nFirst 5 rows:")
print(df.head())
