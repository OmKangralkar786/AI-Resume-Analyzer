skills_list = [
    'python',
    'java',
    'react',
    'django',
    'sql',
    'javascript',
    'html',
    'css',
    'machine learning',
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills