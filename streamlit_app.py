import streamlit as st
from analyzer.pipeline import analyze_document

st.title("Legal Document Complexity Scorer")

st.write(
    "Analyze legal documents for readability and complexity."
)

text = st.text_area(
    "Paste Legal Document Here",
    height=300
)
analyze_button = st.button("Analyze Document")
st.header("Document Analysis Results")
if analyze_button:
    result=analyze_document(text)
    readability = result["readability"]

    avg_length = result["average_sentence_length"]

    jargon_density = result["jargon_density"]
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Difficulty",
            readability["difficulty"]
        )

    with col2:
        st.metric(
            "Grade Level",
            round(readability["grade_level"], 2)
        )

    with col3:
        st.metric(
            "Jargon Density",
            f"{jargon_density}%"
        )
    st.subheader("Sentence Statistics")

    st.write(
        f"Average Sentence Length: {avg_length} words"
    )
    st.subheader("Most Complex Sentences")

    for item in result["top_complex_sentences"]:

        st.markdown("---")

        st.write(item["sentence"])

        st.write(f"Complexity Score: {item['score']}")

        st.write("Why flagged:")

        for explanation in item["explanations"]:
            st.write(f"- {explanation}")
    