import spacy

nlp = spacy.load("en_core_web_sm")

def get_sentences(text):
    doc=nlp(text)
    sentences=[]
    for sent in doc.sents:
        sentences.append(sent.text.strip())
    return sentences

def get_average_sentence_length(text):
    sentences=get_sentences(text)
    total_words=0
    for sentence in sentences:
        words=sentence.split()
        count=len(words)
        total_words+=count
    average=total_words/len(sentences)
    return average
    