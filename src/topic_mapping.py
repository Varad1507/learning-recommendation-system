import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "student_profiled.csv")

df = pd.read_csv(DATA_PATH)

topics = ["Arrays", "Linked Lists", "Sorting", "Stacks", "Queues"]

records = []

for _, row in df.iterrows():
    base_score = row["GPA"] * 25  # normalize GPA to 100

    for topic in topics:
        noise = np.random.randint(-10, 10)
        score = max(0, min(100, base_score + noise))

        records.append({
            "StudentID": row["StudentID"],
            "LearnerType": row["LearnerType"],
            "Topic": topic,
            "Score": score
        })

topic_df = pd.DataFrame(records)

OUTPUT_PATH = os.path.join(BASE_DIR, "..", "data", "topic_performance.csv")
topic_df.to_csv(OUTPUT_PATH, index=False)

print("✅ Topic-wise performance generated!")
print(topic_df.head())
