import os
import json
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_recommend_resources(weak_topics, learner_type):
    print("🚀 GROQ AI CALLED — generating recommendations")

    prompt = f"""
You are an intelligent learning recommendation system.

Learner type: {learner_type}
Weak topics: {', '.join(weak_topics)}

Generate 3 learning recommendations in STRICT JSON format.
Each object must contain:
- Topic
- Title
- ResourceType
- Link
- Explanation

Return ONLY valid JSON. Do NOT use markdown.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    raw_text = response.choices[0].message.content.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(raw_text)
        print("✅ GROQ RESPONSE PARSED SUCCESSFULLY")
        return data
    except json.JSONDecodeError:
        print("❌ JSON parsing failed")
        print(raw_text)
        return []
