import textstat


def get_flesch_score(text):
    return textstat.flesch_reading_ease(text)


def get_grade_level(text):
    return textstat.flesch_kincaid_grade(text)


def get_difficulty_label(score):
    if(score>=90):
       return "Very Easy"
    elif(score>=80 and score<90):
        return "Easy"
    elif(score>=70 and score<80):
        return "Little less easy"
    elif(score>=50 and score<70):
        return "Moderate"
    elif(score>30 and score<50):
        return "difficult"
    else:
        return "Very difficult"

def analyze_text(text):
    flesch_score = get_flesch_score(text)

    grade_level = get_grade_level(text)

    difficulty = get_difficulty_label(flesch_score)
    return {
            "flesch_score":flesch_score,
            "grade_level":grade_level,
            "difficulty":difficulty

    }