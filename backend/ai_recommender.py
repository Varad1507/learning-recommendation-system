import os
from groq import Groq
import json

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_recommend_resources(weak_topics, learner_type):
    print("🚀 GROQ AI CALLED — generating structured recommendations")

    prompt = f"""
You are an intelligent learning recommender system.

Student level: {learner_type}
Weak topics: {", ".join(weak_topics)}

Return STRICT JSON in the following format ONLY.
No markdown. No explanation outside JSON.

{{
  "learning_plan": {{
    "summary": "short summary",
    "steps": [
      "step 1",
      "step 2"
    ]
  }},
  "resources": [
    {{
      "topic": "Topic name",
      "title": "Resource title",
      "type": "Video / Article / Practice",
      "link": "https://valid-url.com",
      "reason": "Why this resource helps"
    }}
  ]
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    raw = response.choices[0].message.content.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {
            "learning_plan": {
                "summary": "AI response parsing failed",
                "steps": []
            },
            "resources": []
        }
