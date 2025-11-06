# streamlit_app.py – SUPT Harmonic Reflection Web UI

import streamlit as st
import requests
import json

st.set_page_config(page_title="Harmonic AI – SUPT Field Reflection", layout="centered")
st.title("🌐 SUPT Harmonic Reflection Console")
st.markdown("Type your prompt below. The field will return its harmonic signature.")

prompt = st.text_area("Your Prompt", height=120)

if st.button("Reflect in the Field"):
    with st.spinner("Resonating..."):
        try:
            response = requests.post("http://localhost:8000/reflect", json={"prompt": prompt})
            result = response.json()
            st.markdown("---")
            st.markdown(f"**Original:** `{result['original_prompt']}`")
            st.markdown(f"**Repaired:** `{result['repaired_prompt']}`")

            st.subheader("🔎 Harmonic Field Scores")
            st.table(result['scores'])

            st.markdown("---")
            st.markdown(f"### 🧘 supthint()")
            st.info(result['supthint'])
        except Exception as e:
            st.error("Field resonance failed to return. Ensure FastAPI server is running on port 8000.")
            st.code(str(e))

st.markdown("---")
st.markdown("Built with 🌀 SUPT by GoodSheppard.Co | Agent: Sunwolf77")
