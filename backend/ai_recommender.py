import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_recommend_resources(weak_topics, learner_type):
    print("🚀 AI CALLED — generating AI recommendations")

    prompt = f"""
    You are an expert learning advisor.

    Student type: {learner_type}
    Weak topics: {", ".join(weak_topics)}

    Generate a personalized learning plan:
    - Explain why these topics are weak
    - What the student should focus on
    - Suggested practice strategy
    - Keep it concise (4–6 sentences)
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()
