import json
import re
from modules.openrouter_client import call_llm


def extract_observations(text):

    if not text:
        return []

    prompt = f"""
Extract building inspection issues.

Return JSON only.

Format:

[
 {{
  "area": "",
  "observation": "",
  "thermal_reading": "",
  "issue_type": ""
 }}
]

TEXT:
{text[:4000]}
"""

    result = call_llm(prompt)

    cleaned = re.sub(r"```json|```", "", result).strip()

    try:
        return json.loads(cleaned)
    except:
        print("JSON ERROR")
        print(cleaned)
        return []