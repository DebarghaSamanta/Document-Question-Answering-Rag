def chunk_pages(pages, chunk_size=400, overlap=80):
    
    chunks = []
    chunk_id = 0

    for page in pages:
        words = page["text"].split()

        i = 0
        while i < len(words):
            chunk_words = words[i:i + chunk_size]
            chunk_text = " ".join(chunk_words)

            chunks.append({
                "doc_id": page["doc_id"],
                "page": page["page"],
                "chunk_id": chunk_id,
                "text": chunk_text
            })

            chunk_id += 1
            i += chunk_size - overlap

    return chunks
