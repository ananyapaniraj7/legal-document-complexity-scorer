import spacy
nlp=spacy.load("en_core_web_sm")

LEGAL_TERMS = {
    "notwithstanding",
    "indemnify",
    "herein",
    "hereinafter",
    "pursuant",
    "liability",
    "arbitration",
    "covenant",
    "termination",
    "confidential",
    "obligation",
    "damages",
    "disclosure",
    "agreement",
    "warrant"
}
def detect_legal_terms(text):
    doc=nlp(text)
    found_terms=[]
    for token in doc:
        word=token.text.lower()
        if word in LEGAL_TERMS:
            found_terms.append(word)
    return found_terms

def get_jargon_density(text):
    doc=nlp(text)
    total_words=0
    for token in doc:
        if token.is_alpha:
            total_words+=1
    legal_terms=detect_legal_terms(text)
    density=(len(legal_terms)/total_words)*100
    return round(density,2)