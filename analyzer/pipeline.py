from analyzer.readability import analyze_text
from analyzer.preprocess import get_average_sentence_length
from analyzer.jargon_detector import get_jargon_density
from analyzer.complexity import rank_sentences, explain_sentence
from analyzer.simplifier import simplify_sentence

def analyze_document(text):
    readability_data=analyze_text(text)

    avg_sentence_length=get_average_sentence_length(text)

    jargon_density=get_jargon_density(text)

    ranked_sentences=rank_sentences(text)
    
    top_sentences=[]

    for item in ranked_sentences[:3]:
        sentence=item["sentence"]
        score=item["score"]
        explanations=explain_sentence(sentence)
        simplification=simplify_sentence(sentence)

        top_sentences.append({
            "sentence":sentence,
            "score":score,
            "explanations":explanations,
            "simplification":simplification
        })
    return{
        "readability":readability_data,
        "average_sentence_length":round(avg_sentence_length,2),
        "jargon_density":jargon_density,
        "top_complex_sentences":top_sentences
    }