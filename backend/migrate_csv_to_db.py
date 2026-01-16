import pandas as pd

from backend.app import app
from backend.database import db
from backend.models import Student, Resource

STUDENT_CSV = "data/student_performance.csv"
RESOURCE_CSV = "data/resources.csv"

with app.app_context():

    df_students = pd.read_csv(STUDENT_CSV)

    for _, row in df_students.iterrows():
        student = Student(
            id=int(row["StudentID"]),
            age=int(row["Age"]),
            gender=int(row["Gender"]),
            study_time=float(row["StudyTimeWeekly"]),
            absences=int(row["Absences"]),
            gpa=float(row["GPA"]),
            grade_class=int(row["GradeClass"])
        )
        db.session.merge(student)  

    df_resources = pd.read_csv(RESOURCE_CSV)

    for _, row in df_resources.iterrows():
        resource = Resource(
            topic=row["Topic"],
            difficulty=row["Difficulty"],
            resource_type=row["ResourceType"],
            title=row["Title"],
            link=row["Link"]
        )
        db.session.add(resource)

    db.session.commit()

print("✅ CSV data successfully migrated into the database")
