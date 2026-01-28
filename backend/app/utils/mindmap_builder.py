import re


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def is_expandable(label: str) -> bool:
    keywords = [
        " and ",
        "types",
        "preprocessing",
        "methods",
        "algorithms",
        "applications"
    ]
    l = label.lower()
    return any(k in l for k in keywords)
