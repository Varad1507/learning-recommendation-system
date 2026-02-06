import os
import pandas as pd
from backend.database import db
from backend.models import StudentTopic, Resource

def seed_database():
    if StudentTopic.query.first():
        print("Database already seeded")
        return

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))

    topics_csv = os.path.join(DATA_DIR, "topic_performance.csv")
    resources_csv = os.path.join(DATA_DIR, "resources.csv")

    topics_df = pd.read_csv(topics_csv)
    resources_df = pd.read_csv(resources_csv)

    for _, row in topics_df.iterrows():
        db.session.add(StudentTopic(
            student_id=int(row["StudentID"]),
            topic=row["Topic"].strip().title(),
            score=float(row["Score"]),
            learner_type=row["LearnerType"]
        ))

    for _, row in resources_df.iterrows():
        db.session.add(Resource(
            topic=row["Topic"].strip().title(),
            title=row["Title"],
            resource_type=row["ResourceType"],
            link=row["Link"],
            difficulty=row["Difficulty"]
        ))

    db.session.commit()
    print("Database seeded successfully")
