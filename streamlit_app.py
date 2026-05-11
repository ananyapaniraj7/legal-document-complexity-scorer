import streamlit as st
from analyzer.pipeline import analyze_document
from analyzer.complexity import get_complexity_label
from PyPDF2 import PdfReader

def show_difficulty_level(level):
    if level=="Very difficult":
        st.error(f"Difficulty:{level}")

    elif level=="Difficult":
        st.warning(f"Difficulty:{level}")

    else:
        st.success(f"Difficulty:{level}")

st.title( "AI-Powered Legal Document Analyzer")

st.write(
    "Analyze legal documents for readability, complexity, and plain-English accessibility using NLP and AI."
)

text = st.text_area(
    "Paste Legal Document Here",
    height=300
)

uploaded_file=st.file_uploader(
    "Upload Legal PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    pdf_reader=PdfReader(uploaded_file)
    pdf_text=""
    for page in pdf_reader.pages:
        extracted=page.extract_text()
        if extracted:
            pdf_text+=extracted
    text=pdf_text
    st.success("PDf uploaded successfully")


analyze_button = st.button("Analyze Document")

if analyze_button:

    if text.strip()=="":
        st.warning(
            "Please enter a legal document."
        )
    else:
        with st.spinner(
        "Analyzing legal document..."
        ):
            result=analyze_document(text)

        readability = result["readability"]

        avg_length = result["average_sentence_length"]

        jargon_density = result["jargon_density"]

        st.header("Document Analysis Results")

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

        complexity_score = 100 - max(
            readability["flesch_score"],
            0
        )

        complexity_score = min(
            int(complexity_score),
            100
        )
        st.subheader("Complexity Level")

        st.progress(complexity_score)

        st.subheader("Document Statistics")

        st.write(
            f"Average Sentence Length: {avg_length} words"
        )
        st.subheader("AI Analysis of Complex Clauses")

        for item in result["top_complex_sentences"]:

            with st.expander(
                f"{get_complexity_label(item['score'])} • Score: {item['score']}"
            ):
                st.subheader("Original Sentence")

                st.write(item["sentence"])

                simplification=item["simplification"]

                if simplification["quality_ok"]:
                    st.subheader("AI Simplified Version")
                    st.success(simplification["simplified"])
                    col_a,col_b=st.columns(2)
                    with col_a:
                        st.metric(
                            "Before Grade",
                            simplification["grade_before"]
                        )
                    with col_b:
                        st.metric(
                            "After Grade",
                            simplification["grade_after"]
                        )
                else:
                    st.info("No reliable simplification generated.")


                st.write("Complexity Factors")

                for explanation in item["explanations"]:
                    st.write(f"- {explanation}")
    