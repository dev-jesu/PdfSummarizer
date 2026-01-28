def chunk_text(text: str, max_words: int = 350) -> list[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    chunks = []
    current_chunk = []
    current_word_count = 0

    for paragraph in paragraphs:
        words_in_paragraph = len(paragraph.split())

        # If adding this paragraph exceeds limit → finalize current chunk
        if current_word_count + words_in_paragraph > max_words:
            if current_chunk:
                chunks.append("\n\n".join(current_chunk))
                current_chunk = []
                current_word_count = 0

        current_chunk.append(paragraph)
        current_word_count += words_in_paragraph

    # Add last chunk
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))

    return chunks
