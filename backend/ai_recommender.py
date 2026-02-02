import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyDhIEoBf3jyhkpnteSvNZT2mdfkLCb9_9A"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_learning_recommendations(topics, learner_type):
    topic_list = ", ".join(topics)

    prompt = f"""
You are an intelligent learning assistant.

Student profile:
- Learner type: {learner_type}
- Weak topics: {topic_list}

For EACH topic, generate:
1. Learning objective
2. Recommended resource types (videos, articles, practice)
3. A short study plan
4. Expected outcome

Respond in clear, structured text (no markdown).
"""

    response = model.generate_content(prompt)
    return response.text
