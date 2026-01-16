import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TOPIC_PATH = os.path.join(BASE_DIR, "..", "data", "topic_performance.csv")
RESOURCE_PATH = os.path.join(BASE_DIR, "..", "data", "resources.csv")

topics_df = pd.read_csv(TOPIC_PATH)
resources_df = pd.read_csv(RESOURCE_PATH)

def get_difficulty(learner_type):
    if learner_type == "Weak":
        return ["Easy"]
    elif learner_type == "Average":
        return ["Medium", "Easy"]
    else:
        return ["Medium"]

def recommend_for_student(student_id):
    student_data = topics_df[topics_df["StudentID"] == student_id]

    learner_type = student_data["LearnerType"].iloc[0]
    difficulties = get_difficulty(learner_type)

    threshold = student_data["Score"].quantile(0.4)
    weak_topics = student_data[student_data["Score"] <= threshold]["Topic"]

    recommendations = resources_df[
        (resources_df["Topic"].isin(weak_topics)) &
        (resources_df["Difficulty"].isin(difficulties))
    ]

    return recommendations


if __name__ == "__main__":
    sid = topics_df["StudentID"].iloc[0]
    recs = recommend_for_student(sid)

    print(f"\n📘 Recommendations for Student {sid}:\n")

    if recs.empty:
        print("No weak topics detected. Student is performing well.")
    else:
        print(recs[["Topic", "ResourceType", "Title", "Link"]])
