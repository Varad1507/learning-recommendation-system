import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "student_clustered.csv")

df = pd.read_csv(DATA_PATH)

summary = df.groupby("LearningCluster").agg({
    "GPA": "mean",
    "StudyTimeWeekly": "mean",
    "Absences": "mean"
})

print("\n📊 Cluster Summary:\n")
print(summary)

cluster_order = summary["GPA"].sort_values().index.tolist()

labels = {
    cluster_order[0]: "Weak",
    cluster_order[1]: "Average",
    cluster_order[2]: "Strong"
}

df["LearnerType"] = df["LearningCluster"].map(labels)

OUTPUT_PATH = os.path.join(BASE_DIR, "..", "data", "student_profiled.csv")
df.to_csv(OUTPUT_PATH, index=False)

print("\n✅ Learner profiling completed!")
print(df["LearnerType"].value_counts())
