from backend.models import StudentTopic
from backend.ai_recommender import ai_recommend_resources

def recommend_for_student(student_id):
    topic_rows = StudentTopic.query.filter_by(student_id=student_id).all()

    if not topic_rows:
        return []

    learner_type = topic_rows[0].learner_type
    scores = [t.score for t in topic_rows]

    threshold = sorted(scores)[int(0.4 * len(scores))]
    weak_topics = [t.topic for t in topic_rows if t.score <= threshold]

    ai_text = ai_recommend_resources(weak_topics, learner_type)

    return [{
        "Topic": ", ".join(weak_topics),
        "Title": "AI-Generated Learning Plan",
        "ResourceType": "AI Recommendation",
        "Link": "#",
        "Explanation": ai_text
    }]
