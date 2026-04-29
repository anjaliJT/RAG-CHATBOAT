import streamlit as st
import requests
import os

API_URL = "http://localhost:8000/api/v1"

st.set_page_config(page_title="Enterprise RAG Assistant", page_icon="🤖", layout="wide")

st.title("🤖 Enterprise Gen AI RAG Assistant")
st.markdown("Upload documents (PDF, TXT, MD) and ask questions about them using state-of-the-art Retrieval-Augmented Generation.")

# Sidebar for document upload
with st.sidebar:
    st.header("1. Document Management")
    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "txt", "md"])
    
    if st.button("Upload & Index"):
        if uploaded_file is not None:
            with st.spinner("Processing document..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                try:
                    response = requests.post(f"{API_URL}/upload", files=files)
                    if response.status_code == 200:
                        data = response.json()
                        st.success(f"Successfully indexed! ({data['chunks_indexed']} chunks created)")
                    else:
                        st.error(f"Error: {response.text}")
                except Exception as e:
                    st.error(f"Failed to connect to backend: {str(e)}")
        else:
            st.warning("Please select a file first.")

# Main area for querying
st.header("2. Ask Questions")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message:
            with st.expander("View Sources"):
                for idx, source in enumerate(message["sources"]):
                    st.markdown(f"**Source {idx+1}**: ({source['metadata'].get('source', 'Unknown')})")
                    st.info(source["page_content"])

# React to user input
if prompt := st.chat_input("What would you like to know from the documents?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                f"{API_URL}/query",
                json={"query": prompt}
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data["answer"]
                sources = data["sources"]
                
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(answer)
                    with st.expander("View Sources"):
                        for idx, source in enumerate(sources):
                            st.markdown(f"**Source {idx+1}**: ({source['metadata'].get('source', 'Unknown')})")
                            st.info(source["page_content"])
                            
                # Add assistant response to chat history
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer, "sources": sources}
                )
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to backend: {str(e)}")
