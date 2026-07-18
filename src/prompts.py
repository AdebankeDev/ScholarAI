def build_document_prompt(document: str, question: str) -> str:
    return f"""
You are a helpful study assistant.

Use ONLY the information in the document below.

If the answer is not in the document, say:
"I couldn't find that information in the document."

Document:
{document}

Question:
{question}
"""