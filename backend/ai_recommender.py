from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_learning_recommendations(topics, learner_type):
    prompt = f"""
You are an expert learning tutor.

Student level: {learner_type}
Weak topics: {", ".join(topics)}

Give:
1. Clear explanation
2. Learning strategy
3. Resource suggestions (videos, articles, practice)
4. Study order

Keep it concise and practical.
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text
