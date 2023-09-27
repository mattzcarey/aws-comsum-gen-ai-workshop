"""Streamlit app for GenAI Workshop.

Please read the README.md in the root to set up the project then. 

Start from project root with :
```bash
PYTHONPATH=. streamlit run demo/main.py
```
Don't forget to set .env variables before running the app.
"""

import streamlit as st

from demo.constants.paths import ROOT_FOLDER
from demo.llm.llm import llm
from demo.prompts.system_prompt import system_prompt
from demo.prompts.welcome_message import welcome_message

st.set_page_config(
    "GenAI Workshop",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=str(ROOT_FOLDER / "demo/logo.png"),
)

st.title("ComSum AI Personal Assistant")

# Side bar
# with st.sidebar:

# Initialize chat history on app start
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        system_prompt,
        welcome_message,
    ]

# Display the welcome message
for msg in st.session_state.messages:
    if msg["role"] == "system":
        st.markdown(f"System Prompt: *{msg['content']}*")
        continue
    st.chat_message(msg["role"]).write(msg["content"])

# Show a chat text box
with st.spinner("Thinking..."):
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        msg = ""

        try:
            response = llm(prompt)
            print(response)
            msg = response

        except Exception as e:
            st.error(e)
            st.stop()
        st.empty()

    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg["content"])
