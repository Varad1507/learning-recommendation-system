import os
import pandas as pd
from backend.database import db
from backend.models import StudentTopic, Resource

def seed_database():
    # Prevent reseeding
    if StudentTopic.query.first():
        print("Database already seeded")
        return

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))

    topics_csv = os.path.join(DATA_DIR, "topic_performance.csv")
    resources_csv = os.path.join(DATA_DIR, "resources.csv")

    print("Looking for CSVs at:", DATA_DIR)
    print("Topics CSV exists:", os.path.exists(topics_csv))
    print("Resources CSV exists:", os.path.exists(resources_csv))

    if not os.path.exists(topics_csv) or not os.path.exists(resources_csv):
        print("CSV files not found. Skipping seed.")
        return

    # ---- Load student topics ----
    topics_df = pd.read_csv(topics_csv)

    for _, row in topics_df.iterrows():
        db.session.add(StudentTopic(
            student_id=int(row["StudentID"]),
            topic=row["Topic"],
            score=float(row["Score"]),
            learner_type=row["LearnerType"]
        ))

    # ---- Load resources ----
    resources_df = pd.read_csv(resources_csv)

    for _, row in resources_df.iterrows():
        db.session.add(Resource(
            topic=row["Topic"],
            title=row["Title"],
            resource_type=row["ResourceType"],
            link=row["Link"],
            difficulty=row["Difficulty"]
        ))

    db.session.commit()
    print("Database seeded successfully")
