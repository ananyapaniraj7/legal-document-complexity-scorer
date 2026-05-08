from analyzer.readability import get_flesch_score
from analyzer.jargon_detector import detect_legal_terms
from analyzer.preprocess import get_sentences


def score_sentence(sentence):
    readability=get_flesch_score(sentence)
    jargon_count=len(detect_legal_terms(sentence))
    word_count=len(sentence.split())
    score=(word_count *1.5+jargon_count*10+(100-readability))
    return round(score,2)