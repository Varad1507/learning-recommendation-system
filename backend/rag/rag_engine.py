def generate_explanation(topic, learner_type):
    """
    Lightweight fallback explanation.
    This avoids heavy ML dependencies during deployment.
    """

    if learner_type == "Weak":
        return (
            f"You showed lower performance in {topic}. "
            f"This resource focuses on building strong fundamentals step by step."
        )

    elif learner_type == "Average":
        return (
            f"You have a moderate understanding of {topic}. "
            f"This resource helps reinforce concepts and improve consistency."
        )

    else:
        return (
            f"You are doing well in {topic}, but this resource helps strengthen mastery "
            f"and prepares you for advanced problems."
        )
