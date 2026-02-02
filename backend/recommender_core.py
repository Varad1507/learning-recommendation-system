from backend.models import StudentTopic
from backend.ai_recommender import generate_learning_recommendations


def recommend_for_student(student_id):
    topic_rows = StudentTopic.query.filter_by(student_id=student_id).all()

    if not topic_rows:
        return []

    learner_type = topic_rows[0].learner_type

    scores = sorted([t.score for t in topic_rows])
    threshold = scores[int(0.4 * len(scores))]

    weak_topics = [t.topic for t in topic_rows if t.score <= threshold]

    if not weak_topics:
        return []

    explanation = generate_learning_recommendations(
        topics=weak_topics,
        learner_type=learner_type
    )

    return [
        {
            "Topic": ", ".join(weak_topics),
            "Title": "AI-Generated Personalized Learning Plan",
            "ResourceType": "GenAI (Gemini)",
            "Link": "",
            "Explanation": explanation
        }
    ]
