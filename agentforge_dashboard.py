import streamlit as st
import json

st.set_page_config(page_title="AgentForge - Trace Viewer", layout="wide")
st.title("🧠 AgentForge - Trace & Memory Inspector")

st.markdown("""
Upload a `.json` trace file from your agent run below.  
You'll see each tool call, input/output pair, and memory hits (RAG chunks).
""")

uploaded_file = st.file_uploader("📁 Upload Agent Trace (JSON)", type=["json"])

if uploaded_file is None:
    st.info("👆 Upload a trace file to get started.")
else:
    try:
        trace = json.load(uploaded_file)

        # --- METADATA ---
        st.subheader("🔖 Run Metadata")
        if "metadata" in trace:
            st.json(trace["metadata"])
        else:
            st.warning("No metadata found in trace.")

        # --- AGENT STEPS ---
        st.subheader("🧩 Step-by-Step Trace")
        steps = trace.get("steps", [])
        if steps:
            for step in steps:
                with st.expander(f"Step {step['step_number']}: {step['tool']}"):
                    st.markdown(f"**📝 Input:** `{step['input']}`")
                    st.markdown(f"**📤 Output:** `{step['output']}`")
                    st.markdown(f"**⏱ Timestamp:** `{step.get('timestamp', 'N/A')}`")
                    if "error_type" in step:
                        st.error(f"⚠️ Error: {step['error_type']}")
                    if "notes" in step:
                        st.info(f"🗒 Notes: {step['notes']}")
        else:
            st.warning("No steps found in trace.")

        # --- MEMORY HITS ---
        st.subheader("🧠 Memory (RAG Context)")
        memory_hits = trace.get("memory_hits", [])
        if memory_hits:
            for i, hit in enumerate(memory_hits, start=1):
                with st.expander(f"Memory Hit {i} - Score: {hit['score']}"):
                    st.markdown(f"**📄 Source:** `{hit['source']}`")
                    st.code(hit["content"])
        else:
            st.info("No memory (RAG) chunks found in this trace.")

    except Exception as e:
        st.error(f"❌ Error parsing trace file: {e}")
