def extract_skills(text):
    keywords = [
        "python", "java", "c", "c++", "sql", "html",
        "css", "javascript", "machine learning", "data analysis"
    ]
    found = []
    text = text.lower()

    for skill in keywords:
        if skill in text:
            found.append(skill)

    return found
