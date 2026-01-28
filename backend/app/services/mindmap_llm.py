import json
import re
import google.generativeai as genai
from app.core.config import GEMINI_API_KEY

MODEL = "models/gemini-2.5-flash-lite"


def _clean(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text, flags=re.IGNORECASE).strip()
        text = re.sub(r"```$", "", text).strip()
    return text


def get_root_concept(document: str) -> str:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(MODEL)

    prompt = f"""
Identify the single central concept of the document.

Rules:
- Use ONLY the document content
- Short noun phrase
- No explanation
- No markdown

Document:
{document}

Output:
"Central Concept"
"""

    res = model.generate_content(prompt)
    return _clean(res.text).strip('"')


def get_children(concept: str, document: str) -> list[str]:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(MODEL)

    prompt = f"""
Based ONLY on the document, list the direct subtopics under:
"{concept}"

Rules:
- Use ONLY document content
- No external knowledge
- If none exist, return []
- Short noun phrases
- Return ONLY valid JSON array

Document:
{document}
"""

    res = model.generate_content(prompt)
    return json.loads(_clean(res.text))
