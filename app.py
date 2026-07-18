import streamlit as st

from src.pdf_loader import extract_text
from src.prompts import build_document_prompt
from src.llm import ask_llm

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="ScholarAI",
    page_icon="📘",
    layout="wide",
)

st.title("📘 ScholarAI")
st.caption("Your AI-Powered Learning & Research Assistant")

# ----------------------------
# Session State
# ----------------------------
if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "document_name" not in st.session_state:
    st.session_state.document_name = None

# ----------------------------
# PDF Upload
# ----------------------------
uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"],
)

if st.session_state.document_name:
    st.info(f"📄 Current document: {st.session_state.document_name}")
    

if uploaded_file is not None:

    if uploaded_file.name != st.session_state.document_name:

        try:
            with st.spinner("Reading your document..."):

                st.session_state.document_text = extract_text(uploaded_file)
                st.session_state.document_name = uploaded_file.name

            st.success(f"✅ '{uploaded_file.name}' uploaded successfully!")

        except Exception as e:
            st.error(f"Error reading PDF: {e}")

# ----------------------------
# Question Input
# ----------------------------
question = st.text_input(
    "Ask a question about your document"
)

# ----------------------------
# Ask Button
# ----------------------------
if st.button("Ask ScholarAI"):

    if not st.session_state.document_text:
        st.warning("Please upload a PDF first.")

    elif not question.strip():
        st.warning("Please enter a question.")

    else:

        prompt = build_document_prompt(
            st.session_state.document_text,
            question
        )

        with st.spinner("ScholarAI is thinking..."):

            answer = ask_llm(prompt)

        st.subheader("Answer")

        st.markdown(answer)