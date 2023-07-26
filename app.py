import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)

def main():
    llm = ChatOpenAI(temperature=0.7, max_tokens=64)
    
    st.set_page_config(
        page_title="Numko Chatbot",
        page_icon="(^^)",
    )
    st.header("Numko Chatbot")
    
    # Chat setting
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage("Hello, I'm Numko.I'm Vtuber. How can I help you?"),
        ]
        
    # Check input
    if user_input := st.text_input("What is your question?"):
        st.session_state.messages.append(HumanMessage(user_input))
        with st.spinner("Numko is thinking..."):
            ai_message = llm.generate_message(st.session_state.messages)
        st.session_state.messages.append(ai_message(content=response.content))
        
    # Show chat history
    messages = st.session_state.get('messages', [])
    for message in messages:
        if isinstance(message, SystemMessage):
            st.write(message.content)
        elif isinstance(message, HumanMessage):
            st.write(message.content)
        elif isinstance(message, AIMessage):
            st.write(message.content)
            
if __name__ == "__main__":
    main()