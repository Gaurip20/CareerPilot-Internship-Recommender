
def generate_questions(skills):

    questions = []

    if "Python" in skills:
        questions.extend([
            "Explain OOP in Python.",
            "Difference between List and Tuple?"
        ])

    if "Machine Learning" in skills:
        questions.extend([
            "What is supervised learning?",
            "Explain overfitting."
        ])

    if "SQL" in skills:
        questions.extend([
            "Difference between DELETE and TRUNCATE."
        ])

    questions.extend([
        "Tell me about yourself.",
        "Why should we hire you?"
    ])

    return questions
