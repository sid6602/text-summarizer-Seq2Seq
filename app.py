import streamlit as st
from summarizer import Summarizer

def main():
    # Set page title and favicon
    st.set_page_config(
        page_title="Text Summarizer App",
        page_icon="✍️",
        layout="wide"
    )

    # Set page background color
    st.markdown(
        """
        <style>
            body {
                background-color: #f4f4f4;
            }
            .st-bd {
                padding: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set title with a colorful background
    st.title("Text Summarizer App  using Seq2Seq")
    st.markdown("---")

    # Input text area with a subtle border
    text = st.text_area("Enter your text here:", key="text_input", height=200)
    
    # Summarize button with a custom color
    if st.button("Summarize", help="Click to generate summary"):
        if text:
            model = Summarizer()
            summary = model(text)

            # Display summary with a highlighted background
            st.subheader("Summary:")
            st.markdown(f"> {summary}", unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()
