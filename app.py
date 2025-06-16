import streamlit as st
from nlp_utils import extract_keywords
from graph_utils import build_mind_map, draw_graph

st.set_page_config(page_title="🧠 Mind Map Generator", layout="wide")
st.title("🧠 Mind Map Generator from Notes")

text_input = st.text_area("✍️ Paste your notes here:")

if st.button("🧠 Generate Mind Map"):
    if text_input.strip():
        keywords = extract_keywords(text_input)
        if keywords:
            st.subheader("📌 Extracted Keywords:")
            st.write(", ".join(keywords))
            G = build_mind_map(keywords)
            draw_graph(G)
        else:
            st.error("No keywords found. Try different text.")
    else:
        st.warning("Please enter some notes first.")
