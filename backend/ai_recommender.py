import os
import json
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_recommend_resources(weak_topics, learner_type):
    print("🚀 GROQ AI CALLED — generating structured recommendations")

    prompt = f"""
You are an intelligent learning recommendation system.

Student type: {learner_type}
Weak topics: {", ".join(weak_topics)}

Return ONLY valid JSON in the following format:

{{
  "summary": {{
    "student_level": "{learner_type}",
    "weak_topics": {weak_topics},
    "reason": "Explain briefly why these topics are weak"
  }},
  "resources": [
    {{
      "topic": "Topic name",
      "title": "Resource title",
      "type": "Video / Article / Practice",
      "link": "Valid learning URL",
      "why": "Why this resource is helpful"
    }}
  ]
}}

Rules:
- Give 2–4 resources
- Use real, well-known learning platforms (GeeksForGeeks, YouTube, LeetCode)
- Do NOT include markdown
- Do NOT include explanations outside JSON
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    raw_text = response.choices[0].message.content.strip()

    try:
        return json.loads(raw_text)
    except Exception:
        print("❌ AI returned invalid JSON")
        return None
