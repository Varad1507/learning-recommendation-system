from backend.models import StudentTopic, Resource
from backend.rag.rag_engine import generate_explanation


def get_difficulty(learner_type):
    if learner_type == "Weak":
        return ["Easy"]
    elif learner_type == "Average":
        return ["Easy", "Medium"]
    return ["Medium"]


def recommend_for_student(student_id):
    topic_rows = StudentTopic.query.filter_by(student_id=student_id).all()

    if not topic_rows:
        return []

    learner_type = topic_rows[0].learner_type
    difficulties = get_difficulty(learner_type)

    scores = [t.score for t in topic_rows]
    threshold = sorted(scores)[int(0.4 * len(scores))]
    weak_topics = [t.topic for t in topic_rows if t.score <= threshold]

    resources = (
        Resource.query
        .filter(Resource.topic.in_(weak_topics))
        .filter(Resource.difficulty.in_(difficulties))
        .all()
    )

    return [
        {
            "Topic": r.topic,
            "Title": r.title,
            "ResourceType": r.resource_type,
            "Link": r.link,
            "Explanation": generate_explanation(r.topic, learner_type)
        }
        for r in resources
    ]
