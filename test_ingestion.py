from ingestion.pdf_loader import load_pdf

if __name__ == "__main__":
    pages = load_pdf("data/raw_pdf/Sample.pdf", doc_id="doc1")

    print("Total pages extracted:", len(pages))
    print("\n--- Second Page ---\n")
    print(pages[1]["text"][:1000])
