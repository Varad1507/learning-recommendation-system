from flask import Flask, jsonify
from flask_cors import CORS
import os
from backend.database import db
from backend import models
from backend.recommender_core import recommend_for_student
from backend.seed_data import seed_database

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

    @app.route("/recommend/<int:student_id>", methods=["GET"])
    def recommend(student_id):
        recs = recommend_for_student(student_id)

        if not recs:
            return jsonify({
                "student_id": student_id,
                "message": "No weak topics detected",
                "recommendations": []
            })

        return jsonify({
            "student_id": student_id,
            "recommendations": recs
        })

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
