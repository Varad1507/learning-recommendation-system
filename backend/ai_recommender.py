import os

def ai_recommend_resources(topics, learner_type):
    """
    AI is ONLY responsible for explanation & study strategy
    """

    topic_list = ", ".join(topics)

    explanation = f"""
**Why these topics were recommended**

• Based on performance analysis, the student shows comparatively lower scores in **{topic_list}**.
• These topics require strong conceptual clarity and repeated practice.
• Strengthening them will significantly improve overall problem-solving ability.

**Recommended Learning Strategy**

1. Start with conceptual understanding using visual explanations.
2. Implement basic examples manually before moving to problems.
3. Solve beginner-level problems and gradually increase difficulty.
4. Analyze mistakes and revise weak sub-concepts.
5. Revisit these topics weekly to ensure long-term retention.

**Outcome**
Following this plan will improve confidence, speed, and accuracy in interviews and exams.
"""

    return explanation.strip()
