def extract_text_from_txt(file) -> str:
    content = file.read().decode("utf-8").strip()

    if not content:
        raise ValueError("TXT file is empty")

    return content
