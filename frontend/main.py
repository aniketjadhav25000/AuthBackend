import streamlit as st
import requests

# Title
st.set_page_config(page_title="AI Coding Assistant", layout="centered")
st.title("💡 AI Coding Assistant")
st.write("Generate code from your prompt using OpenAI.")

# Input form
prompt = st.text_area("📝 Enter your code prompt:", height=150)
language = st.selectbox("💻 Choose a programming language:", ["python", "javascript", "java", "c++", "c", "go", "typescript"])

if st.button("🚀 Generate Code"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/generate_code",
                    json={"prompt": prompt, "language": language}
                )
                if response.status_code == 200:
                    result = response.json()
                    st.code(result["code"], language)
                else:
                    st.error("Something went wrong. Check backend or API.")
            except Exception as e:
                st.error(f"Error: {e}")

# Show editable and copyable code block if generated
if "generated_code" in st.session_state:
    st.subheader("✏️ Edit or Copy Your Code")

    # Editable text area for code
    edited_code = st.text_area(
        "🧠 Modify the generated code here:",
        value=st.session_state.generated_code,
        height=300,
        key="editable_code"
    )

    # Optional: Show code in syntax-highlighted block below
    st.code(edited_code, language=language)

    # Download button
    st.download_button(
        label="📥 Download Code",
        data=edited_code,
        file_name=f"generated_code.{language if language != 'c++' else 'cpp'}",
        mime="text/plain"
    )

    # Copy to clipboard button (basic JavaScript injection)
    st.markdown(
        """
        <button onclick="navigator.clipboard.writeText(document.querySelector('textarea').value)"
                style="background-color:#ff4b4b;color:white;padding:10px 20px;border:none;
                       border-radius:8px;font-size:16px;margin-top:10px;cursor:pointer;">
            📋 Copy Code
        </button>
        """,
        unsafe_allow_html=True
    )
