import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_recommend_resources(topics, learner_type):
    print("🚀 AI CALLED — generating structured resources")

    prompt = f"""
You are an intelligent learning recommendation system.

Student type: {learner_type}
Weak topics: {", ".join(topics)}

Return a JSON ARRAY.
Each item must contain:
- Topic
- Title
- ResourceType (Video / Article / Practice)
- Link (REAL, VALID URL)
- Explanation (array of bullet points)

Example format:
[
  {{
    "Topic": "Sorting",
    "Title": "Sorting Algorithms Explained",
    "ResourceType": "Video",
    "Link": "https://www.youtube.com/watch?v=kgBjXUE_Nwc",
    "Explanation": [
      "Explains time complexity visually",
      "Helps understand trade-offs"
    ]
  }}
]

Return ONLY valid JSON. No markdown.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    import json
    return json.loads(response.choices[0].message.content)
