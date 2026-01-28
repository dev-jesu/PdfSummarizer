from app.services.mindmap_llm import get_children
from app.utils.slug import slugify

MAX_DEPTH = 4
MAX_CHILDREN = 7


def build_node(label: str, document: str, depth: int = 1) -> dict:
    node = {
        "id": slugify(label),
        "label": label
    }

    if depth >= MAX_DEPTH:
        return node

    children = get_children(label, document)

    if not children:
        return node

    children = children[:MAX_CHILDREN]

    node["children"] = [
        build_node(child, document, depth + 1)
        for child in children
    ]

    return node
