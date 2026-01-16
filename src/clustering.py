import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("Loading dataset...")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "student_performance.csv")

df = pd.read_csv(DATA_PATH)

features = [
    "Age",
    "StudyTimeWeekly",
    "Absences",
    "Tutoring",
    "ParentalSupport",
    "GPA"
]

X = df[features]

print("Standardizing features...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Running KMeans clustering...")
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["LearningCluster"] = kmeans.fit_predict(X_scaled)

OUTPUT_PATH = os.path.join(BASE_DIR, "..", "data", "student_clustered.csv")
df.to_csv(OUTPUT_PATH, index=False)

print("✅ Clustering completed successfully!")
print("\nCluster distribution:")
print(df["LearningCluster"].value_counts())
