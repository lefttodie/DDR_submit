import json
from modules.openrouter_client import call_llm


def generate_ddr(observations):

    if not observations:
        return "No inspection issues were found."

    obs_text = json.dumps(observations, indent=2)

    prompt = f"""
You are a structural engineer.

Generate a Detailed Diagnostic Report.

OBSERVATIONS:
{obs_text}

Report Sections:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment
5. Recommended Actions
6. Additional Notes
"""

    return call_llm(prompt)