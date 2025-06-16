import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import streamlit as st

def build_mind_map(keywords):
    G = nx.Graph()
    for i, kw in enumerate(keywords):
        G.add_node(kw)
        if i != 0:
            G.add_edge(keywords[0], kw)  # center node se edge
    return G

def draw_graph(G):
    fig, ax = plt.subplots(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, edge_color='gray', ax=ax)

    st.pyplot(fig)

    # Save as image logic
    buf = BytesIO()
    fig.savefig(buf, format="png")
    st.download_button(
        label="📥 Download Mind Map as Image",
        data=buf.getvalue(),
        file_name="mindmap.png",
        mime="image/png"
    )
