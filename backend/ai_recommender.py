import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_recommend_resources(topics, learner_type):
    topic_list = ", ".join(topics)

    prompt = f"""
A student with learning style {learner_type} is weak in:
{topic_list}

Explain:
1. Why this topic is weak
2. How to study it
3. Expected outcome
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=1200
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Groq ERROR:", e)
        return "Explanation not available"
