from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_pages
if __name__ == "__main__":
    pages = load_pdf("data/raw_pdf/Sample.pdf", doc_id="doc1")

    print("Total pages extracted:", len(pages))
    print("\n--- Second Page ---\n")
    print(pages[0]["text"][:1000])


    chunks = chunk_pages(pages, chunk_size=400, overlap=80)
    print("Total chunks created:", len(chunks))

    print("\n--- First chunk preview ---\n")
    print(chunks[0]["text"][:1000])
    print("\n--- Chunk metadata example ---\n")
    print(chunks[0])
    