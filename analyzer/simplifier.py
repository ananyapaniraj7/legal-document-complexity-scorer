import requests
import os
import textstat


GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY",
    ""
)

API_URL = (
    "https://api.groq.com/openai/v1/chat/completions"
)


def passes_quality_gate(
    original,
    simplified
):

    if not simplified:
        return False

    if len(simplified.strip()) < 10:
        return False

    original_flesch = (
        textstat.flesch_reading_ease(
            original
        )
    )

    simplified_flesch = (
        textstat.flesch_reading_ease(
            simplified
        )
    )

    if simplified_flesch < original_flesch:
        return False

    return True


def simplify_sentence(sentence):

    headers = {

        "Authorization":
        f"Bearer {GROQ_API_KEY}",

        "Content-Type":
        "application/json"
    }

    payload = {

        "model": "llama-3.1-8b-instant",

        "messages": [

            {
                "role": "user",

                "content": (
                    "Simplify this legal sentence "
                    "into plain everyday English. "
                    "Return only the simplified "
                    "sentence.\n\n"
                    f"{sentence}"
                )
            }
        ],

        "temperature": 0.3,

        "max_tokens": 100
    }

    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload
        )

        result = response.json()
        if "choices" not in result:
            simplified = None
        else:

            simplified = result[
                "choices"
            ][0][
                "message"
            ][
                "content"
            ].strip()

    except Exception as e:

        simplified = None

    quality_ok = (
        passes_quality_gate(
            sentence,
            simplified
        )
        if simplified else False
    )

    return {

        "simplified": (
            simplified
            if quality_ok else None
        ),

        "quality_ok": quality_ok,

        "original_flesch": round(
            textstat.flesch_reading_ease(
                sentence
            ),
            1
        ),

        "simplified_flesch": round(
            textstat.flesch_reading_ease(
                simplified
            ),
            1
        ) if quality_ok else None,

        "grade_before": round(
            textstat.flesch_kincaid_grade(
                sentence
            ),
            1
        ),

        "grade_after": round(
            textstat.flesch_kincaid_grade(
                simplified
            ),
            1
        ) if quality_ok else None,
    }