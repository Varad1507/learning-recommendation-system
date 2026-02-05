import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ai_recommend_resources(topics, learner_type):
    """
    Uses Groq LLM to generate personalized learning explanations.
    AI is ONLY responsible for explanation.
    """

    if not topics:
        return "No weak topics identified."

    topic_list = ", ".join(topics)

    prompt = f"""
You are an intelligent learning assistant.

A student with learner type "{learner_type}" is weak in the following topics:
{topic_list}

Generate:
1. Why these topics were recommended
2. A clear, beginner-friendly learning strategy
3. Expected learning outcome

Keep the explanation concise, structured, and easy to understand.
Avoid markdown symbols.
"""

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return (
            "AI explanation could not be generated at this time. "
            "Please refer to the recommended learning resources."
        )
