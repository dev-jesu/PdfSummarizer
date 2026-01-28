import json
import re
import google.generativeai as genai
from app.core.config import GEMINI_API_KEY

MODEL = "models/gemini-2.5-flash-lite"


def _clean_json(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text, flags=re.IGNORECASE).strip()
        text = re.sub(r"```$", "", text).strip()
    return text


def extract_concepts(document: str) -> dict:
    if not GEMINI_API_KEY:
        raise RuntimeError("Gemini API key missing")

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(MODEL)

    prompt = f"""
You are analyzing a document to extract structured learning concepts.

Task:
From the document, extract:
1. One main topic
2. 5–10 key concepts
3. For each concept, list 2–5 related sub-concepts ONLY if they are explicitly mentioned

Rules:
- Use ONLY the document content
- Do NOT add external knowledge
- Use short noun phrases
- If a concept has no clear sub-concepts, use an empty list
- Return ONLY valid JSON
- No markdown, no explanation

JSON format:
{{
  "main_topic": "...",
  "concepts": [
    {{
      "label": "...",
      "sub_concepts": ["...", "..."]
    }}
  ]
}}

Document:
{document}
"""

    response = model.generate_content(prompt)
    clean = _clean_json(response.text)

    return json.loads(clean)
