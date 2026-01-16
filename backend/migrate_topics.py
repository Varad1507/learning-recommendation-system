import pandas as pd

from backend.app import create_app
from backend.database import db
from backend.models import StudentTopic

app = create_app()

CSV_PATH = "data/topic_performance.csv"

with app.app_context():
    df = pd.read_csv(CSV_PATH)

    for _, row in df.iterrows():
        record = StudentTopic(
            student_id=int(row["StudentID"]),
            topic=row["Topic"],
            score=float(row["Score"]),
            learner_type=row["LearnerType"]
        )
        db.session.add(record)

    db.session.commit()

print("✅ Topic performance migrated successfully")
