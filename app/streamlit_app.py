"""Streamlit demo — side-by-side base vs. fine-tuned + agent.

Run:
    streamlit run app/streamlit_app.py

Filled in during Notebook 4 / post-training. This is a working skeleton.
"""
import streamlit as st
from app.demo_notes import DEMO_NOTES

st.set_page_config(page_title="ICD-10 Coding SLM Demo", layout="wide")
st.error("⚠️  Educational demo only — not medical advice. No real patient data.")
st.title("ICD-10 Coding SLM — Base vs. Fine-tuned + Agent")

# Case selector
case_key = st.selectbox(
    "Choose a sample doctor's note:",
    options=list(DEMO_NOTES.keys()),
    format_func=lambda k: DEMO_NOTES[k]["title"],
)
note_data = DEMO_NOTES[case_key]

st.text_area("Clinical note:", value=note_data["note"], height=300, disabled=True)

if st.button("🔬 Run both models", type="primary"):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Base Qwen3-1.7B (FP16)")
        st.caption("No fine-tuning, no tools")
        st.info("TODO: run base model inference — wired in Notebook 4.")
    with col2:
        st.subheader("Fine-tuned Q4 + Agent")
        st.caption("QLoRA-trained, Q4 GGUF, RAG + tool validation")
        st.info("TODO: run agent pipeline — wired in Notebook 4.")

    st.markdown("### Expected codes (author annotation)")
    for code in note_data["expected_codes"]:
        st.code(code)
