from flask import Flask, jsonify
from flask_cors import CORS
import os
from backend.database import db
from backend.seed import seed_database
from backend.recommender_core import recommend_for_student

def create_app():
    app = Flask(__name__)
    CORS(app)

    instance_path = os.path.join(app.root_path, "instance")
    os.makedirs(instance_path, exist_ok=True)

    db_path = os.path.join(instance_path, "learning.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        seed_database()

    @app.route("/recommend/<int:student_id>")
    def recommend(student_id):
        return jsonify({
            "student_id": student_id,
            "recommendations": recommend_for_student(student_id)
        })

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
