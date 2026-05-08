from analyzer.readability import get_flesch_score
from analyzer.jargon_detector import detect_legal_terms
from analyzer.preprocess import get_sentences


def score_sentence(sentence):
    readability=get_flesch_score(sentence)
    jargon_count=len(detect_legal_terms(sentence))
    word_count=len(sentence.split())
    score=(word_count *1.5+jargon_count*10+(100-readability))
    return round(score,2)

def rank_sentences(text):
    sentences=get_sentences(text)
    ranked=[]
    for sentence in sentences:
        score=score_sentence(sentence)
        ranked.append({
            "sentence":sentence,
            "score": score
        })
    ranked.sort(
        key=lambda x:x["score"],
        reverse=True
    )
    return ranked

def explain_sentence(sentence):
    explanations=[]

    word_count=len(sentence.split())
    if word_count>25:
        explanations.append("Long sentence structure")

    jargon_count=len(detect_legal_terms(sentence))

    if jargon_count>0:
        explanations.append(f"Contains {jargon_count} legal term(s)")
    
    readability= get_flesch_score(sentence)
    if(readability<30):
        explanations.append("Very difficult readability")
    
    return explanations