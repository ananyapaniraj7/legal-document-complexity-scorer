from analyzer.readability import get_flesch_score,get_grade_level,analyze_text
from analyzer.preprocess import get_sentences,get_average_sentence_length
from analyzer.jargon_detector import detect_legal_terms,get_jargon_density
from analyzer.complexity import score_sentence,rank_sentences,explain_sentence
from analyzer.pipeline import analyze_document
from analyzer.simplifier import simplify_sentence

text = """
Notwithstanding any provisions contained herein, the receiving party shall, upon execution of this Agreement, indemnify and hold harmless the disclosing party against any and all liabilities, claims, damages, losses, or expenses arising directly or indirectly from the unauthorized disclosure of confidential information, except where such disclosure is required by applicable law or regulatory authority.

The employee agrees that during the term of employment and for a period of two years following termination, they shall not directly or indirectly engage in any business activities that compete with the employer within any jurisdiction in which the employer conducts substantial operations.

This agreement may be terminated by either party upon providing thirty days written notice; however, termination shall not relieve either party from obligations accrued prior to the effective termination date.
"""
# result=analyze_text(text)
# print(result)
# sentences=get_sentences(text)
# print(sentences)
# print(len(sentences))
# print(get_average_sentence_length(text))
# terms = detect_legal_terms(text)
# print(terms)
# density=get_jargon_density(text)
# print(density)

# sentences = get_sentences(text)

# for sentence in sentences:
#     print(sentence)
#     print(score_sentence(sentence))
#     print()

# ranked= rank_sentences(text)
# for item in ranked:
#     print(item["score"])
#     print(item["sentence"])
#     print()

# sentences=get_sentences(text)
# for sentence in sentences:
#     print(sentence)
#     print(explain_sentence(sentence))
#     print()

# result = analyze_document(text)

# print(result)
from analyzer.simplifier import simplify_sentence

sentence = """
The agreement may be terminated by either party upon written notice.
"""

print(simplify_sentence(sentence))