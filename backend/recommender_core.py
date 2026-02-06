import math
from backend.models import StudentTopic, Resource
from backend.ai_recommender import ai_recommend_resources

def recommend_for_student(student_id):
    rows = StudentTopic.query.filter_by(student_id=student_id).all()

    if not rows:
        return []

    scores = sorted([r.score for r in rows])
    cutoff = max(1, math.ceil(0.30 * len(scores)))
    threshold = scores[cutoff - 1]

    weak_topics = [
        r.topic for r in rows if r.score <= threshold
    ]

    if not weak_topics:
        return []

    learner_type = rows[0].learner_type
    results = []

    for topic in weak_topics:
        explanation = ai_recommend_resources([topic], learner_type)

        resources = Resource.query.filter_by(topic=topic).all()

        for r in resources:
            results.append({
                "Topic": topic,
                "Title": r.title,
                "ResourceType": r.resource_type,
                "Link": r.link,
                "Explanation": explanation
            })

    return results
