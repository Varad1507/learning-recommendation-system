from backend.database import db

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    study_time = db.Column(db.Float)
    absences = db.Column(db.Integer)
    gpa = db.Column(db.Float)
    grade_class = db.Column(db.Integer)

class Resource(db.Model):
    __tablename__ = "resources"

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100))
    difficulty = db.Column(db.String(50))
    resource_type = db.Column(db.String(50))
    title = db.Column(db.String(200))
    link = db.Column(db.String(300))

class StudentTopic(db.Model):
    __tablename__ = "student_topics"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Float, nullable=False)
    learner_type = db.Column(db.String(20), nullable=False)
