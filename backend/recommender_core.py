from backend.models import StudentTopic
from backend.ai_recommender import ai_recommend_resources
from backend.resources_map import RESOURCES_MAP

def recommend_for_student(student_id):
    topic_rows = StudentTopic.query.filter_by(student_id=student_id).all()
    if not topic_rows:
        return []

    scores = sorted([t.score for t in topic_rows])
    threshold = scores[int(0.4 * len(scores))]

    weak_topics = [t.topic for t in topic_rows if t.score <= threshold]
    if not weak_topics:
        return []

    learner_type = topic_rows[0].learner_type

    # AI ONLY FOR EXPLANATION
    explanation = ai_recommend_resources(weak_topics, learner_type)

    recommendations = []

    for topic in weak_topics:
        for res in RESOURCES_MAP.get(topic, []):
            recommendations.append({
                "Topic": topic,
                "Title": res["title"],
                "ResourceType": res["type"],
                "Link": res["link"],
                "Explanation": explanation
            })

    return recommendations
